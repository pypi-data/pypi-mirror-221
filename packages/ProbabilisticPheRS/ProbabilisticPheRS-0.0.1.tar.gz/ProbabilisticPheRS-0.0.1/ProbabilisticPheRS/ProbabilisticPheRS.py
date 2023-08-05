import pandas as pd 
import numpy as np
from scipy.special import logsumexp
from scipy.stats import beta as beta_dist
from scipy.optimize import fsolve
import time
from scipy.optimize import fmin

from .PDSBase import InferenceDataStruct,PDSBase
from .MarginalFrequencyPrior import MarginalFrequencyPrior

SMALL_FLOAT=np.finfo(np.float64).eps
MINLOG = np.log(SMALL_FLOAT)


__version__ = "0.0.1"

class ProbabilisticPheRS(PDSBase):

	def _cosine_annealing_schedule(self, init_temp,max_temp,n_steps):
		t=np.linspace(0,1.0,n_steps)
		return init_temp+0.5*(max_temp-init_temp)*(1-np.cos(t*np.pi))




	def _convert_bounds_to_beta_prior(self,lower_bound,upper_bound,CI=0.99,tol=1e-8):
		mean=lower_bound+(upper_bound-lower_bound)/2.0
		init_denom=(1.0/mean)*100
		log_a=np.log(init_denom*mean)
		log_b=np.log(init_denom-np.exp(log_a))

		f=lambda x: np.sqrt((upper_bound-beta_dist(np.exp(x[0]),np.exp(x[1])).ppf(1.0-(1.0-CI)/2.0))**2+(lower_bound-beta_dist(np.exp(x[0]),np.exp(x[1])).ppf((1.0-CI)/2.0))**2)
		output=fmin(f,np.array([log_a,log_b]),ftol=tol,disp=False)
		return np.exp(output)



	def _initialize_indicators(self,inference_data_struct,training_phers_scores,exp_dis_prevalence,include_nuisance):

		if include_nuisance==False:
			inital_indicators=pd.DataFrame(np.zeros([inference_data_struct.training_index.shape[0],2],dtype=np.float64),index=inference_data_struct.training_index,columns=['Target','Independent'])
		else:
			inital_indicators=pd.DataFrame(np.zeros([inference_data_struct.training_index.shape[0],3],dtype=np.float64),index=inference_data_struct.training_index,columns=['Target','Nuisance','Independent'])

		symptomatic_patients=training_phers_scores[training_phers_scores>0.0].index
		symptomatic_patients_ranks=pd.Series(np.arange(0,symptomatic_patients.shape[0]),index=training_phers_scores[symptomatic_patients].sort_values()[::-1].index)
		total_num_disease_patients=exp_dis_prevalence*training_phers_scores.shape[0]

		if symptomatic_patients_ranks.shape[0]<=total_num_disease_patients:
			inital_indicators.loc[symptomatic_patients,'Target']=1.0
		else:
			approx_geom_rate=1.0-(1.0/total_num_disease_patients)
			symptomatic_patients_inds=approx_geom_rate**(symptomatic_patients_ranks)
			inital_indicators.loc[symptomatic_patients,'Target']=symptomatic_patients_inds

		if include_nuisance:
			inital_indicators.loc[symptomatic_patients,'Nuisance']=1.0-inital_indicators.loc[symptomatic_patients,'Target']
		else:
			inital_indicators.loc[symptomatic_patients,'Independent']=1.0-inital_indicators.loc[symptomatic_patients,'Target']

		inital_indicators.loc[inital_indicators.index.difference(symptomatic_patients),'Independent']=1.0
		
		inital_indicators.where(inital_indicators<1.0,1.0-SMALL_FLOAT,inplace=True)
		inital_indicators.where(inital_indicators>=SMALL_FLOAT,SMALL_FLOAT,inplace=True)
		return inital_indicators



	def _model_marg_like_compute_posteriors(self,inference_data_struct,has_disease_inds,target_prior,nuisance_prior,hyperparameters,beta_temp=1.0):

		# first compute posteriors
		
		target_counts,nuisance_counts,ind_counts=inference_data_struct._compute_counts(has_disease_inds)

		target_set_posterior=((beta_temp*target_prior).add(target_counts*beta_temp))-beta_temp+1.0
		if nuisance_counts is not None:
			nuisance_posterior=((beta_temp*nuisance_prior).add(beta_temp*nuisance_counts))-beta_temp+1.0
		else:
			nuisance_posterior=pd.Series([],dtype=np.float64)

		independent_posteriors=(ind_counts*beta_temp+hyperparameters['independent_freq_prior']*beta_temp)-beta_temp+1.0
		disease_prevalence_posteriors=(hyperparameters['prevalence_prior']*beta_temp+has_disease_inds.sum(axis=0).values*beta_temp)-beta_temp+1.0

		exp_log_freqs_target=pd.Series(self._dirichlet_exp_logx(target_set_posterior.values),index=target_set_posterior.index)
		if nuisance_posterior.shape[0]>0:
			exp_log_freqs_nuisance=pd.Series(self._dirichlet_exp_logx(nuisance_posterior.values),index=nuisance_posterior.index)
		else:
			exp_log_freqs_nuisance=None

		exp_log_ind_freqs=np.vstack([self._dirichlet_exp_logx(x) for x in independent_posteriors])
		exp_log_dis_class=self._dirichlet_exp_logx(disease_prevalence_posteriors)

		posteriors={'TargetSetFreqs':target_set_posterior,'NuisanceSetFreqs':nuisance_posterior,'IndependentSymptomFreqs':independent_posteriors,'DiseasePrev':disease_prevalence_posteriors}


		
		# now compute marg like
		marg_like=0.0

		#first symptomatic patient likelihoods
		symptomatic_pt_sets=inference_data_struct.symptomatic_patients_to_unique_sets.loc[inference_data_struct.symptomatic_in_training]
		target_dis_inds=has_disease_inds.loc[inference_data_struct.symptomatic_in_training,'Target']

		marg_like+=np.sum(target_dis_inds*(exp_log_dis_class[0]+exp_log_freqs_target.loc[symptomatic_pt_sets].values)-(1.0/beta_temp)*target_dis_inds*np.log(target_dis_inds))

		if exp_log_freqs_nuisance is not None:
			nuisance_dis_inds=has_disease_inds.loc[inference_data_struct.symptomatic_in_training,'Nuisance']
			marg_like+=np.sum(nuisance_dis_inds*(exp_log_dis_class[1]+exp_log_freqs_nuisance.loc[symptomatic_pt_sets].values)-(1.0/beta_temp)*nuisance_dis_inds*np.log(nuisance_dis_inds))
		
		independent_likelihoods=inference_data_struct._return_set_indepedent_likelihoods(exp_log_ind_freqs[:,0],exp_log_ind_freqs[:,1])
		independent_dis_inds=has_disease_inds.loc[inference_data_struct.symptomatic_in_training,'Independent']

		marg_like+=np.sum(independent_dis_inds*(exp_log_dis_class[-1]+independent_likelihoods.loc[symptomatic_pt_sets].values)-(1.0/beta_temp)*independent_dis_inds*np.log(independent_dis_inds))

		#then asymptomatic likelihoods
		target_dis_inds=has_disease_inds.loc[inference_data_struct.asymptomatic_in_training,'Target']
		marg_like+=np.sum(target_dis_inds*(exp_log_dis_class[0]+exp_log_freqs_target.loc['-1'])-(1.0/beta_temp)*target_dis_inds*np.log(target_dis_inds))

		independent_dis_inds=has_disease_inds.loc[inference_data_struct.asymptomatic_in_training,'Independent']
		marg_like+=np.sum(independent_dis_inds*(exp_log_dis_class[-1]+np.sum(exp_log_ind_freqs[:,1]))-(1.0/beta_temp)*independent_dis_inds*np.log(independent_dis_inds))
		


		# now priors
		marg_like+=self._dirichlet_log_like(exp_log_freqs_target.loc[target_prior.index].values,target_prior.values)+(1.0/beta_temp)*self._dirichlet_entropy(target_set_posterior.values)


		if exp_log_freqs_nuisance is not None:
			marg_like+=self._dirichlet_log_like(exp_log_freqs_nuisance.loc[nuisance_prior.index].values,nuisance_prior.values)+(1.0/beta_temp)*self._dirichlet_entropy(nuisance_posterior.values)
		
		marg_like+=np.sum([(self._dirichlet_log_like(exp_log_ind_freqs[i],hyperparameters['independent_freq_prior'])+(1.0/beta_temp)*self._dirichlet_entropy(independent_posteriors[i])) for i in range(exp_log_ind_freqs.shape[0])])

		marg_like+=self._dirichlet_log_like(exp_log_dis_class,hyperparameters['prevalence_prior'])+(1.0/beta_temp)*self._dirichlet_entropy(disease_prevalence_posteriors)
		
		return marg_like,posteriors,target_counts



	def _update_disease_indicators(self,inference_data_struct,posteriors,beta_temp=1.0):

		# first compute posterior expectations
		exp_log_target_freqs=pd.Series(self._dirichlet_exp_logx(posteriors['TargetSetFreqs'].values),index=posteriors['TargetSetFreqs'].index)
		if posteriors['NuisanceSetFreqs'].shape[0]>0:
			exp_log_nuisance_freqs=pd.Series(self._dirichlet_exp_logx(posteriors['NuisanceSetFreqs'].values),index=posteriors['NuisanceSetFreqs'].index)
		else:
			exp_log_nuisance_freqs=None

		exp_log_ind_freqs=np.vstack([self._dirichlet_exp_logx(x) for x in posteriors['IndependentSymptomFreqs']])		
		exp_log_dis_class=self._dirichlet_exp_logx(posteriors['DiseasePrev'])

		#symptomatic first
		symptomatic_pt_sets=inference_data_struct.symptomatic_patients_to_unique_sets.loc[inference_data_struct.symptomatic_in_training]

		symptomatic_log_probs=np.zeros((symptomatic_pt_sets.shape[0],2+int(exp_log_nuisance_freqs is not None)))

		#target
		symptomatic_log_probs[:,0]=exp_log_dis_class[0]+exp_log_target_freqs.loc[symptomatic_pt_sets].values

		#nuisance
		if exp_log_nuisance_freqs is not None:
			symptomatic_log_probs[:,1]=exp_log_dis_class[1]+exp_log_nuisance_freqs.loc[symptomatic_pt_sets].values

		#independent
		independent_likelihoods=inference_data_struct._return_set_indepedent_likelihoods(exp_log_ind_freqs[:,0],exp_log_ind_freqs[:,1])
		symptomatic_log_probs[:,-1]=exp_log_dis_class[-1]+independent_likelihoods.loc[symptomatic_pt_sets].values


		norm_const = logsumexp(beta_temp*symptomatic_log_probs,axis=1)
		symptomatic_probs=np.exp(beta_temp*symptomatic_log_probs-norm_const.reshape(-1,1))
		symptomatic_probs[symptomatic_probs<SMALL_FLOAT]=SMALL_FLOAT
		symptomatic_probs[symptomatic_probs>(1.0-SMALL_FLOAT)]=(1.0-SMALL_FLOAT)

		#now asymptomatic

		asymptomatic_log_prob=np.array([exp_log_dis_class[0]+exp_log_target_freqs.loc['-1']]+[-np.inf]*(exp_log_nuisance_freqs is not None)+[exp_log_dis_class[-1]+np.sum(exp_log_ind_freqs[:,1])])
		norm_const = logsumexp(beta_temp*asymptomatic_log_prob)
		asymptomatic_probs=np.exp(beta_temp*asymptomatic_log_prob-norm_const)


		asymptomatic_probs=np.ones((inference_data_struct.asymptomatic_in_training.shape[0],asymptomatic_probs.shape[0]))*asymptomatic_probs
		asymptomatic_probs[asymptomatic_probs<SMALL_FLOAT]=SMALL_FLOAT
		asymptomatic_probs[asymptomatic_probs>(1.0-SMALL_FLOAT)]=(1.0-SMALL_FLOAT)

		return pd.DataFrame(np.vstack([symptomatic_probs,asymptomatic_probs]),index=np.concatenate([inference_data_struct.symptomatic_in_training,inference_data_struct.asymptomatic_in_training]),columns=['Target']+['Nuisance']*(exp_log_nuisance_freqs is not None)+['Independent']).sort_index()


	def _predict_disease_inds_testing(self,inference_data_struct,posteriors):

		# first compute posterior expectations
		exp_log_target_freqs=pd.Series(self._dirichlet_exp_logx(posteriors['TargetSetFreqs'].values),index=posteriors['TargetSetFreqs'].index)
		if posteriors['NuisanceSetFreqs'].shape[0]>0:
			exp_log_nuisance_freqs=pd.Series(self._dirichlet_exp_logx(posteriors['NuisanceSetFreqs'].values),index=posteriors['NuisanceSetFreqs'].index)
		else:
			exp_log_nuisance_freqs=None

		exp_log_ind_freqs=np.vstack([self._dirichlet_exp_logx(x) for x in posteriors['IndependentSymptomFreqs']])		
		exp_log_dis_class=self._dirichlet_exp_logx(posteriors['DiseasePrev'])

		symptomatic_in_testing=inference_data_struct.all_symptomatic_cases.index.difference(inference_data_struct.symptomatic_in_training)
		asymptomatic_in_testing=inference_data_struct.all_asymptomatic_cases.index.difference(inference_data_struct.asymptomatic_in_training)

		#symptomatic first
		symptomatic_pt_sets=inference_data_struct.symptomatic_patients_to_unique_sets.loc[symptomatic_in_testing]

		symptomatic_log_probs=np.zeros((symptomatic_pt_sets.shape[0],2+int(exp_log_nuisance_freqs is not None)))

		#target
		symptomatic_log_probs[:,0]=exp_log_dis_class[0]+exp_log_target_freqs.loc[symptomatic_pt_sets].values

		#nuisance
		if exp_log_nuisance_freqs is not None:
			symptomatic_log_probs[:,1]=exp_log_dis_class[1]+exp_log_nuisance_freqs.loc[symptomatic_pt_sets].values

		#independent
		independent_likelihoods=inference_data_struct._return_set_indepedent_likelihoods(exp_log_ind_freqs[:,0],exp_log_ind_freqs[:,1])
		symptomatic_log_probs[:,-1]=exp_log_dis_class[-1]+independent_likelihoods.loc[symptomatic_pt_sets].values


		norm_const = logsumexp(symptomatic_log_probs,axis=1)
		symptomatic_probs=np.exp(symptomatic_log_probs-norm_const.reshape(-1,1))
		symptomatic_probs[symptomatic_probs<SMALL_FLOAT]=SMALL_FLOAT
		symptomatic_probs[symptomatic_probs>(1.0-SMALL_FLOAT)]=(1.0-SMALL_FLOAT)

		#now asymptomatic

		asymptomatic_log_prob=np.array([exp_log_dis_class[0]+exp_log_target_freqs.loc['-1']]+[-np.inf]*(exp_log_nuisance_freqs is not None)+[exp_log_dis_class[-1]+np.sum(exp_log_ind_freqs[:,1])])
		norm_const = logsumexp(asymptomatic_log_prob)
		asymptomatic_probs=np.exp(asymptomatic_log_prob-norm_const)


		asymptomatic_probs=np.ones((asymptomatic_in_testing.shape[0],asymptomatic_probs.shape[0]))*asymptomatic_probs
		asymptomatic_probs[asymptomatic_probs<SMALL_FLOAT]=SMALL_FLOAT
		asymptomatic_probs[asymptomatic_probs>(1.0-SMALL_FLOAT)]=(1.0-SMALL_FLOAT)

		return pd.DataFrame(np.vstack([symptomatic_probs,asymptomatic_probs]),index=np.concatenate([symptomatic_in_testing,asymptomatic_in_testing]),columns=['Target']+['Nuisance']*(exp_log_nuisance_freqs is not None)+['Independent']).sort_index()


	def Fit(self,hpo_info,prevalence_interval,include_prior_information=False,update_prior=False,include_nuisance=False,stochastic_prior_init=False,verbose=True,max_sub_iter=500,max_global_iter=50,error_tol=1e-8,**model_kwargs):

		"""Summary
		
		Args:
		    hpo_terms (TYPE): Description
		    prevalence_prior (TYPE): Description
		    annotation_rates (TYPE): Description
		    frequency_info (TYPE): Description
		    independent_freq_prior (list, optional): Description
		    max_iter (int, optional): Description
		    error_tol (float, optional): Description
		    verbose (bool, optional): Description
		    init_prior_strength (float, optional): Description
		    init_prior_smoothing (TYPE): Description
		    update_prior_params (bool, optional): Description
		
		Returns:
		    TYPE: Description
		"""

		assert isinstance(hpo_info, pd.DataFrame),"Expects a pd.DataFrame of HPO-specific prior information."
		assert len(hpo_info.columns),"hpo_info must contain at least two columns. The first must contain the probability that the symptom is correctly annotated, and the second should specify the prior over symptom frequency."
		missing_terms=set(hpo_info.index).difference(self.hpo_term_columns)
		if len(missing_terms)>0:
			print('Warning: {0:s} are not in the datset. Note: they may have been dropped because their frequency was too low.'.format(','.join(missing_terms)))
			hpo_terms=list(hpo_info.index.intersection(self.hpo_term_columns))
			assert len(hpo_terms)>0,"No symptoms found in the dataset."
			hpo_info=hpo_info.loc[hpo_terms]

		hyperparameters={}

		inference_data_struct=self._build_inference_data_struct(hpo_info.index)


		if include_nuisance:
			assert include_prior_information==True,"Without specifying prior information, a model with nuisance diseases present is non-identifiable. Please remove nuisance diseases or include prior information."
		if update_prior:
			assert include_prior_information==True,"Cannot update target disease prior distribution without some amount of prior information."

		hyperparameters['include_prior_information']=include_prior_information
		hyperparameters['include_nuisance']=include_nuisance
		hyperparameters['update_prior']=update_prior
		hyperparameters['stochastic_prior_init']=stochastic_prior_init
		

		
		assert len(prevalence_interval)==2,"Expected a python iterable with two entries for the prevalence prior information."
		assert (prevalence_interval[0]<1.0) and (prevalence_interval[1]<1.0),"Prevalence limits must be less than 1.0"
		assert prevalence_interval[0]<prevalence_interval[1],"The lower limit of the prevalence interval must be less than the upper interval"

		if 'prevalence_confidence' in model_kwargs.keys():
			assert (model_kwargs['prevalence_confidence']>0.0) and (model_kwargs['prevalence_confidence']<1.0),"prevalence_confidence must lie within (0.0,1.0)"
			prevalence_confidence=model_kwargs['prevalence_confidence']
		else:
			prevalence_confidence=0.99
		target_prevalence_prior=self._convert_bounds_to_beta_prior(prevalence_interval[0],prevalence_interval[1],CI=prevalence_confidence)

		if include_nuisance:
			if 'nuisance_relative_exp_prevalence' in model_kwargs.keys():
				assert (model_kwargs['nuisance_relative_exp_prevalence']>0.0),"nuisance_relative_exp_prevalence must be greater than 0.0"
				nuisance_relative_exp_prevalence=model_kwargs['nuisance_relative_exp_prevalence']
			else:
				nuisance_relative_exp_prevalence=10.0
			
			#adjust target_prevalence_prior
			new_prior=np.zeros(3)
			new_prior[0]=target_prevalence_prior[0]
			new_prior[1]=target_prevalence_prior[0]*nuisance_relative_exp_prevalence
			new_prior[2]=target_prevalence_prior[1]-np.sum(new_prior[0:2])

			assert new_prior[-1]>0,"Based on prevalence prior information for the target disease, cannot create a proper prior distribution over all target and nuisance states. Must decrease  target disease prior prevalence and/or nuisance disease relative expected prevalence."
			hyperparameters['prevalence_prior']=new_prior
		else:
			hyperparameters['prevalence_prior']=np.array(target_prevalence_prior,dtype=np.float64)

		if 'independent_freq_prior' in model_kwargs.keys():
			assert len(model_kwargs['independent_freq_prior'])==2,"independent_freq_prior must be an iterable containing two floats."
			hyperparameters['independent_freq_prior']=np.array(model_kwargs['independent_freq_prior'],dtype=np.float64)
		else:
			hyperparameters['independent_freq_prior']=np.array([10,1000.0])


		if 'independent_freq_prior' in model_kwargs.keys():
			assert len(model_kwargs['independent_freq_prior'])==2,"independent_freq_prior must be an iterable containing two floats."
			hyperparameters['independent_freq_prior']=np.array(model_kwargs['independent_freq_prior'],dtype=np.float64)
		else:
			hyperparameters['independent_freq_prior']=np.array([10,1000.0])	


		if 'target_prior_strength' in model_kwargs.keys():
			assert isinstance(model_kwargs['target_prior_strength'],float) and (model_kwargs['target_prior_strength']>0.0),"target_prior_strength must be a float > 0.0."
			hyperparameters['target_prior_strength']=model_kwargs['target_prior_strength']
		else:
			hyperparameters['target_prior_strength']=float(inference_data_struct.unique_symptom_sets.shape[0])
			

		if 'target_prior_smoothing' in model_kwargs.keys():
			assert isinstance(model_kwargs['target_prior_smoothing'],float) and (model_kwargs['target_prior_smoothing']>0.0) and (model_kwargs['target_prior_smoothing']<1.0),"target_prior_smoothing must be a float in (0.0,1.0). Recommend a value very close to 1.0."
			hyperparameters['target_prior_smoothing']=model_kwargs['target_prior_strength']
		else:
			hyperparameters['target_prior_smoothing']=1.0-SMALL_FLOAT
	

		if 'nuisance_prior_strength' in model_kwargs.keys():
			assert isinstance(model_kwargs['nuisance_prior_strength'],float) and (model_kwargs['nuisance_prior_strength']>0.0),"nuisance_prior_strength must be a float and greater than 0. Recommend a value close to 1.0."
			hyperparameters['nuisance_prior_strength']=model_kwargs['nuisance_prior_strength']
		else:
			hyperparameters['nuisance_prior_strength']=1.0	
		
		assert hyperparameters['nuisance_prior_strength']<hyperparameters['target_prior_strength'],"Note: nuisance_prior_strength is specified to be greater than or equal to target_prior_strength. This tends to cause the model to converge to a disease distinct. Recommend decreasing nuisance parameter strength"


		##### need to create final data table!!!!!######
		##### stores interim results######
		
		if include_prior_information:
			if len(hpo_info.columns)==2:
				marg_freq_prior=MarginalFrequencyPrior(hpo_info.index,hpo_info[hpo_info.columns[0]].values,hpo_info[hpo_info.columns[1]].values,inference_data_struct,init_strength=hyperparameters['target_prior_strength'],stochastic_init=stochastic_prior_init)
			else:
				marg_freq_prior=MarginalFrequencyPrior(hpo_info.index,hpo_info[hpo_info.columns[0]].values,hpo_info[hpo_info.columns[1]].values,inference_data_struct,init_strength=hyperparameters['target_prior_strength'],symptom_frequencies=hpo_info[hpo_info.columns[2]],stochastic_init=stochastic_prior_init)
			target_priors=marg_freq_prior.symptom_set_dirichlet_params
		else:

			target_priors=pd.Series(np.ones((inference_data_struct.unique_symptom_sets.shape[0]+1))*hyperparameters['target_prior_strength']/inference_data_struct.unique_symptom_sets.shape[0],index=np.concatenate([inference_data_struct.unique_symptom_sets.index,np.array(['-1'])]))
			target_priors.update(pd.Series([SMALL_FLOAT],index=['-1']))

		if include_nuisance:
			nuisance_priors=pd.Series(np.ones(target_priors.shape[0]-1)*(hyperparameters['nuisance_prior_strength']/(target_priors.shape[0]-1)),index=target_priors.index.drop('-1'))
		else:
			nuisance_priors=pd.Series([],dtype=np.float64)

		
		#initialize posteriors
		#Compute PheRS results, and use these results initialize disease indicators

		phers_results=self.PheRS(hpo_info.index)

		has_disease_indicators_training=self._initialize_indicators(inference_data_struct,phers_results['Training'],target_prevalence_prior[0]/target_prevalence_prior.sum(),include_nuisance)

		marginal_log_like,posteriors,target_counts=self._model_marg_like_compute_posteriors(inference_data_struct,has_disease_indicators_training,target_priors, nuisance_priors, hyperparameters)

		if include_prior_information:
			dirichlet_loss,prior_loss,total_loss=marg_freq_prior.ReturnLossComponents(target_counts,1.0)
			global_marginal_log_like=marginal_log_like+prior_loss

		if verbose:
			if include_prior_information:
				print('Fitting ProbabalisticPheRS Model. Initial marginal log-likelihood (lower-bound, including prior): {0:f}'.format(global_marginal_log_like))
			else:
				print('Fitting ProbabalisticPheRS Model. Initial marginal log-likelihood (lower-bound): {0:f}'.format(marginal_log_like))

		current_iter=0
		global_iter=0
		inference_complete=False
		while (current_iter<=max_sub_iter) and (inference_complete==False) and (global_iter<=max_global_iter):

			has_disease_indicators_training=self._update_disease_indicators(inference_data_struct,posteriors)
			new_marginal_log_like,posteriors,target_counts=self._model_marg_like_compute_posteriors(inference_data_struct,has_disease_indicators_training,target_priors, nuisance_priors, hyperparameters)
			current_iter+=1
			error=(new_marginal_log_like-marginal_log_like)/(-1.0*new_marginal_log_like)

			if error<error_tol:
				if (include_prior_information==False):
					if verbose:
						print('Probabilistic PheRS Inference Complete. Final marginal log-likelihood: {0:f}'.format(new_marginal_log_like))
					marginal_log_like=new_marginal_log_like
					inference_complete=True
				else:
					if verbose:
						print('Sub-inference complete. Current global iterations: {2:d}. Current partial marginal log-likelihood: {0:f} (Error: {1:e})'.format(new_marginal_log_like,error,global_iter))
					if update_prior:
						loss=marg_freq_prior.UpdatePriorParams(target_counts,1.0,error_tol=error_tol,verbose=False)
						new_global_marginal_log_like,posteriors,target_counts=self._model_marg_like_compute_posteriors(inference_data_struct,has_disease_indicators_training,target_priors, nuisance_priors, hyperparameters)
					else:
						new_global_marginal_log_like=new_marginal_log_like

					dirichlet_loss,prior_loss,total_loss=marg_freq_prior.ReturnLossComponents(target_counts,1.0)
					new_global_marginal_log_like+=prior_loss
					global_iter+=1
					error=(new_global_marginal_log_like-global_marginal_log_like)/(-1.0*new_global_marginal_log_like)
					if error<error_tol:
						if verbose:
							print('Probabilistic PheRS Inference Complete. Final marginal log-likelihood: {0:f}'.format(new_global_marginal_log_like))

						global_marginal_log_like=new_global_marginal_log_like
						inference_complete=True
					else:
						if verbose:
							print('Completed {0:d} global iterations. Current marginal log-likelihood: {1:f} (Error: {2:e})'.format(global_iter,new_global_marginal_log_like,error))
						global_marginal_log_like=new_global_marginal_log_like
						marginal_log_like=global_marginal_log_like-prior_loss
						current_iter=0

			else:

				if verbose:
					if (include_prior_information==False):
						print('Completed {0:d} iterations. Current marginal log-likelihood: {1:f} (Error: {2:e})'.format(current_iter,new_marginal_log_like,error))
					else:
						print('Completed {0:d} sub-iterations. Current global iterations: {3:d}. Current partial marginal log-likelihood: {1:f} (Error: {2:e})'.format(current_iter,new_marginal_log_like,error,global_iter))
				marginal_log_like=new_marginal_log_like


		if (current_iter==max_sub_iter) or (global_iter==max_global_iter):
			print("Warning: Inference failed to occur in allotted iterations. The quality of the inference results is uncertain.")


		if self.testing_index.shape[0]>0:
			print('Computing posterior predictions on withheld data...')
			testing_scores = self._predict_disease_inds_testing(inference_data_struct,posteriors)
		else:
			testing_scores = pd.DataFrame([],columns=has_disease_indicators_training.columns,index=self.testing_index)


		return_data_structure={}
		if include_prior_information:
			return_data_structure['MarginalLogLike']=global_marginal_log_like
		else:
			return_data_structure['MarginalLogLike']=marginal_log_like

		return_data_structure['ParameterPosteriors']=posteriors

		if include_prior_information:
			return_data_structure['TargetDirichletPrior']=target_priors
			return_data_structure['SymptomSpecificPosteriors']=marg_freq_prior.posterior_info
			return_data_structure['PriorAuxParams']=marg_freq_prior.aux_params

		final_indicator_table_training=pd.DataFrame(np.zeros([has_disease_indicators_training.shape[0],2]),columns=['ProbPheRS','PheRS'],index=has_disease_indicators_training.index)
		final_indicator_table_testing=pd.DataFrame(np.zeros([testing_scores.shape[0],2]),columns=['ProbPheRS','PheRS'],index=testing_scores.index)

		final_indicator_table_training['PheRS']=phers_results['Training']
		final_indicator_table_testing['PheRS']=phers_results['Testing']

		final_indicator_table_training['ProbPheRS']=has_disease_indicators_training['Target']
		final_indicator_table_testing['ProbPheRS']=testing_scores['Target']


		return_data_structure['TrainingResults']=final_indicator_table_training
		return_data_structure['TestingResults']=final_indicator_table_testing

		return return_data_structure

	


import pandas as pd 
import numpy as np
from scipy.special import betaln,logsumexp,logit,expit
from scipy.stats import beta as beta_dist
from PiecewiseBeta.PiecewiseBeta import PiecewiseBeta
from collections.abc import Iterable

from .DirichletPriorOptimizer import DirichletPriorOptimizer

SMALL_FLOAT=np.finfo(np.float64).eps
MINLOG = np.log(np.finfo(np.float64).eps)

class MarginalFrequencyPrior:

	def _simple_beta_marg_like(self,a,b,successes,failures,stochastic_init=False):
		return betaln(a+successes,b+failures)-betaln(a,b)

	def _symptom_log_marginals_beta_pieces(self, annot_prob,segment_probs,stochastic_init=False):
		if annot_prob==0.0:
			annot_prob=SMALL_FLOAT
		elif annot_prob==1.0:
			annot_prob=1.0-SMALL_FLOAT

		segment_probs=np.array(segment_probs)
		segment_probs/=segment_probs.sum()

		pbeta=PiecewiseBeta(self.piecewise_beta_cut_points,self.linked_frequency_prior_params[0],self.linked_frequency_prior_params[1])
		if stochastic_init:
			log_symptom_freq=np.log(pbeta.RandomVariates(segment_probs,1)[0])
			log_1m_symptom_freq=np.log(1.0-np.exp(log_symptom_freq))
		else:
			log_symptom_freq=pbeta.MarginalLogLikelihood(segment_probs,1,1)
			log_1m_symptom_freq=pbeta.MarginalLogLikelihood(segment_probs,0,1)

		obs_log_prob=np.logaddexp(np.log(annot_prob)+log_symptom_freq,np.log(1.0-annot_prob)+self._simple_beta_marg_like(self.unlinked_frequency_prior_params[0],self.unlinked_frequency_prior_params[1],1,1))
		unobs_log_prob=np.logaddexp(np.log(annot_prob)+log_1m_symptom_freq,np.log(1.0-annot_prob)+self._simple_beta_marg_like(self.unlinked_frequency_prior_params[0],self.unlinked_frequency_prior_params[1],0,1))
		
		return np.exp(log_symptom_freq),obs_log_prob,unobs_log_prob



	def _symptom_log_marginals_counts(self,annot_prob,successes, total,stochastic_init=False):
		if annot_prob==0.0:
			annot_prob=SMALL_FLOAT
		elif annot_prob==1.0:
			annot_prob=1.0-SMALL_FLOAT

		if stochastic_init:
			log_symptom_freq=np.log(beta_dist(self.linked_frequency_prior_params[0]+successes,self.linked_frequency_prior_params[1]+total-successes).rvs())
			log_1m_symptom_freq=np.log(1.0-np.exp(log_symptom_freq))
		else:
			log_symptom_freq=self._simple_beta_marg_like(self.linked_frequency_prior_params[0]+successes,self.linked_frequency_prior_params[1]+total-successes,1,0)
			log_1m_symptom_freq=self._simple_beta_marg_like(self.linked_frequency_prior_params[0]+successes,self.linked_frequency_prior_params[1]+total-successes,0,1)

		obs_log_prob=np.logaddexp(np.log(annot_prob)+log_symptom_freq,np.log(1.0-annot_prob)+self._simple_beta_marg_like(self.unlinked_frequency_prior_params[0],self.unlinked_frequency_prior_params[1],1,0))

		unobs_log_prob=np.logaddexp(np.log(annot_prob)+log_1m_symptom_freq,np.log(1.0-annot_prob)+self._simple_beta_marg_like(self.unlinked_frequency_prior_params[0],self.unlinked_frequency_prior_params[1],0,1))

		return np.exp(log_symptom_freq),obs_log_prob,unobs_log_prob

	def _symptom_log_freq_transform(self,annot_prob,symptom_freq):
		if annot_prob==0.0:
			annot_prob=SMALL_FLOAT
		elif annot_prob==1.0:
			annot_prob=1.0-SMALL_FLOAT

		log_symptom_freq=np.log(symptom_freq)
		log_1m_symptom_freq=np.log(1.0-symptom_freq)

		obs_log_prob=np.logaddexp(np.log(annot_prob)+log_symptom_freq,np.log(1.0-annot_prob)+self._simple_beta_marg_like(self.unlinked_frequency_prior_params[0],self.unlinked_frequency_prior_params[1],1,0))

		unobs_log_prob=np.logaddexp(np.log(annot_prob)+log_1m_symptom_freq,np.log(1.0-annot_prob)+self._simple_beta_marg_like(self.unlinked_frequency_prior_params[0],self.unlinked_frequency_prior_params[1],0,1))
		return np.exp(log_symptom_freq),obs_log_prob,unobs_log_prob


	def _process_freq_info(self,hpo,annot_rate,freq_info,stochastic_init=False):

		if isinstance(freq_info,tuple):
			assert len(freq_info)==2,"Frequency information for HPO {0:s} data type 'tuple' does not match expectations. Must have two entries.".format(hpo)
			assert freq_info[1]>=freq_info[0],"Frequency counts for HPO {0:s} are improper. Must be in (successes, total) format."
			return self._symptom_log_marginals_counts(annot_rate,freq_info[0],freq_info[1],stochastic_init=stochastic_init)+(False,)
		elif isinstance(freq_info,Iterable):
			freq_info=np.array(freq_info)
			assert len(freq_info)==(self.piecewise_beta_cut_points.shape[0]-1),"Frequency information for HPO {0:s} data type 'frequency classes' does not match expectations. Number of entries must match provided beta distribution cut points".format(hpo)
			return self._symptom_log_marginals_beta_pieces(annot_rate,freq_info,stochastic_init=stochastic_init)+(True,)
		else: 
			raise ValueError("Error in frequency informaton for HPO {0:s}. Frequency information must either be a tuple of length 2 or a vector of frequency classes.".format(hpo))

	def __init__(self,hpo_ids,annotation_rates,symptom_frequency_priors,inference_data_struct,symptom_frequencies=None,stochastic_init=False,piecewise_beta_cut_points=[0.0,0.04,0.3,0.8,0.99,1.0],linked_frequency_prior_params=[1.25,1.25],unlinked_frequency_prior_params=[10.0,1000.0],update_smoothing=True,update_strength=True,update_frequencies=True,update_indicators=True,init_smoothing=0.999999,init_strength=1.0,strength_penalty=0.1):


		self.piecewise_beta_cut_points=np.array(piecewise_beta_cut_points)
		self.linked_frequency_prior_params=np.array(linked_frequency_prior_params)
		self.unlinked_frequency_prior_params=np.array(unlinked_frequency_prior_params)
		self.hpo_col_indexes=inference_data_struct.hpo_column_labels
		self.symptom_sets=inference_data_struct.unique_symptom_sets.copy()
		self.symptom_sets=pd.concat([self.symptom_sets,pd.Series([np.array([])],index=['-1'])])
		if symptom_frequencies is not None:
			assert isinstance(symptom_frequencies,pd.Series),"If symptom frequencies provided, expect a dictionary of hpo-frequency value pairs. Note, not every hpo term must be included."

		assert (len(hpo_ids)==len(annotation_rates)) and (len(hpo_ids)==len(symptom_frequency_priors)),"Length of prior information does not match."
		self.prior_info=pd.DataFrame([],columns=['AnnotPrior','IsPiecewise','FreqPrior','FreqValue'],index=hpo_ids)
		self.prior_info=self.prior_info.astype({"AnnotPrior": float, "IsPiecewise": bool,'FreqValue':float})
		self.posterior_info=pd.DataFrame([],columns=['IsAnnotProb','SymptomFreq','LogFreqPresent','LogFreqAbsent'],index=hpo_ids)
		self.posterior_info=self.posterior_info.astype({'IsAnnotProb':float,'SymptomFreq':float,'LogFreqPresent':float,'LogFreqAbsent':float})
		self.aux_params={'Strength':init_strength,'Smoothing':init_smoothing,'UnlinkedFrequency':unlinked_frequency_prior_params[0]/sum(unlinked_frequency_prior_params)}


		for i in range(len(hpo_ids)):
			hpo=hpo_ids[i]
			rate=annotation_rates[i]
			freq_prior=symptom_frequency_priors[i]
			self.prior_info.at[hpo,'FreqPrior']=freq_prior
			self.prior_info.loc[hpo,'AnnotPrior']=rate
			output=self._process_freq_info(hpo,rate,freq_prior,stochastic_init=stochastic_init)
			self.prior_info.loc[hpo,'IsPiecewise']=output[3]

			if (symptom_frequencies is not None) and (hpo in symptom_frequencies.index) and (pd.isna(symptom_frequencies.loc[hpo])==False):
				output=self._symptom_log_freq_transform(rate,symptom_frequencies.loc[hpo])
			self.posterior_info.loc[hpo,'SymptomFreq']=output[0]
			self.posterior_info.loc[hpo,'LogFreqPresent']=output[1]
			self.posterior_info.loc[hpo,'LogFreqAbsent']=output[2]
			self.posterior_info.loc[hpo,'IsAnnotProb']=rate
		
		#initialize prior weights
		self.symptom_set_dirichlet_params=pd.Series(np.zeros(inference_data_struct.unique_symptom_sets.shape[0]+1),index=np.concatenate([inference_data_struct.unique_symptom_sets.index,np.array(['-1'])]))

		for idx,sset in inference_data_struct.unique_symptom_sets.items():
			obs_hpos=self.hpo_col_indexes[sset]
			unobs_hpos=inference_data_struct.hpo_column_labels.difference(obs_hpos)
			self.symptom_set_dirichlet_params.loc[idx]+=np.sum(self.posterior_info.loc[obs_hpos]['LogFreqPresent'])+np.sum(self.posterior_info.loc[unobs_hpos]['LogFreqAbsent'])
		self.symptom_set_dirichlet_params.loc['-1']+=self.posterior_info['LogFreqAbsent'].sum()

		norm_const=logsumexp(self.symptom_set_dirichlet_params.values*init_smoothing)
		self.symptom_set_dirichlet_params[self.symptom_set_dirichlet_params.index]=np.exp((self.symptom_set_dirichlet_params.values*init_smoothing+np.log(init_strength))-norm_const)


		#initialize optimizer
		self.prior_optimizer=DirichletPriorOptimizer(pd.Series(np.arange(self.hpo_col_indexes.shape[0]),index=self.hpo_col_indexes),self.symptom_sets,self.prior_info,self.posterior_info['SymptomFreq'],update_smoothing=update_smoothing,update_strength=update_strength,update_frequencies=update_frequencies,prior_for_piecewise=linked_frequency_prior_params,prior_for_std_beta=linked_frequency_prior_params,update_indicators=update_indicators,prior_for_unannoated=unlinked_frequency_prior_params,cut_points=piecewise_beta_cut_points,init_smoothing=init_smoothing,init_strength=init_strength,strength_penalty=strength_penalty)

	def UpdatePriorParams(self,new_set_counts,temperature,error_tol=1e-8,verbose=False):
		loss=self.prior_optimizer.Fit(new_set_counts,temperature,error_tol=error_tol,verbose=False,init_learning_rate=1.0)
		dirichlet_params_array,log_freq_present_array,log_freq_absent_array=self.prior_optimizer.ReturnModelParams()
		for i,set_idx in enumerate(self.prior_optimizer.set_index_to_arrays.keys()):
			self.symptom_set_dirichlet_params[set_idx]=dirichlet_params_array[i]

		for hpo in self.posterior_info.index:
			is_annot_freq=np.exp(self.prior_optimizer._compute_obs_prob(hpo).detach().numpy())
			self.posterior_info.loc[hpo,'SymptomFreq']=is_annot_freq
			self.posterior_info.loc[hpo,'LogFreqPresent']=log_freq_present_array[self.prior_optimizer.symptom_to_array_index[hpo]]
			self.posterior_info.loc[hpo,'LogFreqAbsent']=log_freq_absent_array[self.prior_optimizer.symptom_to_array_index[hpo]]
			self.posterior_info.loc[hpo,'IsAnnotProb']=self.prior_optimizer.prob_is_associated[hpo].detach().numpy()

		self.aux_params['Strength']=np.exp(self.prior_optimizer.log_strength_parameter.detach().numpy())
		self.aux_params['Smoothing']=expit(self.prior_optimizer.logit_smoothing_parameter.detach().numpy())
		self.aux_params['UnlinkedFrequency']=expit(self.prior_optimizer.unnannotated_log_odds.detach().numpy())
		return loss

	def ReturnLossComponents(self,set_counts,temperature):
		self.prior_optimizer._set_new_counts(set_counts)
		return self.prior_optimizer.ReturnLossComponents(temperature)

	


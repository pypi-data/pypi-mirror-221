import pandas as pd 
import numpy as np
from scipy import sparse
from scipy.special import gammaln,betaln,expit,digamma
import pickle
from sklearn.metrics import precision_recall_curve, average_precision_score

SMALL_FLOAT=np.finfo(np.float64).eps
MINLOG = np.log(SMALL_FLOAT)

class InferenceDataStruct:


	def __init__(self,sparse_data_array,patient_indices,hpo_columns,training_index,testing_index):
		self.patient_indices=patient_indices
		self.hpo_column_labels=hpo_columns
		self.training_index=training_index
		self.testing_index=testing_index
		
		symptom_counts=sparse_data_array.sum(axis=1)

		self.all_asymptomatic_cases=np.where(symptom_counts==0)[0]
		self.all_symptomatic_cases=np.where(symptom_counts>0)[0]

		self.all_asymptomatic_cases=pd.Series(self.all_asymptomatic_cases,index=self.patient_indices[self.all_asymptomatic_cases])
		self.all_symptomatic_cases=pd.Series(self.all_symptomatic_cases,index=self.patient_indices[self.all_symptomatic_cases])
		self.symptomatic_in_training=self.all_symptomatic_cases.index.intersection(self.training_index)
		self.asymptomatic_in_training=self.all_asymptomatic_cases.index.intersection(self.training_index)



		#Find all of the unique symptom sets and where they occur. 
		symptomatic_lil_array=sparse.lil_array(sparse_data_array[self.all_symptomatic_cases])
		unique_symptom_sets,array_of_unique_indices=np.unique(symptomatic_lil_array.rows,return_inverse=True)

		self.unique_symptom_sets=pd.Series(unique_symptom_sets,index=map(str,np.arange(len(unique_symptom_sets))))
		self.symptomatic_patients_to_unique_sets=pd.Series(map(str,array_of_unique_indices),index=self.all_symptomatic_cases.index)

		self.symptoms_to_unique_sets={}
		for u_id,symptom_array in self.unique_symptom_sets.items():
			for symp in symptom_array:
				try:
					self.symptoms_to_unique_sets[symp]+=[u_id]
				except KeyError:
					self.symptoms_to_unique_sets[symp]=[u_id]
		self.symptoms_to_unique_sets=pd.DataFrame({'S_ID':list(self.symptoms_to_unique_sets.keys()),'U_ID':list(self.symptoms_to_unique_sets.values())})
		self.symptoms_to_unique_sets.set_index('S_ID',inplace=True)

		self.unique_sets_to_patient_map={}
		for p_id,u_id in self.symptomatic_patients_to_unique_sets.items():
			try:
				self.unique_sets_to_patient_map[u_id]+=[p_id]
			except KeyError:
				self.unique_sets_to_patient_map[u_id]=[p_id]
		self.unique_sets_to_patient_map=pd.DataFrame({'U_ID':list(self.unique_sets_to_patient_map.keys()),'P_ID':list(self.unique_sets_to_patient_map.values())})
		self.unique_sets_to_patient_map.set_index('U_ID',inplace=True)

		self.unique_sets_to_patient_map_training_only={}
		for p_id,u_id in self.symptomatic_patients_to_unique_sets.loc[self.all_symptomatic_cases.index.intersection(self.training_index)].items():
			try:
				self.unique_sets_to_patient_map_training_only[u_id]+=[p_id]
			except KeyError:
				self.unique_sets_to_patient_map_training_only[u_id]=[p_id]
		self.unique_sets_to_patient_map_training_only=pd.DataFrame({'U_ID':list(self.unique_sets_to_patient_map_training_only.keys()),'P_ID':list(self.unique_sets_to_patient_map_training_only.values())})
		self.unique_sets_to_patient_map_training_only.set_index('U_ID',inplace=True)

		self.unique_sets_to_patient_map_testing_only={}
		for p_id,u_id in self.symptomatic_patients_to_unique_sets.loc[self.all_symptomatic_cases.index.intersection(self.testing_index)].items():
			try:
				self.unique_sets_to_patient_map_testing_only[u_id]+=[p_id]
			except KeyError:
				self.unique_sets_to_patient_map_testing_only[u_id]=[p_id]
		self.unique_sets_to_patient_map_testing_only=pd.DataFrame({'U_ID':list(self.unique_sets_to_patient_map_testing_only.keys()),'P_ID':list(self.unique_sets_to_patient_map_testing_only.values())})
		self.unique_sets_to_patient_map_testing_only.set_index('U_ID',inplace=True)

		self.num_unique_sets_total=self.unique_symptom_sets.shape[0]
		self.num_unique_sets_training=self.unique_sets_to_patient_map_training_only.shape[0]

	def _return_set_indepedent_likelihoods(self,log_prob_pos, log_prob_neg):
		likelihoods = pd.Series(np.zeros(self.unique_symptom_sets.shape[0]),index=self.unique_symptom_sets.index)
		for u_idx,symp_set in self.unique_symptom_sets.items():
			vec=np.zeros(self.hpo_column_labels.shape[0])
			vec[symp_set]=1
			likelihoods.loc[u_idx]=np.sum(log_prob_pos*vec)+np.sum(log_prob_neg*(1-vec))
		return likelihoods

	def _compute_counts(self,has_disease_inds):
		target_count_vec=pd.Series(np.zeros(self.num_unique_sets_total+1),index=np.concatenate([self.unique_symptom_sets.index,np.array(['-1'])]))

		if has_disease_inds.shape[1]==3:
			nuisance_count_vec=pd.Series(np.zeros(self.num_unique_sets_total),index=self.unique_symptom_sets.index)
		else:
			nuisance_count_vec=None
		independent_counts=np.zeros((self.hpo_column_labels.shape[0],2))

		for u_idx,p_id in self.unique_sets_to_patient_map_training_only.iterrows():
			target_count_vec.loc[u_idx]+=np.sum(has_disease_inds.loc[p_id.P_ID,'Target'])
			if nuisance_count_vec is not None:
				nuisance_count_vec.loc[u_idx]+=np.sum(has_disease_inds.loc[p_id.P_ID,'Nuisance'])
			independent_counts[self.unique_symptom_sets[u_idx],0]+=np.sum(has_disease_inds.loc[p_id.P_ID,'Independent'])

		target_count_vec.loc['-1']+=np.sum(has_disease_inds.loc[self.asymptomatic_in_training,'Target'])
		independent_counts[:,1]=has_disease_inds['Independent'].sum()-independent_counts[:,0]
		return target_count_vec,nuisance_count_vec,independent_counts


class PDSBase:
	def _beta_exp_log_x(self,alpha,beta):
		return digamma(alpha)-digamma(alpha+beta)

	def _beta_exp_log_1mx(self,alpha,beta):
		return digamma(beta)-digamma(alpha+beta)

	def _beta_entropy(self,alpha,beta):
		return betaln(alpha,beta)-(alpha-1.0)*digamma(alpha)-(beta-1.0)*digamma(beta)+(alpha+beta-2.0)*digamma(alpha+beta)

	def _dirichlet_entropy(self,pvec):
		return self._multivariate_log_beta(pvec)+(np.sum(pvec)-pvec.shape[0])*digamma(np.sum(pvec))-np.sum((pvec-1.0)*digamma(pvec))
	
	def _dirichlet_log_like(self,log_prob_vec,param_vec):
		prior_norm_const=self._multivariate_log_beta(param_vec)
		return np.sum((param_vec-1.0)*log_prob_vec)-prior_norm_const

	def _multivariate_log_beta(self,alpha_vec):
		return np.sum(gammaln(alpha_vec))-gammaln(np.sum(alpha_vec))

	def _dirichlet_exp_logx(self,count_vec):
		return digamma(count_vec)-digamma(np.sum(count_vec))

	def _dirichlet_marg_like(self,obs_vec,pvec):
		prior_norm_const=self._multivariate_log_beta(pvec)
		posterior_norm_const=np.sum(gammaln(pvec+obs_vec))-gammaln(np.sum(pvec+obs_vec))
		return posterior_norm_const-prior_norm_const




	def _removeZeros(self):
		counts=np.array(self.sparse_hpo_data_matrix.sum(axis=0)).ravel()
		missing_counts=np.where(counts==0)[0]
		obs_counts=np.where(counts>0)[0]
		if missing_counts.shape[0]>0:
			print('Warning: {0:d} symptoms have no observed diagnoses. Dropping from dataset. If you believe this is an error, please double check your matrix of diagnoses.'.format(missing_counts.shape[0]))
			self.sparse_hpo_data_matrix=self.sparse_hpo_data_matrix[:,obs_counts]
			self.hpo_term_columns=self.hpo_term_columns[obs_counts]
			self.hpo_to_array_map=pd.Series(np.arange(self.sparse_hpo_data_matrix.shape[1]),index=self.hpo_term_columns)

	def _build_inference_data_struct(self,hpo_terms):

		missing_terms=set(hpo_terms).difference(self.hpo_term_columns)
		if len(missing_terms)>0:
			print('Warning: {0:s} are not in the datset. Note: they may have been dropped because their frequency was too low.'.format(','.join(missing_terms)))
			hpo_terms=list(hpo_terms.intersection(self.hpo_term_columns))

		hpo_indices=pd.Series([self.hpo_to_array_map[x] for x in hpo_terms],index=hpo_terms)
		return InferenceDataStruct(self.sparse_hpo_data_matrix[:,hpo_indices],self.patient_indices,hpo_indices.index,self.training_index,self.testing_index)

	def __init__(self,patient_indices,hpo_term_columns,sparse_hpo_data_matrix):

		self.patient_indices=np.array(patient_indices)
		assert len(set(self.patient_indices))==self.patient_indices.shape[0],"Patient indices contain duplicate columns."
		self.hpo_term_columns=np.array(hpo_term_columns)
		assert len(set(self.hpo_term_columns))==self.hpo_term_columns.shape[0],"Symptom array columns contain duplicate HPO terms."
		self.sparse_hpo_data_matrix=sparse_hpo_data_matrix
		self.training_index=self.patient_indices
		self.testing_index=np.array([],dtype=self.training_index.dtype)

		self.patient_index_to_array_map=pd.Series(np.arange(sparse_hpo_data_matrix.shape[0]),index=self.patient_indices)
		self.hpo_to_array_map=pd.Series(np.arange(sparse_hpo_data_matrix.shape[1]),index=self.hpo_term_columns)

		#remove zeros
		self._removeZeros()

	def SetTrainingState(self,training_fraction):
		new_index_array=np.copy(self.patient_indices)
		np.random.shuffle(new_index_array)
		cutoff=int(np.floor(training_fraction*new_index_array.shape[0]))
		self.training_index=new_index_array[:cutoff]
		self.testing_index=new_index_array[cutoff:]

		counts=np.array(self.sparse_hpo_data_matrix[self.patient_index_to_array_map[self.training_index],:].sum(axis=0)).ravel()
		missing_counts=np.where(counts==0)[0]
		obs_counts=np.where(counts>0)[0]
		if missing_counts.shape[0]>0:
			print('Warning: {0:d} symptoms have no observed diagnoses in the training data. Consider increasing size of training dataset or dropping low-prevalence symptoms from the dataset.'.format(missing_counts.shape[0]))

	def DropLowFrequencySymptoms(self,min_freq):
		freqs=np.array(self.sparse_hpo_data_matrix.mean(axis=0)).ravel()
		dropped=np.where(freqs<min_freq)[0]
		allowed=np.where(freqs>=min_freq)[0]
		print('{0:d} symptoms with prevalence < {1:f}. Dropping from dataset.'.format(dropped.shape[0],min_freq))
		self.sparse_hpo_data_matrix=self.sparse_hpo_data_matrix[:,allowed]
		self.hpo_term_columns=self.hpo_term_columns[allowed]
		self.hpo_to_array_map=pd.Series(np.arange(self.sparse_hpo_data_matrix.shape[1]),index=self.hpo_term_columns)


	def PheRS(self,hpo_terms):
		missing_terms=set(hpo_terms).difference(self.hpo_term_columns)

		if len(missing_terms)>0:
			print('Warning: {0:s} are not in the datset. Note: they may have been dropped because their frequency was too low.'.format(','.join(missing_terms)))
			hpo_terms=list(hpo_terms.intersection(self.hpo_term_columns))

		hpo_indices=pd.Series([self.hpo_to_array_map[x] for x in hpo_terms],index=hpo_terms)

		assert np.sum(self.sparse_hpo_data_matrix[:,hpo_indices][self.patient_index_to_array_map[self.training_index],:].sum(axis=0)==0)==0,"There are symptoms with no observations in the training data. Please either increase training dataset size or drop low frequency symptoms."

		surprisals=-1.0*np.log(self.sparse_hpo_data_matrix[self.patient_index_to_array_map[self.training_index]].mean(axis=0))[hpo_indices]

		training_phers=self.sparse_hpo_data_matrix[self.patient_index_to_array_map[self.training_index]][:,hpo_indices].multiply(surprisals.reshape(1,-1)).sum(axis=1)

		if self.testing_index.shape[0]>0:
			testing_phers=self.sparse_hpo_data_matrix[self.patient_index_to_array_map[self.testing_index]][:,hpo_indices].multiply(surprisals.reshape(1,-1)).sum(axis=1)
		else:
			testing_phers=np.array([])
		return {'PheRS_Weights':pd.Series(surprisals,index=hpo_terms),'Training':pd.Series(training_phers,index=self.training_index),'Testing':pd.Series(testing_phers,index=self.testing_index)}

	def BasicPerformanceStats(self,labels,scores):
		assert isinstance(labels,pd.Series), "Expects labels to be a pd.Series with the index corresponding to the the patient indices."
		assert isinstance(scores,pd.Series), "Expects scores to be a pd.Series with the index corresponding to the the patient indices."
		training_avg_precision_score=average_precision_score(labels.loc[self.training_index],scores.loc[self.training_index])
		prec_training,recall_training,thresh=precision_recall_curve(labels.loc[self.training_index],scores.loc[self.training_index])


		if len(self.testing_index)>0:
			testing_avg_precision_score=average_precision_score(labels.loc[self.testing_index],scores.loc[self.testing_index])
			prec_testing,recall_testing,thresh=precision_recall_curve(labels.loc[self.testing_index],scores.loc[self.testing_index])
		else:
			testing_avg_precision_score=np.nan
			prec_testing=np.array([])
			recall_testing=np.array([])

		results=pd.DataFrame({'Precision':[prec_training,prec_testing],'Recall':[recall_training,recall_testing],'AvgPrecision':[training_avg_precision_score,testing_avg_precision_score]},index=['Training','Testing'])

		return results




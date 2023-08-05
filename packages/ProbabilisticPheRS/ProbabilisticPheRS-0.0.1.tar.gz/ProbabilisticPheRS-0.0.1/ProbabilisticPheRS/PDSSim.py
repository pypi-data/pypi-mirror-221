import pandas as pd 
import numpy as np
from scipy import sparse
from scipy.stats import beta as beta_dist
from scipy.stats import poisson
from PiecewiseBeta.PiecewiseBeta import PiecewiseBeta
from tqdm import tqdm
import pickle
from collections.abc import Iterable


class DiseaseCharacteristics:
	def __init__(self,prevalence,symptoms,frequencies):

		assert symptoms.shape[0]==frequencies.shape[0],'Symptoms and frequencies must be the same length.'
		self.prevalence=prevalence
		self.symptoms=symptoms
		self.frequencies=frequencies



class PDSSim:

	def _truncated_poisson_rvs(self,exp_val,max_val,num_samples):
		max_prob=poisson(exp_val).cdf(max_val)
		min_prob=poisson(exp_val).cdf(0)
		rv_ = np.random.uniform(low=min_prob,high=max_prob, size=num_samples)
		return poisson(exp_val).ppf(rv_)


	def _sample_freq_rates(self,hpo,freq_info):
		if isinstance(freq_info,tuple):
			assert len(freq_info)==2,"Frequency information for HPO {0:s} data type 'tuple' does not match expectations. Must have two entries.".format(hpo)
			assert freq_info[1]>=freq_info[0],"Frequency counts for HPO {0:s} are improper. Must be in (successes, total) format."
			# return beta_dist(self.linked_frequency_priors[0]+freq_info[0],self.linked_frequency_priors[1]+(freq_info[1]-freq_info[0])).rvs()
			return beta_dist(self.linked_frequency_priors[0]+freq_info[0],self.linked_frequency_priors[1]+(freq_info[1]-freq_info[0])).rvs()
		elif isinstance(freq_info,Iterable):
			freq_info=np.array(freq_info)
			assert len(freq_info)==(self.piecewise_beta.cut_points.shape[0]-1),"Frequency information for HPO {0:s} data type 'frequency classes' does not match expectations. Number of entries must match provided beta distribution cut points".format(hpo)
			return self.piecewise_beta.RandomVariates(freq_info,1)[0]
		else: 
			raise ValueError("Error in frequency informaton for HPO {0:s}. Frequency information must either be a tuple of length 2 or a vector of frequency classes.".format(hpo))


	def  __init__(self,hpo_info,linked_frequency_priors=[1.0,1.0],background_frequency_priors=[1,1000],contaminating_disease_prevalence_priors=[1,200],contaminating_disease_symptom_freq_priors=[2,2],symptom_frequency_cut_points=[0.0,0.04,0.3,0.8,0.99,1.0]):
		"""Summary
		
		Args:
		    target_annotation_rates (TYPE): Description
		    target_symptom_freqs (TYPE): Description
		    symptom_frequency_cut_points (list, optional): Description
		    beta_priors (list, optional): Description
		    background_beta_priors (list, optional): Description
		    contaminating_disease_prevalence_priors (list, optional): Description
		    contaminating_disease_exp_symptom_num (int, optional): Description
		"""
		self.hpo_to_index=pd.Series(np.arange(hpo_info.shape[0]),index=hpo_info.index)
		self.hpo_info=hpo_info
		self.background_frequency_priors=np.array(background_frequency_priors)
		self.linked_frequency_priors=np.array(linked_frequency_priors)
		self.piecewise_beta=PiecewiseBeta(symptom_frequency_cut_points,linked_frequency_priors[0],linked_frequency_priors[1])
		self.contaminating_disease_prevalence_priors=np.array(contaminating_disease_prevalence_priors)
		self.contaminating_disease_symptom_freq_priors=np.array(contaminating_disease_symptom_freq_priors)

	def GenerateDataset(self,num_samples,target_disease_prevelance,num_contaminating_diseases,contaminating_disease_exp_frac_overlap):
		"""Summary
		
		Args:
		    num_samples (TYPE): Description
		    target_disease_prevelance (TYPE): Description
		    num_contaminating_diseases (TYPE): Description
		    contaminated_disease_exp_overlap (TYPE): Description
		"""
		assert num_samples>0,"Must simulate at least 1 patent."
		assert (target_disease_prevelance>0.0) and (target_disease_prevelance<1.0),"Target disease prevelance must be between 0 and 1."
		assert isinstance(num_contaminating_diseases, int) and (num_contaminating_diseases>=0),"Target disease must be an integer from [0,infty)."
		assert (contaminating_disease_exp_frac_overlap>=0.0) and (contaminating_disease_exp_frac_overlap < 1.0),"Expected fraction of contaminating disease symptom overlap must be between 0.0 and 1."
		if (num_contaminating_diseases>0) and (contaminating_disease_exp_frac_overlap==0.0):
			raise ValueError("There is no point in specificying contaminating diseases with 0 symptom overlap. Just specify 0 contaminating diseases.")
		#background symptom frequencies
		background_frequencies=np.random.beta(*self.background_frequency_priors,self.hpo_info.shape[0])


	# 	#target disease information

		target_associated_symptoms=np.where(np.random.binomial(1,self.hpo_info[self.hpo_info.columns[0]])==1)[0]
		associated_symptom_info=self.hpo_info.iloc[target_associated_symptoms].copy()

		sampled_freqs=[]
		for hpo,freq_info in associated_symptom_info[associated_symptom_info.columns[1:]].iterrows():
			sampled_freqs+=[self._sample_freq_rates(hpo,freq_info.values[0])]
			
		associated_symptom_info['SAMPLES']=pd.Series(sampled_freqs,index=associated_symptom_info.index)
		target_disease=DiseaseCharacteristics(target_disease_prevelance,self.hpo_to_index[associated_symptom_info.index],associated_symptom_info['SAMPLES'].values)
		contaminating_diseases=[]
		for con_dis in range(1,num_contaminating_diseases+1):
			contaminating_disease_prevalence=np.random.beta(*self.contaminating_disease_prevalence_priors)
			contaminating_disease_symptom_num=int(self._truncated_poisson_rvs(contaminating_disease_exp_frac_overlap*associated_symptom_info.shape[0],associated_symptom_info.shape[0],1)[0])
			overlap_symptoms=np.random.choice(target_associated_symptoms,contaminating_disease_symptom_num,replace=False)
			contaminating_disease_symptom_frequencies=beta_dist(*self.contaminating_disease_symptom_freq_priors).rvs(contaminating_disease_symptom_num)
			contaminating_diseases+=[DiseaseCharacteristics(contaminating_disease_prevalence,overlap_symptoms,contaminating_disease_symptom_frequencies)]

		has_target_disease=np.random.binomial(1,target_disease.prevalence,num_samples)
		off_target_diseases=np.random.binomial(1,np.array([c.prevalence for c in contaminating_diseases]).reshape(-1,1),(num_contaminating_diseases,num_samples))

		sparse_symptom_matrix=sparse.dok_matrix((num_samples,self.hpo_info.shape[0]),dtype=float)

		for i in tqdm(range(num_samples)):
			base_freqs=np.log(1.0-background_frequencies)
			base_freqs[target_disease.symptoms]+=has_target_disease[i]*np.log(1.0-target_disease.frequencies)
			for j,c in enumerate(contaminating_diseases):
				base_freqs[c.symptoms]+=off_target_diseases[j,i]*np.log(1.0-c.frequencies)
			freqs=1.0-np.exp(base_freqs)
			symptoms=np.random.binomial(1,freqs)
			sparse_symptom_matrix[i]=symptoms
		return {'SparseSymptomMatrix':sparse.csr_array(sparse_symptom_matrix),'HasTargetDisease':has_target_disease,'TargetDiseaseParams':target_disease,'OffTargetDiseases':off_target_diseases,'OffTargetParams':contaminating_diseases}


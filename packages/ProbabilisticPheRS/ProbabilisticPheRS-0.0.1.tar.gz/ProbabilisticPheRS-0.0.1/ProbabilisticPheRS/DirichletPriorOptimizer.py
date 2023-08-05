import numpy as np
from scipy.special import logit as scipylogit
from PiecewiseBeta.PiecewiseBeta import PiecewiseBeta
import torch
from tensordict import TensorDict
from torchmin import Minimizer
from torch.special import gammaln as _tgammaln
from torch.special import digamma as _tdigamma
import copy

SMALL_FLOAT=torch.finfo(torch.float64).eps
MINLOG = np.log(torch.finfo(torch.float64).eps)


class _vb_dirichlet_map_loss(torch.nn.Module):

	def _multivariate_log_beta(self,alpha_tensor):
		return torch.sum(_tgammaln(alpha_tensor))-_tgammaln(torch.sum(alpha_tensor))

	def _dirichlet_exp_logx(self,p_tensor):
		return _tdigamma(p_tensor)-_tdigamma(torch.sum(p_tensor))

	def _dirichlet_log_like(self,log_prob_tensor,param_tensor):
		prior_norm_const=self._multivariate_log_beta(param_tensor)
		return torch.sum((param_tensor-1.0)*log_prob_tensor)-prior_norm_const

	def _dirichlet_entropy(self,ptensor):
		return self._multivariate_log_beta(ptensor)+(torch.sum(ptensor)-ptensor.shape[0])*_tdigamma(torch.sum(ptensor))-torch.sum((ptensor-1.0)*_tdigamma(ptensor))


	def _piecewise_beta_log_like(self,prob,weights):
		#note, log like is not normalized, which doesn't matter since norm const won't change with updates
		piece=torch.where(prob<=self.parent_inference_class.cut_points[1:])[0][0]
		return torch.log(prob)*(self.parent_inference_class.prior_for_piecewise[0]-1.0)+torch.log(1.0-prob)*(self.parent_inference_class.prior_for_piecewise[1]-1.0)+torch.log(weights[piece])

	def _std_beta_log_like(self,prob,a,b):
		return torch.log(prob)*(a-1.0)+torch.log(1.0-prob)*(b-1.0)

	def __init__(self,parent_inference_class):
		super(_vb_dirichlet_map_loss, self).__init__()
		self.parent_inference_class=parent_inference_class

	def _dirichlet_component(self,dirichlet_params):

		post_params=self.parent_inference_class.set_counts*self.parent_inference_class.current_temperature+dirichlet_params*self.parent_inference_class.current_temperature-self.parent_inference_class.current_temperature+1.0
		exp_log_vals=self._dirichlet_exp_logx(post_params)

		loss=torch.sum(exp_log_vals*self.parent_inference_class.set_counts)+self._dirichlet_log_like(exp_log_vals,dirichlet_params)+(1.0/self.parent_inference_class.current_temperature)*self._dirichlet_entropy(post_params)
		return loss

	def _prior_component(self,symptom_log_odds,unnannotated_log_odds,is_annot_post,log_strength,log_smoothing):
		loss=0.0
		for hpo in symptom_log_odds.keys():
			if self.parent_inference_class.is_piecewise[hpo]==False:
				loss+=self._std_beta_log_like(torch.nn.functional.sigmoid(symptom_log_odds[hpo]),self.parent_inference_class.symptom_prior_freq_info[hpo][0]+self.parent_inference_class.prior_for_std_beta[0],self.parent_inference_class.symptom_prior_freq_info[hpo][1]+self.parent_inference_class.prior_for_std_beta[1])
			else:
				if self.parent_inference_class.allowed_freq_range[hpo][0]==0.0:
					obs_prob=torch.exp(torch.nn.functional.logsigmoid(symptom_log_odds[hpo])+torch.log(self.parent_inference_class.allowed_freq_range[hpo][1]))
				else:
					obs_prob=torch.exp(torch.logaddexp(torch.nn.functional.logsigmoid(symptom_log_odds[hpo])+torch.log(self.parent_inference_class.allowed_freq_range[hpo][1]-self.parent_inference_class.allowed_freq_range[hpo][0]),torch.log(self.parent_inference_class.allowed_freq_range[hpo][0])))
				loss+=self._piecewise_beta_log_like(obs_prob,self.parent_inference_class.symptom_prior_freq_info[hpo])
			if self.parent_inference_class.symptom_annot_probs[hpo]<1.0:
				loss+=torch.log(self.parent_inference_class.symptom_annot_probs[hpo])*is_annot_post[hpo]+torch.log(1.0-self.parent_inference_class.symptom_annot_probs[hpo])*(1.0-is_annot_post[hpo])+(is_annot_post[hpo]*torch.log(is_annot_post[hpo])+(1.0-is_annot_post[hpo])*torch.log(1.0-is_annot_post[hpo]))

		loss+=self._std_beta_log_like(torch.nn.functional.sigmoid(unnannotated_log_odds),self.parent_inference_class.prior_for_unannoated[0],self.parent_inference_class.prior_for_unannoated[1])
		loss+=-1.0*(log_strength**2.0)*self.parent_inference_class.strength_penalty
		return loss

	def forward(self, dirichlet_params,symptom_log_odds,unnannotated_log_odds,is_annot_post,log_strength,log_smoothing):

		#model likelihood
		dirichlet_loss=self._dirichlet_component(dirichlet_params)
		prior_loss=self._prior_component(symptom_log_odds,unnannotated_log_odds,is_annot_post,log_strength,log_smoothing)
		return -1.0*(dirichlet_loss+prior_loss)


class DirichletPriorOptimizer(torch.nn.Module):


	def _beta_mode(self,a,b):
		return (a-1)/(a+b-2)

	def _check_beta_params(self,a,b):
		if (a<=1.0) or ((a+b)<2.0):
			return False
		else:
			return True


	def _multivariate_log_beta(self,alpha_tensor):
		return torch.sum(_tgammaln(alpha_tensor))-_tgammaln(torch.sum(alpha_tensor))

	def _dirichlet_exp_logx(self,p_tensor):
		return _tdigamma(p_tensor)-_tdigamma(torch.sum(p_tensor))

	def _dirichlet_log_like(self,log_prob_tensor,param_tensor):
		prior_norm_const=self._multivariate_log_beta(param_tensor)
		return torch.sum((param_vec-1.0)*log_prob_tensor)-prior_norm_const

	def _dirichlet_entropy(self,ptensor):
		return self._multivariate_log_beta(ptensor)+(torch.sum(ptensor)-ptensor.shape[0])*_tdigamma(torch.sum(pvec))-torch.sum((_tgammaln-1.0)*_tdigamma(_tgammaln))


	def _piecewise_beta_log_like(self,prob,weights):
		#note, log like is not normalized, which doesn't matter since norm const won't change with updates
		piece=torch.where(prob<=self.cut_points[1:])[0][0]
		return torch.log(prob)*(self.prior_for_piecewise[0]-1.0)+torch.log(1.0-prob)*(self.prior_for_piecewise[1]-1.0)+torch.log(weights[piece])

	def _std_beta_log_like(self,prob,a,b):
		return torch.log(prob)*(a-1.0)+torch.log(1.0-prob)*(b-1.0)

	def __init__(self,symptom_to_array_index,set_index_to_arrays,prior_info,init_frequencies,update_smoothing=True,update_strength=True, update_frequencies=True, update_indicators=True, prior_for_piecewise=[1.5,1.5],prior_for_std_beta=[1.5,1.5],prior_for_unannoated=[10.0,1000.0],cut_points=[0.0,0.04,0.3,0.8,0.99,1.0],init_smoothing=0.999999,init_strength=1.0,strength_penalty=0.1):
		super(DirichletPriorOptimizer,self).__init__()


		self.symptom_to_array_index={}
		for symptom,idx in symptom_to_array_index.items():
			self.symptom_to_array_index[symptom]=idx

		self.array_index_to_symptom={}
		for symptom,idx in symptom_to_array_index.items():
			self.array_index_to_symptom[idx]=symptom

		self.current_temperature=1.0
		
		self.symptom_log_odds=torch.nn.ParameterDict({x:torch.tensor(0.0,requires_grad=True) for x in self.symptom_to_array_index.keys()})
		self.unnannotated_log_odds=torch.nn.Parameter(torch.tensor(0.0,requires_grad=True))
		if update_frequencies==False:
			for key in self.symptom_log_odds.keys():
				self.symptom_log_odds[key].requires_grad_(False)

		if update_smoothing:
			self.logit_smoothing_parameter=torch.nn.Parameter(torch.tensor(scipylogit(init_smoothing),requires_grad=True))
		else:
			self.logit_smoothing_parameter=torch.tensor(scipylogit(init_smoothing),dtype=torch.float64,requires_grad=False)

		if update_strength:
			self.log_strength_parameter=torch.nn.Parameter(torch.tensor(np.log(init_strength),requires_grad=True))
		else:
			self.log_strength_parameter=torch.tensor(np.log(init_strength),dtype=torch.float64,requires_grad=False)

		self.update_indicators=update_indicators

		self.set_index_to_arrays={}
		for set_idx,array_inds in set_index_to_arrays.items():
			self.set_index_to_arrays[set_idx]=array_inds


		self.set_counts=torch.zeros(len(set_index_to_arrays),dtype=torch.float64,requires_grad=False)

		self.symptom_annot_probs=TensorDict({},batch_size=[])
		for hpo,annot_rate in prior_info['AnnotPrior'].items():
			self.symptom_annot_probs[hpo]=torch.tensor(annot_rate,dtype=torch.float64,requires_grad=False)

		self.is_piecewise=TensorDict({},batch_size=[])
		for hpo,is_p in prior_info['IsPiecewise'].items():
			self.is_piecewise[hpo]=torch.tensor(is_p,dtype=torch.bool,requires_grad=False)

		self.symptom_prior_freq_info=TensorDict({},batch_size=[])
		for hpo,freq_info in prior_info['FreqPrior'].items():
			self.symptom_prior_freq_info[hpo]=torch.tensor(freq_info,dtype=torch.float64,requires_grad=False)

		self.prob_is_associated=TensorDict({},batch_size=[])
		for hpo in self.symptom_annot_probs.keys():
			self.prob_is_associated[hpo]=self.symptom_annot_probs[hpo].clone().detach().requires_grad_(False)


		self.prior_for_piecewise=torch.tensor(prior_for_piecewise,requires_grad=False)
		if self._check_beta_params(self.prior_for_piecewise[0],self.prior_for_piecewise[1])==False:
			raise ValueError("Prior parameters for piecewise distribution has an undefined mode. MAP inference is likely to fail.")

		self.prior_for_unannoated=torch.tensor(prior_for_unannoated,requires_grad=False)
		if self._check_beta_params(self.prior_for_unannoated[0],self.prior_for_unannoated[1])==False:
			raise ValueError("Prior parameters for unannotated symptoms has an undefined mode. MAP inference is likely to fail.")

		self.prior_for_std_beta=torch.tensor(prior_for_std_beta,requires_grad=False)
		if self._check_beta_params(self.prior_for_std_beta[0],self.prior_for_std_beta[1])==False:
			raise ValueError("Prior parameters for standary beta has an undefined mode. MAP inference is could fail.")

		self.strength_penalty=torch.tensor(strength_penalty,dtype=torch.float64,requires_grad=False)

		self.cut_points=torch.tensor(cut_points,requires_grad=False)


		self.allowed_freq_range=TensorDict({},batch_size=[])
		for hpo in self.is_piecewise.keys():
			if self.is_piecewise[hpo]==False:
				self.allowed_freq_range[hpo]=torch.tensor([0.0,1.0],dtype=torch.float64,requires_grad=False)
			else:
				where_nonzero=torch.where(self.symptom_prior_freq_info[hpo]>0.0)[0]
				if where_nonzero.shape[0]==1:
					self.allowed_freq_range[hpo]=torch.tensor([self.cut_points[where_nonzero[0]],self.cut_points[where_nonzero[0]+1]],dtype=torch.float64,requires_grad=False)
				elif where_nonzero.shape[0]==(self.cut_points.shape[0]-1):
					self.allowed_freq_range[hpo]=torch.tensor([0.0,1.0],dtype=torch.float64,requires_grad=False)
				else:
					raise ValueError('Prior frequency information provided for {0:s} does not follow recognizable pattern. Should either have probability mass assigned to each segment or mass assigned to only 1 segment. Other possibilities are not allowed.')

		# initialize the parameters
		with torch.no_grad():
			self.unnannotated_log_odds.copy_(torch.logit(self.prior_for_unannoated[0]/self.prior_for_unannoated.sum()))
			for hpo in self.symptom_log_odds.keys():
				self.symptom_log_odds[hpo].copy_(torch.logit((torch.tensor(init_frequencies.loc[hpo],dtype=torch.float64)-self.allowed_freq_range[hpo][0])/(self.allowed_freq_range[hpo][1]-self.allowed_freq_range[hpo][0])))


	def _set_new_counts(self, count_series):
		for i,set_idx in enumerate(self.set_index_to_arrays.keys()):
			self.set_counts[i]=count_series[set_idx]

	def _build_dirichlet_params(self,log_freq_present_tensor,log_freq_absent_tensor):
		dirichlet_params=torch.zeros(self.set_counts.shape[0],dtype=torch.float64,requires_grad=False)
		for i,set_idx in enumerate(self.set_index_to_arrays.keys()):
			obs_hpos=list(self.set_index_to_arrays[set_idx])
			unobs_hpos=list(set(self.symptom_to_array_index.values()).difference(obs_hpos))
			dirichlet_params[i]=torch.sum(log_freq_present_tensor[obs_hpos])+torch.sum(log_freq_absent_tensor[unobs_hpos])

		#now normalize the probabilities, including the smoothing parameter
		norm_const=torch.logsumexp(torch.nn.functional.sigmoid(self.logit_smoothing_parameter)*dirichlet_params,dim=0)
		dirichlet_params=torch.exp(dirichlet_params*torch.nn.functional.sigmoid(self.logit_smoothing_parameter)-norm_const)*torch.exp(self.log_strength_parameter)
		return dirichlet_params

	def _compute_obs_prob(self,hpo):
		if self.is_piecewise[hpo]==False:
			obs_prob=torch.nn.functional.logsigmoid(self.symptom_log_odds[hpo])
		else:
			if self.allowed_freq_range[hpo][0]==0.0:
				obs_prob=torch.nn.functional.logsigmoid(self.symptom_log_odds[hpo])+torch.log(self.allowed_freq_range[hpo][1])
			else:
				obs_prob=torch.logaddexp(torch.nn.functional.logsigmoid(self.symptom_log_odds[hpo])+torch.log(self.allowed_freq_range[hpo][1]-self.allowed_freq_range[hpo][0]),torch.log(self.allowed_freq_range[hpo][0]))
		return obs_prob

	def forward(self):
		#first compute the log probability that each symptom occurs in the disease
		log_freq_present_tensor=torch.zeros(len(self.symptom_to_array_index),dtype=torch.float64,requires_grad=False)
		log_freq_absent_tensor=torch.zeros(len(self.symptom_to_array_index),dtype=torch.float64,requires_grad=False)

		for hpo,idx in self.symptom_to_array_index.items():
			obs_prob=self._compute_obs_prob(hpo)
			
			if (self.symptom_annot_probs[hpo]<1.0):
				log_freq_present_tensor[idx]=self.prob_is_associated[hpo]*obs_prob+(1.0-self.prob_is_associated[hpo])*torch.nn.functional.logsigmoid(self.unnannotated_log_odds)
				log_freq_absent_tensor[idx]=self.prob_is_associated[hpo]*torch.log(-1.0*torch.expm1(obs_prob))+(1.0-self.prob_is_associated[hpo])*torch.log(-1.0*torch.expm1(torch.nn.functional.logsigmoid(self.unnannotated_log_odds)))
			else:
				log_freq_present_tensor[idx]=obs_prob
				log_freq_absent_tensor[idx]=torch.log(-1.0*torch.expm1(obs_prob))

		dirichlet_params=self._build_dirichlet_params(log_freq_present_tensor,log_freq_absent_tensor)


		return dirichlet_params,log_freq_present_tensor,log_freq_absent_tensor



	def _update_single_assoc_prob(self,current_hpo,log_freq_present_tensor,log_freq_absent_tensor,loss_func):
		with torch.no_grad():
			is_annot_obs_prob=self._compute_obs_prob(current_hpo)

			unannot_obs_prob=torch.nn.functional.logsigmoid(self.unnannotated_log_odds)
			
			is_annot_unobs_prob=torch.log(-1.0*torch.expm1(is_annot_obs_prob))
			unannot_unobs_prob=torch.log(-1.0*torch.expm1(unannot_obs_prob))

			
			# first the annot prob
			log_freq_present_tensor[self.symptom_to_array_index[current_hpo]]=is_annot_obs_prob
			log_freq_absent_tensor[self.symptom_to_array_index[current_hpo]]=is_annot_unobs_prob
			dirichlet_params=self._build_dirichlet_params(log_freq_present_tensor,log_freq_absent_tensor)
			tmp_prob_is_annot=loss_func._dirichlet_component(dirichlet_params)

			# now the un-annot prob
			log_freq_present_tensor[self.symptom_to_array_index[current_hpo]]=unannot_obs_prob
			log_freq_absent_tensor[self.symptom_to_array_index[current_hpo]]=unannot_unobs_prob
			dirichlet_params=self._build_dirichlet_params(log_freq_present_tensor,log_freq_absent_tensor)
			tmp_prob_unaannot=loss_func._dirichlet_component(dirichlet_params)

			#compute new prob is associated
			full_loss=torch.logaddexp(torch.log(self.symptom_annot_probs[current_hpo])+tmp_prob_is_annot,torch.log(1.0-self.symptom_annot_probs[current_hpo])+tmp_prob_unaannot)
			self.prob_is_associated[current_hpo]=torch.exp((torch.log(self.symptom_annot_probs[current_hpo])+tmp_prob_is_annot)-full_loss)

			if self.prob_is_associated[current_hpo]==0.0:
				self.prob_is_associated[current_hpo]=torch.tensor(SMALL_FLOAT,dtype=torch.float64,requires_grad=False)
			elif self.prob_is_associated[current_hpo]==1.0:
				self.prob_is_associated[current_hpo]=torch.tensor(1.0-SMALL_FLOAT,dtype=torch.float64,requires_grad=False)



	def Fit(self,set_counts,temperature,error_tol=1e-6,verbose=False,max_iter=50,max_num_failures=5,init_learning_rate=0.1):
		self._set_new_counts(set_counts)
		self.current_temperature=temperature
		criterion = _vb_dirichlet_map_loss(self)
		num_failures=0

		def closure():
			optimizer.zero_grad()
			dirichlet_params,log_freq_present_tensor, log_freq_absent_tensor=self.forward()
			loss = criterion(dirichlet_params,self.symptom_log_odds,self.unnannotated_log_odds,self.prob_is_associated,self.log_strength_parameter,self.logit_smoothing_parameter)
			return loss 

		with torch.no_grad():
			init_params=self.forward()
			prev_loss=-1.0*criterion.forward(init_params[0],self.symptom_log_odds,self.unnannotated_log_odds,self.prob_is_associated,self.log_strength_parameter,self.logit_smoothing_parameter).item()


			if verbose:
				print("Dirichlet Symptom Model Initial Loss: {0:.6f}".format(prev_loss))

		previous_state=copy.deepcopy(self.state_dict())
		optimizer = Minimizer(self.parameters(),method='l-bfgs',max_iter=200,disp=False,options={'lr':init_learning_rate*(0.5**num_failures)})

		for i in range(1,max_iter+1):
			loss=optimizer.step(closure)
			with torch.no_grad():
				new_dirchlet_params,log_freq_present_tensor,log_freq_absent_tensor=self.forward()
				for hpo in self.prob_is_associated.keys():
					if (self.symptom_annot_probs[hpo]<1.0) and (self.update_indicators==True):
						self._update_single_assoc_prob(hpo,log_freq_present_tensor,log_freq_absent_tensor,criterion) 
						new_dirchlet_params,log_freq_present_tensor,log_freq_absent_tensor=self.forward()
			new_loss=-1.0*criterion.forward(new_dirchlet_params,self.symptom_log_odds,self.unnannotated_log_odds,self.prob_is_associated,self.log_strength_parameter,self.logit_smoothing_parameter).item()

			if new_loss<prev_loss:
				# load the previous state and try with a smaller learning rate
				num_failures+=1
				if num_failures>max_num_failures:
					self.load_state_dict(previous_state)
					new_loss=prev_loss
					if verbose:
						print('Maximum number of failures acheived. Final Loss: {1:.2f}'.format(i,new_loss))
					break
				else:
					if verbose:
						print('Unable to find optimum using current learning rate at iteration {0:d}. Loading previous model and decreasing learning rate to {1:f}'.format(i,init_learning_rate*(0.5**num_failures)))
					optimizer = Minimizer(self.parameters(),method='l-bfgs',max_iter=200,disp=False,options={'lr':init_learning_rate*(0.5**num_failures)})
					self.load_state_dict(previous_state)
			else:
				error=(new_loss-prev_loss)/np.abs(new_loss)

				if error<error_tol:
					if verbose:
						print('Dirichlet Symptom Model converged after {0:d} iterations. Final Loss: {1:.2f}'.format(i,new_loss))
					break
				else:
					previous_state=copy.deepcopy(self.state_dict())
					if verbose:
						print('Completed {0:d} iterations. Current Loss: {1:.2f}'.format(i,new_loss))
					prev_loss=new_loss
		if i==max_iter:
			print('Warning: Dirichlet Symptom Model did not converge after {0:d} iterations. The quality of the results is uncertain.'.format(max_iter))
		return new_loss

	def ReturnModelParams(self):
		with torch.no_grad():
			new_dirichlet_params,log_freq_present_tensor,log_freq_absent_tensor=self.forward()
		return new_dirichlet_params.detach().numpy(),log_freq_present_tensor.detach().numpy(),log_freq_absent_tensor.detach().numpy()

	def ReturnLossComponents(self,temperature):
		self.current_temperature=temperature
		criterion = _vb_dirichlet_map_loss(self)
		with torch.no_grad():
			dirichlet_params,log_freq_present_tensor,log_freq_absent_tensor=self.forward()
			dirichlet_loss=criterion._dirichlet_component(dirichlet_params)
			prior_loss=criterion._prior_component(self.symptom_log_odds,self.unnannotated_log_odds,self.prob_is_associated,self.log_strength_parameter,self.logit_smoothing_parameter)
		return dirichlet_loss.detach().numpy(),prior_loss.detach().numpy(),dirichlet_loss.detach().numpy()+prior_loss.detach().numpy()


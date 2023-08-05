import csv
import os 
import copy
import torch
from multiprocessing import Pool
import time
import collections
import random
import matplotlib.pyplot as plt 
import numpy as np
from ConfigSpace.configuration_space import Configuration
import ConfigSpace.util as csu
from HPO.utils.visualisation import plot_scores
from HPO.algorithms.algorithm_utils import train_eval 
###Tounament Selection/Aging Selection
  #
  #parameters:
  # S : (int) number of solutions to sample at each iteration
  # P : population size
  # C : Total cycles of evolution 
  # parent : highest-accuracy model in sample
  # history : Record of all models
  # population : Currently active models


# IDEAS
#
# - Run aging evolution for "species" with 1 species per core allowing cross-over occationally
#g
#
#
#
#
#

def F1(acc,rec):
    b = 1
    return (1+b**2)+ ((acc*rec)/(((b**2)*(acc**-1))+(rec**-1)))

class Model:
  MUTATE_RATE = 0.2
  def __init__(self, cs):
    self._arch = None
    self.accuracy = None
    self.cs = cs
    self.recall = None
    self.accuracy_vals = []
    self.recall_vals = []

  def get_distributions(self):
    self.mu_acc = np.mean(self.accuracy_vals)
    self.sd_acc = np.std(self.accuracy_vals)
    self.mu_rec = np.mean(self.recall_vals)
    self.sd_rec = np.std(self.recall_vals)
    self.cov = np.cov([self.mu_acc,self.mu_rec])

  def sample_joint(self):
    return np.random.multivariate_normal([self.mu_acc,self.mu_rec],self.cov)

  def sample_acc(self):
    return np.random.normal(self.mu,self.sd)
  def set_arch(self, arch):
    self._arch = arch
  def exchange_one( self , key : str ):
    new_hp = self.cs.sample_configuration().get_dictionary()[key]
    
    self._arch[key] = new_hp
  
  def __repr__(self):
    return "Model(Accuracy: {} , Recall: {})".format(self.accuracy,self.recall)
  def perturb(self, key : str):
    value_not_valid = True
    value_type = self.fix_type(key)
    while value_not_valid:
      try:
        self._arch[key] = self._arch[key] + value_type(self._arch[key]*random.uniform(0,Model.MUTATE_RATE)*random.choice([-1,1]))
      except ValueError:
        value_not_valid = True
      else:
        value_not_valid = False

  def fix_type(self,key):
    hp = str(self.cs[key])
    if "Integer" in hp:
      return round
    if "Float" in hp:
      return float
    else:
      return str


  def set_value(self, name, value):
    self._arch[name] = value
  def get_params(self):
    return list(self.arch().keys())
  def arch(self):
    return self._arch

def train_and_eval_population(worker, population, sample_batch, train):
  configs = []
  for model in population:
    if model.accuracy == None:
      configs.append(model.arch())
  results, _config = train.eval( configs )
  for mod,result in zip(population, results):
    mod.accuracy_vals = result["accuracy"]
    mod.recall_vals = result["recall"]
def model_change(parent, child):
  p_dict , c_dict = parent.arch().get_dictionary(), child.arch().get_dictionary()
  for _,i in zip(p_dict, c_dict):
    if p_dict[i] != c_dict[i]:
      print("Mutated {} from {} to {}".format(i, p_dict[i], c_dict[i]))
      return True
  print("WARNING: no change found!!!")
  return False



def Mutate(cs, parent_model : Model) -> Model:
  model = copy.deepcopy(parent_model) 
  model.accuracy = None
    
  def op_mutation(model: Model) -> Model:
    operation = ""
    while "node" not in operation:
      operation = random.choice(model.arch().keys())
    model.exchange_one(operation)
    return model
  

  def cont_mutation( model : Model):
    operation = ""
    while ("node" in operation) or ("index" in operation) or operation == "": 
      operation = random.choice(model.arch().keys())
    model.perturb(operation)
    return model
    
    
     
  def hidden_state_mutation(model : Model) -> Model:
    operation = ""
    while "index" not in operation:
      operation = random.choice(model.arch().keys())
    model.exchange_one(operation)
    return model
    

  while not model_change(parent_model, model):
    model = random.choice([op_mutation, hidden_state_mutation])(model)    
  return model 


"""
def Mutate(cs, parent_model : Model) -> Model:
  model = copy.deepcopy(parent_model) 
  model.set_arch(csu.get_random_neighbor(model._arch, random.randint(1,999)))
  model_change(parent_model,model)
  return model
"""
def load_csv(file , cs):
  population = []
  history = []
  with open(file, "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      acc = float(row[0])
      rec = float(row[1])
      arch = eval(row[2])
      model = Model(cs)
      model.set_arch(Configuration(cs,arch))
      model.accuracy = acc
      model.recall = rec
      population.append(model)
      history.append(model)
  return population, history
def regularized_evolution(configspace, worker , cycles, population_size, sample_size, sample_batch_size, load_file = None,load = False):
  """Algorithm for regularized evolution (i.e. aging evolution).

  Follows "Algorithm 1" in Real et al. "Regularized Evolution for Image
  Classifier Architecture Search".

  Args:
  cycles: the number of cycles the algorithm should run for.
  population_size: the number of individuals to keep in the population.
  sample_size: the number of individuals that should participate in each
      tournament.
  sample_batch_size: Number of children to generate before evaluating and adding to population
  Returns:
  history: a list of `Model` instances, representing all the models computed
      during the evolution experiment.
  """
  population = []
  history = []  # Not used by the algorithm, only used to report results.

  CS = configspace
  # Initialize the population with random models.
  if load_file ==None:
    train = train_eval( worker, sample_batch_size, "RegEvo.csv")
  elif not os.path.exists(load_file) or load == False:
    train = train_eval( worker, sample_batch_size, load_file)
  else:
    population , history = load_csv(load_file, CS)
    train = train_eval( worker, sample_batch_size, load_file )
    a = []
    r = []
    c= []
    for model in history:
      a.append(model.accuracy)
      r.append(model.recall)
      c.append(model.arch().get_dictionary())
    train.resume(a,r,c)
    if len(population) > population_size:
      population = population[-population_size:]
    for i in population:
      print(repr(i))
  while len(population) < population_size:
    model = Model( CS )
    model.set_arch( CS.sample_configuration() )
    population.append(model)
    history.append(model)
  train_and_eval_population(worker, population, sample_batch_size, train )
  # Carry out evolution in cycles. Each cycle produces a model and removes
  # another.
  children = []
  print_counter = 0
  while len(history) < cycles:

    print("Starting cycle", len(history) - population_size)
    # Sample randomly chosen models from the current population.

    if len(children) < sample_batch_size:
      sample = []
      while len(sample) < sample_size:
        # Inefficient, but written this way for clarity. In the case of neural
        # nets, the efficiency of this line is irrelevant because training neural
        # nets is the rate-determining step.
        candidate = random.choice(list(population))
        sample.append(candidate)

      # The parent is the best model in the sample.
      print("Selecting Parent via F1 Score")
      parent = max(sample, key=lambda i: F1(i.accuracy,i.recall))
      print("Scores of Parent F1: {} -- Acc: {} -- Recall: {}".format(F1(parent.accuracy,parent.recall),parent.accuracy,parent.recall))
      #parent = max(sample, key=lambda i: i.accuracy)

      # Create the child model and store it.
      child = Mutate(CS,parent)
      children.append(child)

    else:
      train_and_eval_population(worker, children, sample_batch_size, train)
      for i in children:
        population.append(i)
        history.append(i)
        population.pop(0)
      children = []
      # Remove the oldest model.
      best = max(population, key=lambda i: i.accuracy)
      print("--Current best model--")
      print("Accuracy:{} -- Recall: {} ".format(best.accuracy,best.recall))
      print("Architecture: ", best.arch())
      print("Population Size: ", len(population))
      print("Total Evaluations: ", len(history))
      print_counter +=1
      print_counter = 0
      accuracy_scores = []
      for i in history:
        accuracy_scores.append(i.accuracy)

      plot_scores(accuracy_scores)
  return history


def main(worker, configspace, load_file = "reg_evo.csv"):
  N = 5 #N best models to return
  pop_size = 100
  evaluations = 2500
  history = regularized_evolution(configspace, worker, cycles = evaluations, population_size =  pop_size, sample_size =8, sample_batch_size = 8, load_file = load_file)
  Architectures = []
  accuracy_scores = []
  recall_scores = []
  generations = list(range(evaluations))
  for i in history:
    accuracy_scores.append(i.accuracy)
    Architectures.append(i.arch)
    recall_scores.append(i.recall)
  top_acc = []
  top_rec = []
  top_config = []

  for i in range(N):
    indexs = accuracy_scores.index(max(accuracy_scores))
    print("Best accuracy: ", accuracy_scores[indexs])
    print("Best Hyperparameters: ", Architectures[indexs]())
    acc , rec , config = accuracy_scores[indexs] , recall_scores[indexs], Architectures[indexs]()
    top_acc.append(acc)
    top_rec.append(rec)
    top_config.append(config.get_dictionary())
    accuracy_scores.remove(max(accuracy_scores))
  return top_config,top_acc , top_rec

if __name__ == '__main__':
  main()

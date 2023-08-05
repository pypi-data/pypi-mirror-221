import csv
import copy
import torch
from multiprocessing import Pool
import time
import collections
import random
import matplotlib.pyplot as plt 
import numpy as np
from utils.visualisation import plot_scores
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



class Model:
  def __init__(self):
    self._arch = None
    self.accuracy = 0

  def set_arch(self, arch):
    self._arch = arch
  
  def set_value(self, name, value):
    self._arch[name] = value
  def get_params(self):
    return list(self.arch().keys())
  def arch(self):
    return self._arch.get_dictionary()

from nasbench301.representations import convert_genotype_to_config
def train_and_eval_population(worker, population, sample_batch, train = None, test= None):

  configs = []
  for model in population:
    configs.append(model.arch())
  
  if sample_batch == 1:
    results = []
    for i in configs:
      results.append(worker.compute(i))
  else:
    with Pool(processes = sample_batch) as pool:
        results = pool.map(worker.compute, configs)
        pool.close()
        torch.cuda.empty_cache()
        pool.join()

  for mod,result in zip(population,results):
    mod.accuracy = result

def nb301_mutate(cs,parent_model):

  model = copy.deepcopy(parent_model) 
  while True:
    op_key = random.choice(model.get_params())
    if "edge" in op_key or "input_node" in op_key:
        
      old_op = model.arch()[op_key]
      operations = cs.get_hyperparameter(op_key).choices
      while model.arch()[op_key] == old_op:  
        model.set_value(op_key,  random.choice(operations)  )
  
      return model

def Mutate(cs, parent_model : Model) -> Model:
  
  return nb301_mutate(cs,parent_model)



def regularized_evolution(configspace, worker , cycles, population_size, sample_size, sample_batch_size):
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
  while len(population) < population_size:
    model = Model()
    model.set_arch( CS.sample_configuration() )
    population.append(model)
    history.append(model)

  train_and_eval_population(worker, population, sample_batch_size)

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
      parent = max(sample, key=lambda i: i.accuracy)

      # Create the child model and store it.
      child = Model()
      child = Mutate(CS,parent)
      children.append(child)

    else:
      train_and_eval_population(worker, children, sample_batch_size)
      for i in children:
        population.append(i)
        history.append(i)
        population.pop(0)
      children = []
      # Remove the oldest model.
      best = max(population, key=lambda i: i.accuracy)
      print("--Current best model--")
      print("Accuracy: ",best.accuracy)
      #print("Architecture: ", best.arch())
      print("Population Size: ", len(population))
      print("Total Evaluations: ", len(history))
      print_counter +=1
      print_counter = 0
      accuracy_scores = []
      for i in history:
        accuracy_scores.append(i.accuracy)

      with open("RegEvo.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        for i in history:
          writer.writerow([i.accuracy,i.arch()]) 
      plot_scores(accuracy_scores)
  return history


def main(worker, configspace):
  pop_size = 20
  evaluations = 500
  history = regularized_evolution(configspace, worker, cycles = evaluations, population_size =  pop_size, sample_size = 10, sample_batch_size = 1)
  Architectures = []
  accuracy_scores = []
  generations = list(range(evaluations))
  for i in history:
    accuracy_scores.append(i.accuracy)
    Architectures.append(i.arch)
  
  plt.scatter(generations[:pop_size],accuracy_scores[:pop_size], c = "red")
  plt.scatter(generations[pop_size:],accuracy_scores[pop_size:])
  plt.title("Accuracy Scores of Configurations")
  plt.xlabel("Generation")
  plt.ylabel("Accuracy")
  plt.grid()
  plt.savefig("regevo.png",dpi = 1200)

  indexs = accuracy_scores.index(max(accuracy_scores))
  print("Best accuracy: ", accuracy_scores[indexs])
  print("Best Hyperparameters: ", Architectures[indexs]())
  print("True Validation Score: ",worker.validate(Architectures[indexs]()))




if __name__ == '__main__':
  main()

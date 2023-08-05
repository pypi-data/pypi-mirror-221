from HPO.utils.visualisation import plot_scores
import csv
from ConfigSpace import ConfigurationSpace
from HPO.algorithms.algorithm_utils import train_eval
import json
def main(worker, configspace : ConfigurationSpace, json_config):
  with open(json_config) as f:
    SETTINGS = json.load(f)["SEARCH_CONFIG"]
    
  train = train_eval( worker , json_config)
  configs = configspace.sample_configuration(SETTINGS["TOTAL_EVALUATIONS"] - train.ID_INIT)
  scores ,recall , pop= train.eval(configs)
  #print("Best Score: ", max(scores))      
  #plot_scores(scores)
  
  best_score = max(scores)
  best_config = pop[scores.index(max(scores))]
  best_rec = recall[scores.index(max(scores))]
 

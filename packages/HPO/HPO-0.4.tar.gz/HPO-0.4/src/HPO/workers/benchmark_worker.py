import json
from HPO.utils.model_graph import ModelGraph
from HPO.searchspaces.graph_search_space import GraphConfigSpace
import numpy as np 
from HPO.data.UEA_datasets import UEA_Train, UEA_Test, UEA_Full
import time
import sys
from HPO.utils.utils import MetricLogger
import os 
from HPO.utils.benchmark_models import InceptionTime, MultiResAtt
import matplotlib.pyplot as plt
from HPO.utils.model import NetworkMain
from HPO.utils.DARTS_utils import config_space_2_DARTS
from HPO.utils.FCN import FCN 
import pandas as pd
import torch
from sklearn.model_selection import GroupKFold
from HPO.data.teps_datasets import Train_TEPS , Test_TEPS
import torch.nn as nn
from torch import Tensor
from torch.utils.data import DataLoader, SubsetRandomSampler
from torchsummary import summary
import random
import HPO.utils.augmentation as aug
from HPO.utils.train_utils import collate_fn_padd,BalancedBatchSampler
from HPO.utils.train import train_model
from HPO.utils.weight_freezing import freeze_FCN, freeze_resnet
from HPO.utils.ResNet1d import resnet18
from HPO.utils.files import save_obj
from queue import Empty
from sklearn.model_selection import StratifiedKFold as KFold
from collections import namedtuple
from HPO.utils.worker_score import Evaluator 
from HPO.utils.worker_utils import LivePlot
from HPO.workers.worker_wrapper import __compute
from HPO.data.dataset import get_dataset
Genotype = namedtuple('Genotype', 'normal normal_concat reduce reduce_concat')




def compute(*args, **kwargs):
  __compute(*args, **kwargs, _compute = _compute)
  return None


def _compute(hyperparameter,cuda_device, JSON_CONFIG):
  ### Configuration 
  if type(JSON_CONFIG) != dict:
    with open(JSON_CONFIG) as f:
      data = json.load(f)
  else:
    data = JSON_CONFIG
      
  SETTINGS = data["WORKER_CONFIG"]
  SETTINGS["ID"] = hyperparameter["ID"]
  SETTINGS["database"] = data["DATABASE_NAME"]
  SETTINGS["experiment"] = data["EXPERIMENT_NAME"]
  ARCH_SETTINGS = data["ARCHITECTURE_CONFIG"]
  SAVE_PATH = data["SEARCH_CONFIG"]["PATH"]
  acc = []
  metric_logger = MetricLogger(SAVE_PATH) 
  recall = []
  if cuda_device == None:
     cuda_device = 3
  torch.cuda.empty_cache()
  #print(hyperparameter)
  torch.cuda.set_device(cuda_device)
  #torch.autograd.set_detect_anomaly(True)
  #with torch.autograd.profiler.profile() as prof:

  ##Dataset Initialisation
  name = SETTINGS["DATASET_CONFIG"]["NAME"]
  if data["GENERATE_PARTITION"]:
    DS_PATH = SETTINGS["DATASET_CONFIG"]["DATASET_PATH"]
  else:
    DS_PATH = None
  if "AUGMENTATIONS" in SETTINGS:
    augs = aug.initialise_augmentations(SETTINGS["AUGMENTATIONS"])
  else: 
    augs = None

  train_args = {"cuda_device":cuda_device,"augmentation" : augs, "binary" :SETTINGS["BINARY"],"path" : DS_PATH}
  test_args = {"cuda_device":cuda_device,"augmentation" :None, "binary" :SETTINGS["BINARY"],"path" : DS_PATH}

  if SETTINGS["RESAMPLES"]:
    dataset = get_dataset(name,train_args,None )
    kfold = KFold(n_splits = 5, shuffle = True)
    splits = [(None,None)]*SETTINGS["RESAMPLES"]
    train_dataset = dataset
    test_dataset = dataset
  elif SETTINGS["CROSS_VALIDATION_FOLDS"] == False: 
    train_dataset, test_dataset = get_dataset(name,train_args, test_args)
    splits = [(None,None)]
    #print(train_dataset, test_dataset)
  elif SETTINGS["CROSS_VALIDATION_FOLDS"]:
    dataset, test_dataset = get_dataset(name,train_args, test_args)
    kfold = KFold(n_splits = SETTINGS["CROSS_VALIDATION_FOLDS"], shuffle = False)
    splits = kfold.split(dataset.x.cpu().numpy(),y = dataset.y.cpu().numpy())
    train_dataset = dataset
    test_dataset = dataset

  n_classes = train_dataset.get_n_classes()
  multibatch = False
  torch.cuda.empty_cache()
   
  for _ in range(SETTINGS["REPEAT"]):
    
    if SETTINGS["GROUPED_RESAMPLES"]:
      # Initialize GroupKFold cross-validator with desired number of splits
      kfold = GroupKFold(n_splits=5)
      splits = [(None,None)]*SETTINGS["RESAMPLES"]
      train_dataset = dataset
      test_dataset = dataset

    elif SETTINGS["RESAMPLES"]:
      kfold = KFold(n_splits = 5, shuffle = True)
      splits = [(None,None)]*SETTINGS["RESAMPLES"]
      train_dataset = dataset
      test_dataset = dataset
    elif SETTINGS["CROSS_VALIDATION_FOLDS"] == False: 
      splits = [(None,None)]
    elif SETTINGS["CROSS_VALIDATION_FOLDS"]:
      kfold = KFold(n_splits = SETTINGS["CROSS_VALIDATION_FOLDS"], shuffle = True)
      splits = kfold.split(dataset.x.cpu().numpy(),y = dataset.y.cpu().numpy())
      train_dataset = dataset
      test_dataset = dataset
    #print("train",train_dataset.y.shape,train_dataset.y )
    #print("test",test_dataset.y.shape,test_dataset.y )
    for fold, (train_ids, test_ids) in enumerate(splits):    
      #print('---Fold No.--{}--------------------'.format(fold))
      torch.cuda.empty_cache()
      if SETTINGS["GROUPED_RESAMPLES"]:
         train_ids, test_ids = next(kfold.split(dataset.x.cpu().numpy(),y = dataset.y.cpu().numpy(),groups =dataset.groups))
         dataset.get_groups(train_ids,test_ids)
      elif SETTINGS["RESAMPLES"]:
        train_ids, test_ids = next(kfold.split(dataset.x.cpu().numpy(),y = dataset.y.cpu().numpy()))
      if SETTINGS["CROSS_VALIDATION_FOLDS"] or SETTINGS["RESAMPLES"]: 
        # Sample elements randomly from a given list of ids, no replacement.
        if SETTINGS["BALANCED_BATCH"]:
          train_batch_sampler = BalancedBatchSampler(dataset,SETTINGS["BATCH_SIZE"],train_ids)
          trainloader = torch.utils.data.DataLoader(dataset,collate_fn = collate_fn_padd,batch_sampler =train_batch_sampler)
        else: 
          train_subsampler = torch.utils.data.SubsetRandomSampler(train_ids)
          
          trainloader = torch.utils.data.DataLoader(
                                  dataset,collate_fn = collate_fn_padd,sampler = train_subsampler,
                                  batch_size=SETTINGS["BATCH_SIZE"], drop_last = True)
        test_subsampler = torch.utils.data.SubsetRandomSampler(test_ids)
        testloader = torch.utils.data.DataLoader(
                              dataset,collate_fn = collate_fn_padd,sampler = test_subsampler,
                              batch_size= SETTINGS["BATCH_SIZE"] ,drop_last = True)
      else:
        trainloader = torch.utils.data.DataLoader(
                                train_dataset,collate_fn = collate_fn_padd,shuffle = True,
                                batch_size=SETTINGS["BATCH_SIZE"], drop_last = True)
        testloader = torch.utils.data.DataLoader(
                            test_dataset,collate_fn = collate_fn_padd,shuffle = True,
                            batch_size= SETTINGS["BATCH_SIZE"] ,drop_last = True)
      if SETTINGS["RESAMPLES"] or SETTINGS["CROSS_VALIDATION_FOLDS"]:
        dataset.enable_augmentation(augs)
      n_classes = test_dataset.get_n_classes()
      evaluator = Evaluator(SETTINGS["BATCH_SIZE"], test_dataset.get_n_classes(),cuda_device,testloader = testloader)   
      #print("classes: {} - name: {}".format(train_dataset.get_n_classes(),name))
      #g = GraphConfigSpace(50)
      #s = g.sample_configuration()
      #s = s[0]
      if "stem" in hyperparameter["ops"]:
        stem_size = hyperparameter["ops"]["stem"]
      else:
        stem_size = ARCH_SETTINGS["STEM_SIZE"][0]

      model = InceptionTime(
        in_channels = train_dataset.get_n_features(), length = train_dataset.get_length() , 
        num_classes = train_dataset.get_n_classes() ,n_filters=32, kernel_sizes=[9,19,39], 
        use_residual=True, activation=nn.ReLU(), return_indices=False)
      """
      model = MultiResAtt(  input_channels = train_dataset.get_n_features(), n_filters = 64,num_classes =  train_dataset.get_n_classes())
      model = resnet18(num_classes = train_dataset.get_n_classes(),stem = train_dataset.get_n_features())
      """
      model = model.cuda(device = cuda_device)
      summary(model, (train_dataset.get_n_features(),test_dataset.get_length()))
      if SETTINGS["COMPILE"]:
        torch.set_float32_matmul_precision('high')
        model = torch.compile(model)
      #print(model)

      """
      ### Train the model
      """
      params = sum(p.numel() for p in model.parameters() if p.requires_grad)
      #print("Size: {}".format(params))
      train_model(model , SETTINGS, trainloader , cuda_device, evaluator = evaluator if SETTINGS["LIVE_EVAL"] else None, fold = fold, repeat = _) 
    #print(prof.key_averages().table(sort_by="self_cpu_time_total"))
      torch.cuda.empty_cache()
      model.eval()
      if (SETTINGS["RESAMPLES"] or SETTINGS["CROSS_VALIDATION_FOLDS"] ) and SETTINGS["TEST_TIME_AUGMENTATION"] == False:
        dataset.disable_augmentation()  
      evaluator.forward_pass(model, testloader,SETTINGS["BINARY"],n_iter = SETTINGS["TEST_ITERATION"])
      evaluator.predictions(model_is_binary = SETTINGS["BINARY"] , THRESHOLD = SETTINGS["THRESHOLD"])
      total = evaluator.T()
      acc.append( evaluator.T_ACC())
      recall.append(evaluator.TPR(1))
      recall_total = evaluator.P(1)
      print("Accuracy: ", "%.4f" % ((acc[-1])*100), "%")
      #print("Recall: ", "%.4f" % ((recall[-1])*100), "%")
      if SETTINGS["SAVE_WEIGHTS"]:
        torch.save(model.state_dict(),"{}/weights/{:.02f}-{}".format(SAVE_PATH,acc[-1],hyperparameter["ID"]))
      metric_logger.update({"ID" : hyperparameter["ID"], "accuracy" : acc[-1], "recall": recall[-1]})
    acc_ = np.mean(acc)
    recall_ = np.mean(recall)
    #print("Average Accuracy: ", "%.4f" % ((acc_)*100), "%")
  return acc_, recall_,params



if __name__ == "__main__":
    from HPO.general_utils import load
    with open(sys.argv[1]) as f:
      DATA = json.load(f)
      HP = DATA["WORKER_CONFIG"]
      j = DATA
      j["WORKER_CONFIG"]["MODEL_VALIDATION_RATE"] = 10
      j["WORKER_CONFIG"]["REPEAT"] = 10
      j["WORKER_CONFIG"]["RESAMPLES"] = True
      j["WORKER_CONFIG"]["PRINT_RATE_TRAIN"] = 50
      j["WORKER_CONFIG"]["LIVE_EVAL"] = True
      j["WORKER_CONFIG"]["GROUPED_RESAMPLES"] = False
      j["WORKER_CONFIG"]["DATASET_CONFIG"]["NAME"] = "Full_{}".format(HP["DATASET_CONFIG"]["NAME"] )
      search = load( "{}/{}".format(DATA["SEARCH_CONFIG"]["PATH"],"evaluations.csv"))
      HP["ID"] = "ResNet-Random-2"
      HP["graph"] = search["config"][search["best"].index(min(search["best"]))]["graph"]
      HP["ops"] = search["config"][search["best"].index(min(search["best"]))]["ops"]
    _compute(HP,1,j)

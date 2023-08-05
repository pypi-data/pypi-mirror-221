import numpy as np 
import time
import os 
import matplotlib.pyplot as plt
from HPO.utils.model import NetworkMain
from HPO.utils.DARTS_utils import config_space_2_DARTS
from HPO.utils.FCN import FCN 
import pandas as pd
import torch
from HPO.data.teps_datasets import Train_TEPS , Test_TEPS
import torch.nn as nn
from torch import Tensor
from torch.utils.data import DataLoader, SubsetRandomSampler
import random
import HPO.utils.augmentation as aug
from HPO.utils.train_utils import collate_fn_padd
from HPO.utils.train import train_model, auto_train_model
from HPO.utils.weight_freezing import freeze_FCN, freeze_resnet
from HPO.utils.ResNet1d import resnet18
from HPO.utils.files import save_obj
from queue import Empty
from sklearn.model_selection import StratifiedKFold as KFold
from collections import namedtuple
from HPO.utils.worker_score import Evaluator 
from HPO.utils.worker_utils import LivePlot
Genotype = namedtuple('Genotype', 'normal normal_concat reduce reduce_concat')


def compute( ID = None, configs=None , gpus=None , res = None  , config = None):
  device = None
  print("Starting process: {}".format(ID))
  while not configs.empty():
    try:
      if device == None:
        device = gpus.get(timeout = 10)
      config = configs.get(timeout = 10)
    except Empty:
      if device != None:
        gpus.put(device)
      
    except:
      torch.cuda.empty_cache()
      if device != None:
        gpus.put(device)
      return
    if config != None:
      print("Got Configuration!")

    if device != None:
      print("Starting config with device: {}".format(device))
      complete = False
      crashes = 0
      acc , rec =  _compute(hyperparameter = config , cuda_device = device)
      while not complete:
        try:
          
          complete = True
        except:
          crashes +=1
          print("Model crash: {} ".format(crashes))
          time.sleep(60)
          if crashes == 2:
            print("Final Crash giving score of zero")
            acc , rec = 0 , 0 
            complete = True
      res.put([config , acc , rec ]) 

  torch.cuda.empty_cache()
   
def _compute(hyperparameter,budget = 1, in_model = None , train_path = None,  test_path = None, cuda_device = None,plot_queue = None, model_id = None, binary = True):
  ### Configuration 
  THRESHOLD = 0.4 #Cut off for classification
  batch_size = 32
  if cuda_device == None:
     cuda_device = 0# torch.cuda.current_device()
  
  #      lr,
  #      p,
  #      jitter ,
  #      scaling ,
  #      window_warp_num,
  #      crop ,
  #      mix_up ,
  #      cut_out ,
  #      crop_rate ,
  #      jitter_rate,
  #      scaling_rate,
  #      window_warp_rate,
  #      mix_up_rate,
  #      cut_out_rate

  hpo = {'channels': 64,  'epochs': 100, 'layers': 3, 'normal_index_0_0': 0, 'normal_index_0_1': 1, 'normal_index_1_0': 2, 'normal_index_1_1': 1, 'normal_index_2_0': 3, 'normal_index_2_1': 2, 'normal_index_3_0': 2, 'normal_index_3_1': 4, 'normal_node_0_0': 'dil_conv_3x3', 'normal_node_0_1': 'none', 'normal_node_1_0': 'sep_conv_5x5', 'normal_node_1_1': 'max_pool_3x3', 'normal_node_2_0': 'avg_pool_3x3', 'normal_node_2_1': 'sep_conv_7x7', 'normal_node_3_0': 'skip_connect', 'normal_node_3_1': 'sep_conv_7x7', 'reduction_index_0_0': 0, 'reduction_index_0_1': 0, 'reduction_index_1_0': 1, 'reduction_index_1_1': 1, 'reduction_index_2_0': 1, 'reduction_index_2_1': 3, 'reduction_index_3_0': 2, 'reduction_index_3_1': 2, 'reduction_node_0_0': 'none', 'reduction_node_0_1': 'skip_connect', 'reduction_node_1_0': 'sep_conv_7x7', 'reduction_node_1_1': 'sep_conv_5x5', 'reduction_node_2_0': 'dil_conv_5x5', 'reduction_node_2_1': 'skip_connect', 'reduction_node_3_0': 'skip_connect', 'reduction_node_3_1': 'sep_conv_5x5'}

  hpo.update(hyperparameter)
  
  ##Set up augmentations##
  jitter = aug.Jitter(device = cuda_device,sigma = hyperparameter["jitter"], rate =hyperparameter["jitter_rate"])
  crop = aug.Crop(device = cuda_device, rate =hyperparameter["crop_rate"], crop_min = hyperparameter["crop"] , crop_max = 0.98)
  scaling = aug.Scaling(device = cuda_device, rate = hyperparameter["scaling_rate"], sigma = hyperparameter["scaling"])
  window_warp = aug.WindowWarp(device = cuda_device,rate = hyperparameter["window_warp_rate"])
  cut_out = aug.CutOut(device = cuda_device,perc = hyperparameter["cut_out"],rate = hyperparameter["cut_out_rate"])
  mix_up = aug.MixUp(device = cuda_device,m = hyperparameter["mix_up"], rate = hyperparameter["mix_up_rate"])
  augmentations = [mix_up,window_warp,jitter,scaling,crop,cut_out]

  dataset_train = Train_TEPS(samples_per_class = 100,augmentations = augmentations,device = cuda_device,one_hot = False,binary = binary,samples_per_epoch = 1)
  dataset_val = Test_TEPS(binary = binary,samples_per_class = 50,device = cuda_device,samples_per_epoch = 1,one_hot = False)
  dataset_test = Test_TEPS(binary = binary,samples_per_class = 500,device = cuda_device,one_hot = False)
  #dataset_test_full = Test_TEPS()
  torch.cuda.set_device(cuda_device)

  print("Cuda Device Value: ", cuda_device)
  gen = config_space_2_DARTS(hpo,reduction = True)

  n_classes = dataset_train.get_n_classes()
  inner = 2
  kfold = KFold(n_splits = inner, shuffle = True)
  multibatch = False
  for fold in range(budget):
      print('---Fold No.--{}----------------------'.format(fold))
      torch.cuda.empty_cache()
      if multibatch:
        batches = [2,4,8,16]
        trainloader = {}
        for i in batches:
          trainloader[i] = torch.utils.data.DataLoader(
                              dataset_train,collate_fn = collate_fn_padd,shuffle = True,
                              batch_size=i, drop_last = True)
      else:
        trainloader = torch.utils.data.DataLoader(
                          dataset_train,collate_fn = collate_fn_padd,shuffle = True,
                          batch_size=batch_size, drop_last = True)
      testloader = torch.utils.data.DataLoader(
                          dataset_test,collate_fn = collate_fn_padd,shuffle = False,
                          batch_size=2,drop_last = True)
      valloader =  torch.utils.data.DataLoader(
                          dataset_val,collate_fn = collate_fn_padd,shuffle = True,
                          batch_size=batch_size,drop_last = True)
      val_evaluator = Evaluator(batch_size, n_classes,cuda_device,testloader = valloader) 
      evaluator = Evaluator(2, n_classes,cuda_device,testloader = testloader) 

      model = NetworkMain(dataset_train.get_n_features(),hpo["channels"],num_classes= dataset_train.get_n_classes() , layers = hpo["layers"], auxiliary = False,drop_prob = hyperparameter["p"], genotype = gen, binary = binary)
      model = model.cuda(device = cuda_device)
      """
      ### Train the model
      """
      _ = train_model(model , hpo, trainloader, hpo["epochs"], batch_size , cuda_device, graph = plot_queue, binary = binary,evaluator=val_evaluator,logger = False) 
      ##with aug
      #logger = train_model(model , hpo, trainloader_aug , hpo["epochs"], batch_size , cuda_device, graph = plot_queue, binary = binary,evaluator=val_evaluator,logger = logger) 
      """
      ### Test the model
      """
      model = model.eval()
      evaluator.forward_pass(model, testloader,binary,n_iter = 1)
      #evaluator.predictions_threshold_matrix(binary)
      evaluator.predictions(model_is_binary = binary , THRESHOLD = THRESHOLD)
      tpr ,fpr, t,auc = evaluator.ROC()
      cm_all = evaluator.map_to_origin_class(dataset_test.get_true_labels())
      cm = evaluator.confusion_matrix
      ### Get Metrics
      total = evaluator.T()
      acc  =  evaluator.T_ACC()
      recall = evaluator.TPR(1)
      recall_total = evaluator.P(1)
      #sup = evaluator.sup_loss(model, testloader)
      print("Accuracy: ", "%.4f" % ((acc)*100), "%")
      
      ### Save Model
      def save_model(model, hpo):
        model_zoo = "{}/scripts/model_zoo/".format(os.environ["HOME"])
        torch.save(model.state_dict() , model_zoo+"-Acc-{}-Rec-{}".format(acc, recall))
        save_obj( hpo , model_zoo+"hps/"+"-Acc-{}-Rec-{}".format(acc , recall) )


  print("Final Scores -- ACC: {} -- REC: {}".format(acc, recall))
  return acc, recall

def report(l : list, name : str):
  std = np.std(l)
  avg = np.mean(l)
  print("{}: {} (+- {})".format(name,avg,std))

if __name__ == "__main__":
  import csv
  hpo = {'channels': 32, 'lr': 0.0025170869707739693, 'p': 0.15, 'epochs': 100, 'layers': 3}
  hyperparameter = {'normal_index_0_0': 0, 'normal_index_0_1': 0, 'normal_index_1_0': 1, 'normal_index_1_1': 1, 'normal_index_2_0': 3, 'normal_index_2_1': 3, 'normal_index_3_0': 2, 'normal_index_3_1': 2, 'normal_node_0_0': 'avg_pool_3x3', 'normal_node_0_1': 'sep_conv_7x7', 'normal_node_1_0': 'sep_conv_5x5', 'normal_node_1_1': 'sep_conv_5x5', 'normal_node_2_0': 'sep_conv_7x7', 'normal_node_2_1': 'avg_pool_3x3', 'normal_node_3_0': 'skip_connect', 'normal_node_3_1': 'sep_conv_5x5', 'reduction_index_0_0': 1, 'reduction_index_0_1': 0, 'reduction_index_1_0': 0, 'reduction_index_1_1': 1, 'reduction_index_2_0': 1, 'reduction_index_2_1': 2, 'reduction_index_3_0': 4, 'reduction_index_3_1': 1, 'reduction_node_0_0': 'sep_conv_3x3', 'reduction_node_0_1': 'dil_conv_5x5', 'reduction_node_1_0': 'none', 'reduction_node_1_1': 'max_pool_3x3', 'reduction_node_2_0': 'dil_conv_3x3', 'reduction_node_2_1': 'avg_pool_3x3', 'reduction_node_3_0': 'none', 'reduction_node_3_1': 'sep_conv_5x5'}
  hyperparameter={
  'normal_index_0_0': 1,
  'normal_index_0_1': 0,
  'normal_index_1_0': 0,
  'normal_index_1_1': 2,
  'normal_index_2_0': 1,
  'normal_index_2_1': 2,
  'normal_index_3_0': 3,
  'normal_index_3_1': 0,
  'normal_node_0_0': 'max_pool_3x3',
  'normal_node_0_1': 'sep_conv_3x3',
  'normal_node_1_0': 'skip_connect',
  'normal_node_1_1': 'skip_connect',
  'normal_node_2_0': 'sep_conv_7x7',
  'normal_node_2_1': 'sep_conv_5x5',
  'normal_node_3_0': 'skip_connect',
  'normal_node_3_1': 'sep_conv_7x7',
  'reduction_index_0_0': 1,
  'reduction_index_0_1': 0,
  'reduction_index_1_0': 0,
  'reduction_index_1_1': 2,
  'reduction_index_2_0': 0,
  'reduction_index_2_1': 2,
  'reduction_index_3_0': 0,
  'reduction_index_3_1': 4,
  'reduction_node_0_0': 'none',
  'reduction_node_0_1': 'none',
  'reduction_node_1_0': 'none',
  'reduction_node_1_1': 'dil_conv_3x3',
  'reduction_node_2_0': 'avg_pool_3x3',
  'reduction_node_2_1': 'dil_conv_5x5',
  'reduction_node_3_0': 'max_pool_3x3',
  'reduction_node_3_1': 'sep_conv_3x3'}
  hyperparameter={'normal_index_0_0': 0,
  'normal_index_0_1': 1,
  'normal_index_1_0': 0,
  'normal_index_1_1': 1,
  'normal_index_2_0': 2,
  'normal_index_2_1': 0,
  'normal_index_3_0': 2,
  'normal_index_3_1': 0,
  'normal_node_0_0': 'dil_conv_3x3',
  'normal_node_0_1': 'avg_pool_3x3',
  'normal_node_1_0': 'skip_connect',
  'normal_node_1_1': 'none',
  'normal_node_2_0': 'sep_conv_5x5',
  'normal_node_2_1': 'avg_pool_3x3',
  'normal_node_3_0': 'dil_conv_3x3',
  'normal_node_3_1': 'dil_conv_5x5',
  'reduction_index_0_0': 1,
  'reduction_index_0_1': 0,
  'reduction_index_1_0': 0,
  'reduction_index_1_1': 0,
  'reduction_index_2_0': 0,
  'reduction_index_2_1': 0,
  'reduction_index_3_0': 1,
  'reduction_index_3_1': 4,
  'reduction_node_0_0': 'max_pool_3x3',
  'reduction_node_0_1': 'sep_conv_7x7',
  'reduction_node_1_0': 'skip_connect',
  'reduction_node_1_1': 'sep_conv_5x5',
  'reduction_node_2_0': 'avg_pool_3x3',
  'reduction_node_2_1': 'sep_conv_7x7',
  'reduction_node_3_0': 'max_pool_3x3',
  'reduction_node_3_1': 'none'}
  
  hyperparameter = {'normal_index_0_0': 0, 'normal_index_0_1': 1, 'normal_index_1_0': 2, 'normal_index_1_1': 1, 'normal_index_2_0': 3, 'normal_index_2_1': 2, 'normal_index_3_0': 2, 'normal_index_3_1': 4, 'normal_node_0_0': 'dil_conv_3x3', 'normal_node_0_1': 'none', 'normal_node_1_0': 'sep_conv_5x5', 'normal_node_1_1': 'max_pool_3x3', 'normal_node_2_0': 'avg_pool_3x3', 'normal_node_2_1': 'sep_conv_7x7', 'normal_node_3_0': 'skip_connect', 'normal_node_3_1': 'sep_conv_7x7', 'reduction_index_0_0': 0, 'reduction_index_0_1': 0, 'reduction_index_1_0': 1, 'reduction_index_1_1': 1, 'reduction_index_2_0': 1, 'reduction_index_2_1': 3, 'reduction_index_3_0': 2, 'reduction_index_3_1': 2, 'reduction_node_0_0': 'none', 'reduction_node_0_1': 'skip_connect', 'reduction_node_1_0': 'sep_conv_7x7', 'reduction_node_1_1': 'sep_conv_5x5', 'reduction_node_2_0': 'dil_conv_5x5', 'reduction_node_2_1': 'skip_connect', 'reduction_node_3_0': 'skip_connect', 'reduction_node_3_1': 'sep_conv_5x5'}

  #hyperparameter = {'normal_index_0_0': 1, 'normal_index_0_1': 1, 'normal_index_1_0': 2, 'normal_index_1_1': 1, 'normal_index_2_0': 3, 'normal_index_2_1': 2, 'normal_index_3_0': 4, 'normal_index_3_1': 0, 'normal_node_0_0': 'skip_connect', 'normal_node_0_1': 'dil_conv_5x5', 'normal_node_1_0': 'dil_conv_3x3', 'normal_node_1_1': 'sep_conv_5x5', 'normal_node_2_0': 'dil_conv_3x3', 'normal_node_2_1': 'none', 'normal_node_3_0': 'max_pool_3x3', 'normal_node_3_1': 'sep_conv_7x7', 'reduction_index_0_0': 1, 'reduction_index_0_1': 0, 'reduction_index_1_0': 1, 'reduction_index_1_1': 2, 'reduction_index_2_0': 1, 'reduction_index_2_1': 3, 'reduction_index_3_0': 1, 'reduction_index_3_1': 2, 'reduction_node_0_0': 'avg_pool_3x3', 'reduction_node_0_1': 'skip_connect', 'reduction_node_1_0': 'dil_conv_3x3', 'reduction_node_1_1': 'dil_conv_5x5', 'reduction_node_2_0': 'sep_conv_7x7', 'reduction_node_2_1': 'avg_pool_3x3', 'reduction_node_3_0': 'avg_pool_3x3', 'reduction_node_3_1': 'sep_conv_5x5'}
  df = pd.DataFrame(columns = ["accuracy", "recall", "confusion_matrix","confusions_matrix_all","tpr","fpr","thresholds","auc"])
  for i in range(20):
      a,r,cm,cm_all,tpr,fpr,t,auc = _compute(hyperparameter, binary = True)
      df.loc[len(df.index)] = [a,r, cm,cm_all,tpr,fpr,t,auc]


  


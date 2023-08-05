import random
import torch
import torch.nn as nn
import numpy as np
import json
from HPO.utils.triplet import Batch_All_Triplet_Loss as Triplet_Loss
from torch import Tensor
from HPO.utils.train_log import Logger
from HPO.utils.utils import calculate_train_vals
from HPO.utils.model_constructor import Model
from torch.utils.data import DataLoader
from HPO.utils.train_utils import stdio_print_training_data
from sklearn.metrics import confusion_matrix

def stdio_print_training_data( iteration : int , outputs : Tensor, labels : Tensor , epoch : int, epochs : int, correct :int , total : int , peak_acc : float , loss : Tensor, n_iter, loss_list = None, binary = True):
  def cal_acc(y,t):
    c = np.count_nonzero(y.T==t)
    tot = len(t)
    return c , tot

  def convert_label_max_only(y):
    y = y.cpu().detach().numpy()
    idx = np.argmax(y,axis = 1)
    out = np.zeros_like(y)
    for count, i in enumerate(idx):
        out[count, i] = 1
    return idx
  if binary == True:
    new_correct , new_total = cal_acc(outputs.ge(0.5).cpu().detach().numpy(), labels.cpu().detach().numpy())
  elif len(labels.shape) > 1:
    new_correct , new_total =  cal_acc(convert_label_max_only(outputs), convert_label_max_only(labels))
  else:
    new_correct , new_total =  cal_acc(convert_label_max_only(outputs), labels.cpu().detach().numpy())
  correct += new_correct 
  total += new_total
  acc = correct / total 
  if acc > peak_acc:
    peak_acc = acc
  # Save the canvas
  print("Epoch (",str(epoch),"/",str(epochs), ") Accuracy: ","%.2f" % acc, "Iteration(s) (", str(iteration),"/",str(n_iter), ") Loss: "
    ,"%.6f" % loss," Correct / Total : {} / {} ".format(correct , total),  end = '\r')
  return correct ,total ,peak_acc

def train_model_triplet(model : Model , hyperparameter : dict, dataloader : DataLoader , epochs : int, 
    batch_size : int, cuda_device = None, augment_on = 0, graph = None, binary = False,evaluator= None,logger = None,run = None):
  if cuda_device == None:
    cuda_device = torch.cuda.current_device()
  n_iter = len(dataloader) 
  optimizer = torch.optim.Adam(model.parameters(),lr = hyperparameter["lr"])
  #scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, "max",patience = 4,verbose = True, factor = 0.1,cooldown = 2,min_lr = 0.0000000000000001)
  scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer,epochs)
  criterion = Triplet_Loss(m = 0.1 , device = cuda_device)
  epoch = 0
  peak_acc = 0
  loss_list = []
  total = 0
  correct = 0
  acc = 0
  recall = 0
  if logger == None:
    logger = Logger()
  while epoch < epochs:

    loss_values = 0
    if epoch % 3 == 0:
      total = 0
      correct = 0
    for i, (samples, labels) in enumerate( dataloader ):
      batch_size = samples.shape[0]
      optimizer.zero_grad()
      outputs = model(samples)
      if binary:
        loss = criterion(outputs.view(batch_size), labels.float()).cuda(device = cuda_device)
      else:
        loss = criterion(outputs, labels).cuda(device = cuda_device)
      loss.backward()
      optimizer.step()
      loss_values += criterion.get_fraction_pos()
      if i % 5 == 0:
        print("Epoch {} - [{}/{}] loss over epoch: {}".format(epoch,i,len(dataloader),loss_values/i))
    if epoch % 1 == 0 and run != None:
        torch.save(model.state_dict() ,"SWA/run-{}-checkpoint-{}".format(run, epoch))
    if epoch % 5 == 0:
        torch.save(model.state_dict() ,"triplet-{}".format(epoch))
        if evaluator != None:
          model.eval()
          evaluator.forward_pass(model,binary = binary)
          evaluator.predictions(model_is_binary = binary,THRESHOLD = 0.4)
          if binary:
            evaluator.ROC("train")
          acc = evaluator.T_ACC()
          recall = evaluator.TPR(1)
          evaluator.reset_cm()
          model.train()
          print("")
          print("Validation set Accuracy: {} -- Recall: {}".format(acc,recall))
          print("")
    scheduler.step()
    epoch += 1
  print()
  print("Num epochs: {}".format(epoch))
  return logger

def clone_state_dict(state_dict):
    return {name: val.clone() for name, val in state_dict.items()}

def average_state_dicts(state_dicts):
    avg_state_dict = {name: torch.stack([d[name] for d in state_dicts], dim=0).mean(dim=0)
                      for name in state_dicts[0] if state_dicts[0][name].dtype.is_floating_point}
    return avg_state_dict

def train_model(model : Model , hyperparameter : dict, dataloader : DataLoader ,
     cuda_device = None, evaluator= None,logger = None,run = None,fold = None, repeat = None):

  params = sum(p.numel() for p in model.parameters() if p.requires_grad)
  #INITIALISATION
  EPOCHS = hyperparameter["EPOCHS"]
  BATCH_SIZE = hyperparameter["BATCH_SIZE"] 
  BINARY = hyperparameter["BINARY"]
  PRINT_RATE_TRAIN = hyperparameter["PRINT_RATE_TRAIN"]
  if cuda_device == None:
    cuda_device = torch.cuda.current_device()
  n_iter = len(dataloader) 

  #CONFIGURATION OF OPTIMISER AND LOSS FUNCTION
  optimizer = torch.optim.Adam(model.parameters(),lr = hyperparameter["LR"])
  if hyperparameter["SCHEDULE"] == True:
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer,EPOCHS,eta_min = hyperparameter["LR_MIN"])
  if hyperparameter["BINARY"] == True:
    criterion = nn.BCEWithLogitsLoss().cuda(device = cuda_device)
  else:
    criterion = nn.CrossEntropyLoss().cuda(device = cuda_device)

  #INITIALISE TRAINING VARIABLES
  epoch = 0
  peak_acc = 0
  loss_list = []
  total = 0
  correct = 0
  cm_test = ""
  acc = 0
  val_loss = torch.Tensor([0])
  recall = 0
  val_acc = 0
  if hyperparameter["LOGGING"]:
    logger = Logger(hyperparameter["database"],hyperparameter["experiment"],hyperparameter["DATASET_CONFIG"]["NAME"],fold,repeat,params)
  else:
    logger = None


  #MAIN TRAINING LOOP
  while epoch < EPOCHS:
    if epoch % 3 == 0:
      total = 0
      pred_tensor = torch.Tensor()
      gt_tensor = torch.Tensor()
      correct = 0
    weights =[]
    for i, (samples, labels) in enumerate( dataloader ):
      optimizer.zero_grad()
      #samples, labels = samples.cuda(cuda_device).float(), labels.cuda(cuda_device).long()
      outputs = model(samples)
      if BINARY == True:
        loss = criterion(outputs.view(BATCH_SIZE), labels.float())
      else:
        loss = criterion(outputs, labels)
      loss.backward()
      optimizer.step()
      if hyperparameter["WEIGHT_AVERAGING_RATE"] and epoch > EPOCHS/2:
        weights.append(clone_state_dict(model.state_dict()))
      if hyperparameter["LOGGING"]:
        pred_tensor = torch.cat((pred_tensor, outputs.detach().cpu().flatten(end_dim = 0)))
        gt_tensor = torch.cat((gt_tensor, labels.detach().cpu().flatten()))

      if PRINT_RATE_TRAIN and i % PRINT_RATE_TRAIN == 0:
        correct , total, peak_acc = stdio_print_training_data(i , outputs , labels, epoch,EPOCHS , correct , total, peak_acc, loss.item(), n_iter, loss_list,binary = BINARY)

    if hyperparameter["LOGGING"]:
      cm_train, train_acc = calculate_train_vals(pred_tensor,gt_tensor)
      if PRINT_RATE_TRAIN:
        pred_labels = torch.argmax(pred_tensor, dim=1).numpy()
        gt_labels = gt_tensor.numpy()
        with np.printoptions(linewidth = (10*len(np.unique(gt_labels))+20),precision=4, suppress=True):
          print(confusion_matrix(gt_labels,pred_labels))

    if hyperparameter["MODEL_VALIDATION_RATE"] and epoch % hyperparameter["MODEL_VALIDATION_RATE"] == 0:
        if evaluator != None:
          model.eval()
          evaluator.forward_pass(model,binary = BINARY)
          evaluator.predictions(model_is_binary = BINARY,THRESHOLD = hyperparameter["THRESHOLD"])
          val_loss = 0#evaluator.calculate_loss(criterion,BINARY)
          val_acc = evaluator.T_ACC()
          recall = evaluator.TPR(1)
          cm_test = evaluator.confusion_matrix.copy()
          bal_acc = evaluator.balanced_acc()
          evaluator.reset_cm()
          model.train()
          print("")
          print("Validation set Accuracy: {} -- Balanced Accuracy: {} -- loss: {}".format(val_acc, bal_acc ,val_loss))
          print("")

    if hyperparameter["LOGGING"]:
      cm_test = json.dumps(cm_test.tolist())
      logger.update({
        "loss": loss.item(), 
        "training_accuracy": train_acc,
        "ID":hyperparameter["ID"],
        "epoch": epoch, 
        "validation_accuracy": val_acc, 
        "lr":optimizer.param_groups[0]['lr'],
        "validation_loss": val_loss.item(),
        "confusion_matrix_train": cm_train,
        "confusion_matrix_test": cm_test
        })


    if hyperparameter["SCHEDULE"] == True:
      scheduler.step()
    epoch += 1
  if hyperparameter["WEIGHT_AVERAGING_RATE"]:  
    model.load_state_dict(average_state_dicts(weights))
  #print()
  #print("Num epochs: {}".format(epoch))
  if hyperparameter["LOGGING"]:
    logger.close()
  return logger

def train_model_regression(model : Model , hyperparameter : dict, dataloader : DataLoader ,
     cuda_device = None, evaluator= None,logger = None,run = None):

  #INITIALISATION
  EPOCHS = hyperparameter["EPOCHS"]
  VISUAL = True
  BATCH_SIZE = hyperparameter["BATCH_SIZE"] 
  BINARY = hyperparameter["BINARY"]
  PRINT_RATE_TRAIN = hyperparameter["PRINT_RATE_TRAIN"]
  if cuda_device == None:
    cuda_device = torch.cuda.current_device()
  n_iter = len(dataloader) 

  #CONFIGURATION OF OPTIMISER AND LOSS FUNCTION
  optimizer = torch.optim.Adam(model.parameters(),lr = hyperparameter["LR"])
  scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer,EPOCHS)
  criterion = nn.MSELoss().cuda(device = cuda_device)

  #INITIALISE TRAINING VARIABLES
  epoch = 0
  peak_acc = 0
  loss_list = []
  total = 0
  correct = 0
  acc = 0
  recall = 0
  if logger != False or logger == None:
    logger = Logger()
  #MAIN TRAINING LOOP
  while epoch < EPOCHS:
    if epoch % 3 == 0:
      total = 0
      correct = 0
    for i, (samples, labels) in enumerate( dataloader ):
      optimizer.zero_grad()
      #samples, labels = samples.cuda(cuda_device).float(), labels.cuda(cuda_device).long()
      outputs = model(samples)
      if BINARY == True:
        loss = criterion(outputs.view(BATCH_SIZE), labels.float())
      else:
        loss = criterion(outputs.squeeze(), labels)
      loss.backward()
      optimizer.step()

      if PRINT_RATE_TRAIN and i % PRINT_RATE_TRAIN == 0:
        correct , total, peak_acc = stdio_print_training_data(i , outputs , labels, epoch,EPOCHS , correct , total, peak_acc, loss.item(), n_iter, loss_list,binary = BINARY)
      if logger != False:
        logger.update({"loss": loss.item(), "training_accuracy": (correct/total),"index" : i,
              "epoch": epoch, "validation_accuracy": acc, "lr":optimizer.param_groups[0]['lr'],"validation recall": recall })
    if hyperparameter["WEIGHT_AVERAGING_RATE"] and epoch % hyperparameter["WEIGHT_AVERAGING_RATE"] == 0:
        torch.save(model.state_dict() ,"SWA/run-{}-checkpoint-{}".format(run, epoch))
    if hyperparameter["MODEL_VALIDATION_RATE"] and epoch % hyperparameter["MODEL_VALIDATION_RATE"] == 0 and epoch != 0:
        if evaluator != None:
          model.eval()
          evaluator.regression(model,epoch,hyperparameter)
          model.train()
    epoch += 1
    scheduler.step()
  #print()
  #print("Num epochs: {}".format(epoch))
  return logger


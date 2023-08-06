import numpy as np
from skimage.io import imread,imshow
from skimage.transform import resize
import pandas as pd
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import tensorflow as tf
import os
import random
import numpy as np
import subprocess
import sys
import string
import os.path
import re
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import math
import cv2

from  .arc_unet import arc_UNET
from .gen_video import gen_video
from  .test_iou import test_iou
from  .train import train
from .XY import XY



def pipeline(modelarc, dir_X, dir_Y,optimizer,loss,metrics,dim=(0,0),validation_split=0.1,batch_size=8,epochs=200,patience=100,monitor='val_loss',best=False,video=False):
    """
    Runs all neccessary functions to pull the data, build the model, train the model, collect the results, and plot the results 
    
    Authors:
        Zhuldyz Ualikhankyzy, Tommy Ciardi 

    :param modelarc: architecture of model 
    :type modelarc: string 
    :param dir_X: directory with input images 
    :type dir_X: string
    :param dir_Y: directory with input images 
    :type dir_Y: string
    :param optimizer: optimizer to be used 
    :type optimizer: string 
    :param loss: loss to be used 
    :type loss: string 
    :param metrics: all metrics to be monitored  
    :type metrics: list  
    :param dim: dimension of the image 
    :type dim: tuple  
    :param validation_split: the fraction of the dataset to be used in validation 
    :type validation_split: float  
    :param batch_size: number of data samples that will be processed together in each forward and backward pass during training  
    :type batch_size: integer 
    :param epochs: number of times the entire dataset will be passed through the model during training
    :type epochs: integer  
    :param patience: number of epochs to wait before stopping the training process if early stopping is on 
    :type patience: integer  
    :param monitor: metric that the early stopping algorithm should monitor to determine whether to stop the training process or not  
    :type monitor: string  
    :param best: if true, then the best model is saved, otherwise, the last iteration is saved 
    :type best: boolean    
    :param video: if true, then the video with ground truth and predicted masks
    :type video: boolean
    """
    model_architectures = {
        'UNET': arc_UNET,
        #'UNET+': UNETplus,
        #'UNET++': UNETplusplus,
    }
    if modelarc in model_architectures:
        selected_model = model_architectures[modelarc]
        X_train,Y_train,X_test,Y_test,IMG_HEIGHT,IMG_WIDTH = XY(dir_X, dir_Y,dim)
        model = selected_model(IMG_HEIGHT,IMG_WIDTH,optimizer,loss, metrics)
        filename, modelweights = train(X_train,Y_train,X_test,Y_test,model, validation_split, batch_size, epochs, patience, monitor, best)
        predict_test_t = test_iou (X_test, Y_test, model, modelweights)
        if video==True:
            gen_video(Y_test,predict_test_t,filename)
    else:
        raise ValueError("Invalid model name. Supported models are: " + ", ".join(model_architectures.keys()))

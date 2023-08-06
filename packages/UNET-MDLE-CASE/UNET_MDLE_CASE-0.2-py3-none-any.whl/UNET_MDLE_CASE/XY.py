import numpy as np
from skimage.io import imread,imshow
from skimage.transform import resize
import pandas as pd
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import tensorflow as tf
import os
import random
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


from .resizedim import resizedim


def XY(dir_X, dir_Y,dim): 
    """
    Pulls input X images and target Y images from their respective directories
    
    Authors:
        Zhuldyz Ualikhankyzy, Tommy Ciardi 

    :param dir_X: directory with input images 
    :type dir_X: string 
    :param dir_Y: direcory with target images
    :type dir_Y: string 
    :param dim: dimension of the image 
    :type dim: tuple 
    :return X_train,Y_train,X_test,Y_test,IMG_HEIGHT,IMG_WIDTH:
        - X_train - training input images 
        - Y_train - training target images 
        - X_test - testing input images
        - Y_test - testing target images
        - IMG_HEIGHT - height of image 
        - IMG_WIDTH - width of image 
    :rtype: 
        - X_train - list of  numpy.ndarray 
        - Y_train - list of  numpy.ndarray 
        - X_test - list of  numpy.ndarray 
        - Y_test - list of  numpy.ndarray 
        - IMG_HEIGHT - int  
        - IMG_WIDTH - int
    """

    X_paths = []
    for filename in os.listdir(dir_X):
        X_paths.append(os.path.join(dir_X, filename))

    Y_paths = []
    for filename in os.listdir(dir_Y):
        Y_paths.append(os.path.join(dir_Y, filename))

    X_train_paths, X_test_paths, Y_train_paths, Y_test_paths = train_test_split(X_paths, Y_paths, test_size=0.2, random_state=42)

    if (len(X_train_paths)!=len(Y_train_paths)):
        raise ValueError("Mismatch in the number of X(raw images) and Y(masks)")
    else: 
        IMG_HEIGHT,IMG_WIDTH = resizedim(X_train_paths,dim)
        IMG_CHANNELS = 1 

        X_train = np.zeros((len(X_train_paths), IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
        Y_train = np.zeros((len(Y_train_paths), IMG_HEIGHT, IMG_WIDTH, 1), dtype=np.bool)
        
        for n,filename in enumerate(X_train_paths):
            img = imread(filename)
            if len(img.shape) > 2:
                img = img[:,:,0]
            img = resize(img, (IMG_HEIGHT, IMG_WIDTH), mode='constant', preserve_range=True)
            img = np.expand_dims(img, axis=-1) 
            X_train[n] = img
        
        for n,filename in enumerate(Y_train_paths):
            mask_ = imread(filename)
            mask_ = np.expand_dims(resize(mask_, (IMG_HEIGHT, IMG_WIDTH), mode='constant',  
                                            preserve_range=True), axis=-1)
            Y_train[n] = mask_   

        X_test = np.zeros((len(X_test_paths), IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
        Y_test = np.zeros((len(Y_test_paths), IMG_HEIGHT, IMG_WIDTH, 1), dtype=np.bool)

        for n,filename in enumerate(X_test_paths):
            img = imread(filename)
            if len(img.shape) > 2:
                img = img[:,:,0]
            img = resize(img, (IMG_HEIGHT, IMG_WIDTH), mode='constant', preserve_range=True)
            img = np.expand_dims(img, axis=-1)
            X_test[n] = img

        for n,filename in enumerate(Y_test_paths):
            mask_ = imread(filename)
            mask_ = np.expand_dims(resize(mask_, (IMG_HEIGHT, IMG_WIDTH), mode='constant',  
                                            preserve_range=True), axis=-1)
            Y_test[n] = mask_  

        return X_train,Y_train,X_test,Y_test,IMG_HEIGHT,IMG_WIDTH
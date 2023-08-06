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
import math
import cv2
from PIL import Image
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model


def test_iou (X_test,Y_test, model, modelweights):
    """
    Calculates the IoU of test set

    Authors:
        Zhuldyz Ualikhankyzy, Tommy Ciardi 
    
    :param X_test: X train images
    :type X_test: list of numpy.ndarray 
    :param Y_test: Y test images
    :type Y_test: list of numpy.ndarray 
    :param model: model to be used  
    :type model: TensorFlow Keras Model   
    :param modelweights: name of the file with the weights of the trained model  
    :type modelweights: string  

    """

    def calculate_iou(y_true, y_pred):
        """
        Calculates the IoU

        Authors:
            Zhuldyz Ualikhankyzy, Tommy Ciardi 

        :param y_true: Y test images
        :type y_true: list of numpy.ndarray 
        :param y_pred: predicted masks   
        :type y_pred:list of numpy arrays 
        :param iou_score: value of iou  
        :type iou_score: float   

        """
        intersection = np.logical_and(y_true, y_pred)
        union = np.logical_or(y_true, y_pred)
        iou_score = np.sum(intersection) / np.sum(union)
        return iou_score

    # Load the previously trained model
    model.load_weights(modelweights)  
    predict_test = model.predict(X_test, verbose=1)
    predict_test_t = (predict_test > 0.5).astype(np.uint8)


    iou_scores = []
    for i in range(len(X_test)):
        iou = calculate_iou(Y_test[i], predict_test_t[i])
        iou_scores.append(iou)


    return predict_test_t,np.mean(iou_scores)
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



def gen_video(Y_test,predict_test_t,filename):
    """
    Generates a video of image sequences to compare ground truth and predicted masks 

    Authors:
        Zhuldyz Ualikhankyzy, Tommy Ciardi 

    :param Y_test: Y test images
    :type Y_test: list of numpy.ndarray 
    :param predict_test_t: predicted masks   
    :type predict_test_t:list of numpy arrays 
    :param filename: name of the initial .txt file with outputs 
    :type filename: string  

    """

    output_file = re.findall(r'\d+', filename)[0] + '_test.mp4'
    num_images = min(len(Y_test), len(predict_test_t))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_out = cv2.VideoWriter(output_file, fourcc, 3, (Y_test[0].shape[1], Y_test[0].shape[0]))

    white = [255, 255, 255] 
    red = [255, 0, 0] 
    blue = [0, 0, 255]  

    for i in range(num_images):
        y_true_image = Y_test[i]
        predicted_image = predict_test_t[i]

        if len(y_true_image.shape) == 3 and y_true_image.shape[-1] == 1:
            y_true_image = y_true_image[..., 0]
        if len(predicted_image.shape) == 3 and predicted_image.shape[-1] == 1:
            predicted_image = predicted_image[..., 0]

        y_true_image = np.uint8(y_true_image * 255)
        predicted_image = np.uint8(predicted_image * 255)

        combined_image = np.zeros((y_true_image.shape[0], y_true_image.shape[1], 3), dtype=np.uint8)
        combined_image[y_true_image > 0] = red  
        combined_image[predicted_image > 0] = blue 
        combined_image[(y_true_image > 0) & (predicted_image > 0)] = white 
        video_out.write(combined_image)
    video_out.release()
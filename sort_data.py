from phasefield_scripts.load_files import *
from phasefield_scripts.procedures import *
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
import ipywidgets as widget
from ipywidgets import fixed
import os
import pickle
import multiprocessing as mp
from tqdm import tqdm
from multiprocessing import Pool
import pandas as pd

#function based on sort_data.ipynb to read images and sort them into T0 and T1 folders 

#T1 folder contains images with T1 transitions
#T0 folder contains images without T1 transitions!

def sort_data(expname):
    input_dir = 'data\\' + expname + '\images'
    result_dir = input_dir + '/sorted_data'
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)\
    
    T1_array = np.load(input_dir + '/T1_status.npy')

    def image_loader(data_dir):
        images = []
        image_files = [image_file for image_file in os.listdir(data_dir) if image_file.startswith('img')]
        for image_name in image_files:
            images.append(image_files)
        data = np.array(image_files)
        return data

    images = image_loader(input_dir)
    
    for i in range(len(T1_array)):
        if T1_array[i] == 1:
            if not os.path.exists(result_dir + '/T1'):
                os.makedirs(result_dir + '/T1')
            os.rename(input_dir + '/' + images[i], result_dir + '/T1/' + images[i])
        else:
            if not os.path.exists(result_dir + '/T0'):
                os.makedirs(result_dir + '/T0')
            os.rename(input_dir + '/' + images[i], result_dir + '/T0/' + images[i])
    
            
            
# test = sort_data('i3c3a1d0v5a0_set18b')
        
#make a list with experiments that you want this to be done for, and run the function for each experiment: 
experiments = [
    # 'i3c3a1d0v5a0_set18a',
    # 'i3c3a1d0v5a0_set18b',
    # 'i3c3a1d0v5a0_set18d',
    # 'i3c3a1d0v5a2_set21',
    'i3c3a1d0v5a7_set21',
    'i3c3a1d0v5a14_set21',
    'i3c3a1d0v5a15_set21',
    'i3c3a1d1v5a0_set22',
    'i3c3a1d1v5a7_set22',
    'i3c4a1d0v5a0_set20',
    'i3c4a1d0v5a0_set23',
    'i3c5a1d0v5a0_set20',
    'i3c5a1d0v5a0_set23',
               ]

test_experiments = [
            'i3c3a1d0v5a0_set18d',
            'i3c3a1d0v5a2_set21'
               ]


# print(test_experiments[0])
for i in range(len(experiments)):
    sort_data(experiments[i])

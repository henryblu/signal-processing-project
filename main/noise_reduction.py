import pandas as pd
import numpy as np
from scipy import fftpack

def noise_reduction(fourier_transform, threadshold_level):
    '''this function performs a noise reduction on a given fourier transform depended on the given threashold
    '''
    # first we clean up the fourier transform to have only frequencies smaller then 20000 and positive 

    # then we calculate the mean and standard deviation of the fourier transform
    mean = np.mean(fourier_transform)
    std = np.std(fourier_transform)
    # then we calculate the threadshold
    try:
        if (threadshold_level < 0):
            print('threadshold level must be a non negitive integer')
            exit
    except TypeError:
        print('threadshold level must be a number')
        exit
    
    threadshold = mean - (4-threadshold_level)*std
    # then we set all the values in the fourier transform that are below the threadshold to 0
    
    
    # then we return the fourier transform
    return fourier_transform

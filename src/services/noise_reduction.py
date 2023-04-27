import numpy as np

def noise_reduction(fourier_transform, threadshold_level):
    '''this function performs a noise reduction on a given fourier transform depended on the given threashold. It dosnt work yet
    '''
    # first we calculate the mean and the standard deviation of the fourier transform
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
    
    return fourier_transform

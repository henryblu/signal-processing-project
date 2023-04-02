import pandas as pd
import numpy as np


def discrete_fourier_transform(audio_data):
    ''' this function performs the discrete fourier transform on a given audio data
    '''
    N = len(audio_data)
    fourier_transform = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            fourier_transform[k] += audio_data[n]*np.exp(-2j*np.pi*k*n/N)
    return fourier_transform


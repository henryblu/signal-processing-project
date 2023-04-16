import pandas as pd
import numpy as np
from scipy import fftpack


def regular_fourier_transform(audio_data):
    ''' this function performs a regualr fourier transform on a given audio data
    '''
    N = len(audio_data)
    fourier_transform = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            fourier_transform[k] += audio_data[n]*np.exp(-2j*np.pi*k*n/N)
    return fourier_transform


def fast_fourier_transform(audio_data):
    ''' This function performs a fast fourier transform on a given audio data it only workd for audio data with a length that is a power of 2
    '''
    N = int(len(audio_data))

    if N <= 1:
        return audio_data
    elif N % 2 != 0: 
       raise ValueError("size of audio_data must be a power of 2")
    
    even = fast_fourier_transform(audio_data[:N:2])
    odd = fast_fourier_transform(audio_data[1:N:2])

    factor = np.exp(-2j*np.pi*np.arange(N)/N)
    
    return np.concatenate([even + factor[:N//2]*odd, even + factor[N//2:]*odd])

def inverse_regular_fourier_transform(fourier_transform):
    ''' this function performs an inverse regular fourier transform on a given fourier transform
    '''

    N = len(fourier_transform)
    inverse_fourier_transform = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            inverse_fourier_transform[k] += fourier_transform[n]*np.exp(2j*np.pi*k*n/N)

    return inverse_fourier_transform/N


def inverse_fast_fourier_transform(fourier_transform):
    ''' this function performs an inverse fast fourier transform on a given fourier transform
    '''
    N = int(len(fourier_transform))
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(2j * np.pi * k * n / N)
    return np.dot(M, fourier_transform)/N

    
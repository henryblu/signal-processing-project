import pandas as pd
import numpy as np
from scipy import fftpack


def discrete_fourier_transform(audio_data):
    ''' this function performs a regualr fourier transform on a given audio data
    '''
    N = len(audio_data)
    fourier_transform = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            fourier_transform[k] += audio_data[n]*np.exp(-2j*np.pi*k*n/N)
    return fourier_transform

def fast_fourier_transform(audio_data):
    ''' this function performs a fastg fourier transform on a given audio data
    '''
    N = len(audio_data)
    if N <= 1:
        return audio_data
    even = fast_fourier_transform(audio_data[::2])
    odd = fast_fourier_transform(audio_data[1::2])
    fourier_transform = [0]*N
    for k in range(N//2):
        fourier_transform[k] = even[k] + np.exp(-2j*np.pi*k/N)*odd[k]
        fourier_transform[k+N//2] = even[k] - np.exp(-2j*np.pi*k/N)*odd[k]

    # this isnt working yet and I cant seem to figure out whats wrong. will try again later
    # fourier_transform = fourier_transform[:len(fourier_transform)//2]
    
    return fourier_transform

def inverse_fast_fourier_transform(fourier_transform):
    ''' this function performs an inverse fast fourier transform on a given fourier transform
    '''
    #new_sound_wave = fftpack.ifft(fourier_transform)
    N = len(fourier_transform)
    if N <= 1:
        return fourier_transform
    even = inverse_fast_fourier_transform(fourier_transform[::2])
    odd = inverse_fast_fourier_transform(fourier_transform[1::2])
    audio_data = [0]*N
    for k in range(N//2):
        audio_data[k] = even[k] + np.exp(2j*np.pi*k/N)*odd[k]
        audio_data[k+N//2] = even[k] - np.exp(2j*np.pi*k/N)*odd[k]
    return audio_data

    #return new_sound_wave


    
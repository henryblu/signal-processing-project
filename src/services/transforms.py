import numpy as np

def transform_caller(rft, fft, sample_rate, composite_signal):
    '''  this function is used to call the appropreate transform 
    '''
    if rft and fft:
        print("You may only select one fourier transform")
        return

    elif rft:
        fourier_transform = regular_fourier_transform(composite_signal)
        inverse = inverse_regular_fourier_transform(fourier_transform)
    elif fft:
        fourier_transform = fast_fourier_transform(composite_signal)
        inverse = inverse_fast_fourier_transform(fourier_transform)
    else:
        print("no fourier transform selected")
        print("defaulting to fast fourier transform")
        fourier_transform = fast_fourier_transform(composite_signal)
        inverse = inverse_fast_fourier_transform(fourier_transform)
    
    return fourier_transform, inverse

def regular_fourier_transform(audio_data):
    ''' this function performs a regualr fourier transform on a given audio data
    '''
    N = len(audio_data)
    fourier_transform = np.zeros(N, dtype=complex)
    for k in range(N):
        for q in range(N):
            fourier_transform[k] += audio_data[q]*np.exp(-2j*np.pi*k*q/N)
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
        for q in range(N):
            inverse_fourier_transform[k] += fourier_transform[q]*np.exp(2j*np.pi*k*q/N)

    return inverse_fourier_transform/N

def inverse_fast_fourier_transform(fourier_transform):
    ''' this function performs an inverse fast fourier transform on a given fourier transform
    '''
    N = int(len(fourier_transform))
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(2j * np.pi * k * n / N)
    return np.dot(M, fourier_transform)/N

    
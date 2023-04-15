from fourier import *
from visualisations import *
from scipy.fft import fft, ifft
from scipy.fft import fftfreq, rfftfreq
import time
import numpy as np



def test_wave_generation(duration = 1, sample_rate = 256):
    ''' this function generates a composite wavfe of three random waves of a given sample rate and duration
    '''
    # generate a sine wave with a randome frequency
    frequency_list = [np.random.randint(1, 1000), np.random.randint(1, 1000), np.random.randint(1, 1000)]
    signal_1 = np.sin(2*np.pi*frequency_list[0]*np.arange(sample_rate*duration)/sample_rate)
    signal_2 = np.sin(2*np.pi*frequency_list[1]*np.arange(sample_rate*duration)/sample_rate)
    signal_3 = np.sin(2*np.pi*frequency_list[2]*np.arange(sample_rate*duration)/sample_rate)
    composite_signal = signal_1 + signal_2 + signal_3
    return (composite_signal, frequency_list)


def unit_test_functionality(duration = 1, details = False):
    ''' this function tests the basic functionality of the fourier transform
    '''
    composite_signal, frequency_list= test_wave_generation(duration, sample_rate = 2048)
    fourier_transform = fft(composite_signal)
    inverse_transform = ifft(fourier_transform)


    if details:
        print("test specificaitons:")
        print("  sample rate: " + str(2048) + " per second")
        print("  duration: "+ str(duration)+ " second" if duration == 1 else " seconds")
        print("  number of samples: " + str(len(composite_signal)))
        frequency_list_string = ""
        for x in frequency_list:
            frequency_list_string += str(x) + "hz" + ", "
        print("  frequencies of composite signal (in hz): " + frequency_list_string[:-2])
        print()

    print("unit testing functionality of fourier trandform functions...")

    print("  testing regular fourier transform function... ")

    if test_regular_fourier_transform(composite_signal, fourier_transform):
        print("     passed")
    else:
        print("     failed")
    
    print("  testing fast fourier transform function... ")
    if test_fast_fourier_transform(composite_signal, fourier_transform):
        print("     passed")
    else:
        print("     failed")

    print("  testing inverse regular fourier transform function... ")
    if test_inverse_regular_fourier_transform(fourier_transform, inverse_transform):
        print("     passed")
    else:
        print("     failed")

    print("  testing inverse fast fourier transform function... ")
    if test_inverse_fast_fourier_transform(fourier_transform, inverse_transform):
        print("     passed")
    else:
        print("     failed")



def test_regular_fourier_transform(composite_signal, test_transform):
    ''' this function tests the regular fourier transform function using the scipy fourier transform function
    '''

    home_transform = regular_fourier_transform(composite_signal)
    return np.allclose(test_transform, home_transform)


def test_fast_fourier_transform(composite_signal, test_transform):
    ''' this function tests the fast fourier transform function using the scipy fourier transform function
    '''

    home_transform = fast_fourier_transform(composite_signal)
    return np.allclose(test_transform, home_transform)

    
def test_inverse_regular_fourier_transform(fourier_transform, test_inverse_transform):
    ''' this function tests the inverse regular fourier transform function using the scipy fourier transform function
    '''

    home_transform = inverse_regular_fourier_transform(fourier_transform)
    return np.allclose(test_inverse_transform, home_transform)


def test_inverse_fast_fourier_transform(fourier_transform, test_inverse_transform):
    ''' this function tests the inverse fast fourier transform function using the scipy fourier transform function
    '''

    home_transform = inverse_fast_fourier_transform(fourier_transform)
    return np.allclose(test_inverse_transform, home_transform)


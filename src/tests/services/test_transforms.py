import unittest
from services.transforms import *
from scipy.fft import fft, ifft
import numpy as np

class test_transforms(unittest.TestCase):

    def setUp(self):
        ''' this function is used to set up the test environment
        '''
        duration = 1
        sample_rate = 512
        frequency_list = [np.random.randint(1, sample_rate), np.random.randint(1, sample_rate), np.random.randint(1, sample_rate)]
        signal_1 = np.sin(2*np.pi*frequency_list[0]*np.arange(sample_rate*duration)/sample_rate)
        signal_2 = np.sin(2*np.pi*frequency_list[1]*np.arange(sample_rate*duration)/sample_rate)
        signal_3 = np.sin(2*np.pi*frequency_list[2]*np.arange(sample_rate*duration)/sample_rate)
        composite_signal = signal_1 + signal_2 + signal_3
        self.test_wave = composite_signal
        self.fourier_transform = fft(self.test_wave)
        self.inverse = ifft(self.fourier_transform)

    def test_regular_fourier_transform(self):
        '''this function tests the regular fourier transform function and make sure that all values of the wave match the values in a known fourier transform
        '''
        np.allclose(self.fourier_transform, regular_fourier_transform(self.test_wave))

    def test_fast_fourier_transform(self):
        '''this function test the fast fourier transform function
        '''
        np.allclose(self.fourier_transform, fast_fourier_transform(self.test_wave))

    def test_inverse_regular_fourier_transform(self):
        '''this function test the inverse regular fourier transform function
        '''
        np.allclose(self.inverse, inverse_regular_fourier_transform(self.fourier_transform))
    
    def test_inverse_fast_fourier_transform(self):
        '''this function test the inverse fast fourier transform function
        '''
        np.allclose(self.inverse, inverse_fast_fourier_transform(self.fourier_transform))

    def test_transform_caller(self):
        ''' this function tests the transform caller function
        '''
        fourier_transform, inverse = transform_caller(True, False, 44100, self.test_wave)
        np.allclose(self.fourier_transform, fourier_transform)

if __name__ == '__main__':
    unittest.main()
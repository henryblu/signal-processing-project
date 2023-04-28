import unittest
import numpy as np
from scipy.fft import fft, ifft
from services.transforms import (
    regular_fourier_transform,
    fast_fourier_transform,
    inverse_regular_fourier_transform,
    inverse_fast_fourier_transform,
    transform_caller,
)
from services.data_processing import test_wave_generation


class test_transforms(unittest.TestCase):
    def setUp(self):
        """this function is used to set up the test environment"""
        composite_signal = test_wave_generation()[1]
        self.test_wave = composite_signal
        self.fourier_transform = fft(self.test_wave)
        self.inverse = ifft(self.fourier_transform)

    def test_regular_fourier_transform(self):
        """this function tests the regular fourier transform function and make sure that all values
        of the wave match the values in a known fourier transform
        """
        np.allclose(self.fourier_transform, regular_fourier_transform(self.test_wave))

    def test_fast_fourier_transform(self):
        """this function test the fast fourier transform function"""
        np.allclose(self.fourier_transform, fast_fourier_transform(self.test_wave))

    def test_inverse_regular_fourier_transform(self):
        """this function test the inverse regular fourier transform function"""
        np.allclose(
            self.inverse, inverse_regular_fourier_transform(self.fourier_transform)
        )

    def test_inverse_fast_fourier_transform(self):
        """this function test the inverse fast fourier transform function"""
        np.allclose(
            self.inverse, inverse_fast_fourier_transform(self.fourier_transform)
        )

    def test_transform_caller(self):
        """this function tests the transform caller function"""
        fourier_transform = transform_caller(True, False, self.test_wave)[0]
        np.allclose(self.fourier_transform, fourier_transform)


if __name__ == "__main__":
    unittest.main()

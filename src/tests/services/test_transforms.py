import unittest
import numpy as np
import pytest
from scipy.fft import fft
from services.data_processing import input_checker
from services.transforms import (
    regular_fourier_transform,
    fast_fourier_transform,
    inverse_regular_fourier_transform,
    inverse_fast_fourier_transform,
    transform_caller,
)


class test_transforms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """this function is used to setup the test class the composite wave tests the upper and
        lower bowndaries of a possible wave"""
        super(test_transforms, cls).setUpClass()
        signal_1 = np.sin(2 * np.pi * 1 * np.arange(1024) / 1024)
        signal_2 = np.sin(
            2 * np.pi * np.random.randint(1, 1024) * np.arange(1024) / 1024
        )
        signal_3 = np.sin(2 * np.pi * 1024 * np.arange(1024) / 1024)
        cls.test_waves = signal_1 + signal_2 + signal_3

        cls.test_file = input_checker(r"src/Data/StarWars3.wav", False)[1]

    def test_regular_fourier_transform(self):
        """this function tests the regular fourier transform function and make sure that all values
        of the wave match the values in a known fourier transform
        """
        assert (
            np.allclose(
                fft(self.test_waves), regular_fourier_transform(self.test_waves)
            )
            is True
        )

    def test_fast_fourier_transform(self):
        """this function test the fast fourier transform function"""
        assert (
            np.allclose(fft(self.test_waves), fast_fourier_transform(self.test_waves))
            is True
        )
        with pytest.raises(ValueError, match="size of audio_data must be a power of 2"):
            fast_fourier_transform(self.test_file)

    def test_inverse_regular_fourier_transform(self):
        """this function test the inverse regular fourier transform function"""

        assert (
            np.allclose(
                self.test_waves, inverse_regular_fourier_transform(fft(self.test_waves))
            )
            is True
        )

    def test_inverse_fast_fourier_transform(self):
        """this function test the inverse fast fourier transform function"""
        assert (
            np.allclose(
                self.test_waves, inverse_fast_fourier_transform(fft(self.test_waves))
            )
            is True
        )

    def test_transform_caller(self):
        """this function tests the transform caller function"""
        assert (
            np.allclose(
                fft(self.test_waves), transform_caller(True, False, self.test_waves)[0]
            )
            is True
        )
        assert (
            np.allclose(
                fft(self.test_waves), transform_caller(False, False, self.test_waves)[0]
            )
            is True
        )
        assert (
            np.allclose(
                fft(self.test_waves), transform_caller(False, True, self.test_waves)[0]
            )
            is True
        )
        with pytest.raises(ValueError, match="both rft and fft cannot be true"):
            transform_caller(True, True, self.test_waves)


if __name__ == "__main__":
    unittest.main()

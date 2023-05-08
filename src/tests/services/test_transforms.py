import unittest
import numpy as np
import pytest
from services.transforms import Transforms
from services.sample_wave import SampleWave


class test_transforms(unittest.TestCase):
    """this class tests the transforms class"""

    def setUp(self):
        self.test_file = "src/tests/test_data/test_audio_data.wav"
        self.test_wave_power_2 = SampleWave(
            sample_rate=512
        ).generate_composite_wave()
        self.test_wave_not_power_2 = SampleWave(
            sample_rate=500
        ).generate_composite_wave()
        self.test_fourier_transform = np.fft.fft(self.test_wave_power_2)

    def test_init(self): 
        """this function tests the init function"""
        with pytest.raises(ValueError, match="both rft and fft cannot be true"):
            Transforms(True, True)

    def test_run_transform(self):
        """this function tests the run transform function"""
        t = Transforms(True, False)
        # check that the outputs shape is the same as np.fft.rfft

        assert np.allclose(
            t.run_transform(audio_data=self.test_wave_power_2)[: len(self.test_wave_power_2) // 2 + 1],
            np.fft.rfft(self.test_wave_power_2),
        )

        t = Transforms(False, True)
        assert np.allclose(
            t.run_transform(audio_data=self.test_wave_power_2),
            np.fft.fft(self.test_wave_power_2),
        )


    def test_run_inverse(self):
        """this function tests the run inverse function"""
        t = Transforms(True, False)
        assert np.allclose(
            t.run_inverse(fourier_transform=self.test_fourier_transform),
            np.fft.ifft(self.test_fourier_transform),
        )

        t = Transforms(False, True)
        assert np.allclose(
            t.run_inverse(fourier_transform=self.test_fourier_transform),
            np.fft.ifft(self.test_fourier_transform),
        )
        # make sure the data is only real numbers
        assert np.all(
            np.isreal(t.run_inverse(fourier_transform=self.test_fourier_transform))
        )


if __name__ == "__main__":
    unittest.main()

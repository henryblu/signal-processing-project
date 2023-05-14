import unittest
import numpy as np
import pytest
from src.services.transforms import Transforms
from src.services.sample_wave import SampleWave


class TestTransforms(unittest.TestCase):
    """this class tests the transforms class"""

    def setUp(self):
        self.test_file = "src/tests/test_data/test_audio_data.wav"
        self.test_wave_power_2 = SampleWave(sample_rate=512).generate_composite_wave()
        self.test_wave_not_power_2 = SampleWave(
            sample_rate=500
        ).generate_composite_wave()

    def test_init(self):
        """this function tests the init function"""
        with pytest.raises(ValueError, match="both dft and fft cannot be true"):
            Transforms(True, True)

    def test_run_transform(self):
        """this function tests the run transform function"""
        t = Transforms(True, False, verbose=True)

        assert np.allclose(
            t.run_transform(audio_data=self.test_wave_power_2)[
                : len(self.test_wave_power_2) // 2 + 1
            ],
            np.fft.rfft(self.test_wave_power_2),
        )

        t = Transforms(False, True, verbose=True)
        assert np.allclose(
            t.run_transform(audio_data=self.test_wave_power_2),
            np.fft.fft(self.test_wave_power_2),
        )

        self.assertEqual(
            len(t.run_transform(audio_data=self.test_wave_not_power_2)), 512
        )
        t = Transforms(False, True, verbose=False)

        # make sure the data is only complex numbers exept for the first value whic hshould be 0
        assert np.all(
            np.iscomplex(t.run_transform(audio_data=self.test_wave_not_power_2)[1:])
        )

    def test_run_inverse(self):
        """this function tests the run inverse function"""
        test_fourier_transform = np.fft.fft(self.test_wave_power_2)

        t = Transforms(True, False, verbose=True)
        assert np.allclose(
            t.run_inverse(fourier_transform=test_fourier_transform),
            np.fft.ifft(test_fourier_transform),
        )

        t = Transforms(False, True, verbose=True)
        assert np.allclose(
            t.run_inverse(fourier_transform=test_fourier_transform),
            np.fft.ifft(test_fourier_transform),
        )

        # make sure the data is only real numbers
        assert np.all(
            np.isreal(t.run_inverse(fourier_transform=test_fourier_transform))
        )


if __name__ == "__main__":
    unittest.main()

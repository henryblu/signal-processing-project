import unittest
import numpy as np

from src.services.sample_wave import SampleWave
from src.services.transform_alternations import (
    high_pitch_reduction,
    low_pitch_reduction,
    noise_reduction,
)


class TestTransformAlternations(unittest.TestCase):
    def setUp(self):
        self.sample_wave = SampleWave(sample_rate=20000)
        self.transform = np.fft.fft(self.sample_wave.get_audio_data())

    def test_high_pitch_reduction(self):
        high_pitch_reduction_audio_data = high_pitch_reduction(self.transform, 20000)
        self.assertEqual(high_pitch_reduction_audio_data.shape, self.transform.shape)
        self.assertTrue(np.all(high_pitch_reduction_audio_data == self.transform))

        high_pitch_reduction_audio_data = high_pitch_reduction(self.transform, 10000)
        self.assertEqual(high_pitch_reduction_audio_data.shape, self.transform.shape)
        self.assertTrue(high_pitch_reduction_audio_data[10001] == 0)

    def test_low_pitch_reduction(self):
        low_pitch_reduction_audio_data = low_pitch_reduction(self.transform, 0)
        self.assertEqual(low_pitch_reduction_audio_data.shape, self.transform.shape)
        self.assertTrue(np.all(low_pitch_reduction_audio_data == self.transform))

        low_pitch_reduction_audio_data = low_pitch_reduction(self.transform, 10000)
        self.assertEqual(low_pitch_reduction_audio_data.shape, self.transform.shape)
        self.assertTrue(low_pitch_reduction_audio_data[9999] == 0)

    def test_noise_reduction(self):
        noise_reduction_audio_data = noise_reduction(self.transform, 0)
        self.assertEqual(noise_reduction_audio_data.shape, self.transform.shape)
        self.assertTrue(np.all(noise_reduction_audio_data == self.transform))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

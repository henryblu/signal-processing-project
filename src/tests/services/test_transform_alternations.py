import unittest
import numpy as np

from services.sample_wave import SampleWave
from services.transform_alternations import (
    high_pitch_reduction,
    low_pitch_reduction,
    noise_reduction,
)


class TestTransformAlternations(unittest.TestCase):
    def setUp(self):
        self.sample_wave = SampleWave()
        self.transform = np.fft.fft(self.sample_wave.generate_composite_wave())

    def test_high_pitch_reduction(self):
        high_pitch_reduction_audio_data = high_pitch_reduction(self.transform)
        self.assertEqual(high_pitch_reduction_audio_data.shape, self.transform.shape)
        self.assertTrue(np.all(high_pitch_reduction_audio_data == self.transform))

        high_pitch_reduction_audio_data = high_pitch_reduction(self.transform, 50)
        self.assertEqual(high_pitch_reduction_audio_data.shape, self.transform.shape)
        self.assertTrue(
            high_pitch_reduction_audio_data[int((len(self.transform) / 2) + 1)] == 0
        )

    def test_low_pitch_reduction(self):
        low_pitch_reduction_audio_data = low_pitch_reduction(self.transform)
        self.assertEqual(low_pitch_reduction_audio_data.shape, self.transform.shape)
        self.assertTrue(np.all(low_pitch_reduction_audio_data == self.transform))

        low_pitch_reduction_audio_data = low_pitch_reduction(self.transform, 50)
        self.assertEqual(low_pitch_reduction_audio_data.shape, self.transform.shape)
        self.assertTrue(
            low_pitch_reduction_audio_data[int((len(self.transform) / 2) - 1)] == 0
        )

    def test_noise_reduction(self):
        noise_reduction_audio_data = noise_reduction(self.transform)
        self.assertEqual(noise_reduction_audio_data.shape, self.transform.shape)
        self.assertTrue(np.all(noise_reduction_audio_data == self.transform))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
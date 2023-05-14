import unittest
import pytest
import numpy as np
from scipy.io import wavfile as wav
from src.services.sample_wave import SampleWave


class TestSampleWave(unittest.TestCase):
    def setUp(self):
        self.sample_wave = SampleWave(verbose=True)

    def test_get_audio_data(self):
        np.allclose(self.sample_wave.get_audio_data(), self.sample_wave.audio_data)

    def test_get_sample_rate(self):
        self.assertEqual(
            self.sample_wave.get_sample_rate(), self.sample_wave.sample_rate
        )

    def test_generate_composite_wave(self):
        self.assertEqual(
            self.sample_wave.get_audio_data().shape,
            (self.sample_wave.sample_rate * self.sample_wave.duration,),
        )

    def test_add_noise(self):
        noisy_audio_data = self.sample_wave.add_noise(
            5, self.sample_wave.get_audio_data()
        )
        self.assertEqual(
            noisy_audio_data.shape, self.sample_wave.get_audio_data().shape
        )

    def test_output(self):
        self.sample_wave.output(
            self.sample_wave.get_audio_data(), r"src/tests/Data/test_output.wav"
        )
        file_data = wav.read(r"src/tests/Data/test_output.wav")[1]
        self.assertEqual(file_data.shape, self.sample_wave.get_audio_data().shape)
        np.allclose(file_data, self.sample_wave.get_audio_data())

        with pytest.raises(
            FileNotFoundError, match="The specified output path does not exist."
        ):
            self.sample_wave.output(
                self.sample_wave.get_audio_data(), r"spc/sql/no_work/please.wav"
            )

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

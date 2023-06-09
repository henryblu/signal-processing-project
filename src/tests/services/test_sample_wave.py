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

    def test_set_audio_data(self):
        self.sample_wave.set_audio_data(np.array([1, 2, 3]))
        self.assertTrue(
            np.all(self.sample_wave.get_audio_data() == np.array([1, 2, 3]))
        )

    def test_get_sample_rate(self):
        self.assertEqual(
            self.sample_wave.get_sample_rate(), self.sample_wave.sample_rate
        )

    def test_generate_composite_wave(self):
        self.assertEqual(
            self.sample_wave.get_audio_data().shape,
            (self.sample_wave.sample_rate * self.sample_wave.duration,),
        )

    def test_output(self):
        self.sample_wave.output(r"src/tests/Data/test_output.wav")
        file_data = wav.read(r"src/tests/Data/test_output.wav")[1]
        self.assertEqual(file_data.shape, self.sample_wave.get_audio_data().shape)
        np.allclose(file_data, self.sample_wave.get_audio_data())

        with pytest.raises(
            FileNotFoundError, match="The specified output path does not exist."
        ):
            self.sample_wave.output(r"spc/sql/no_work/please.wav")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

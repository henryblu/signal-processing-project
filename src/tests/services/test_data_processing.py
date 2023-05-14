import unittest
import pytest
import numpy as np
from scipy.io import wavfile as wav
from src.services.audio_file_wave import AudioWave


class TestAudioFileProcessing(unittest.TestCase):
    def setUp(self):
        with pytest.raises(ValueError, match="input file must be a .wav file"):
            self.audio_file_processing = AudioWave(input_file=r"no_work")

        with pytest.raises(FileNotFoundError, match="input file not found"):
            self.audio_file_processing = AudioWave(input_file=r"no_work.wav")

        with pytest.raises(ValueError, match="input file is too long"):
            self.audio_file_processing = AudioWave(
                input_file=r"src/tests/Data/StarWars60.wav"
            )

        self.audio_file_processing = AudioWave(
            input_file=r"src/Data/StarWars3.wav", verbose=True
        )
        self.assertIsInstance(self.audio_file_processing.noise_level, float)
        self.assertIsInstance(self.audio_file_processing.audio_data, np.ndarray)

    def test_get_audio_data(self):
        self.assertIsInstance(self.audio_file_processing.get_audio_data(), np.ndarray)

    def test_set_audio_data(self):
        self.audio_file_processing.set_audio_data(self.audio_file_processing.audio_data)
        self.assertTrue(
            len(self.audio_file_processing.get_audio_data())
            == self.audio_file_processing.length
        )

    def test_get_sample_rate(self):
        self.assertIsInstance(self.audio_file_processing.get_sample_rate(), int)

    def test_data_triming(self):
        self.assertIsInstance(self.audio_file_processing.front_trim, int)
        self.assertIsInstance(self.audio_file_processing.back_trim, int)

    def test_output(self):
        wav.write(r"src/tests/Data/test_output.wav", 0, np.zeros((1,)))

        self.audio_file_processing.output(r"src/tests/Data/test_output.wav")
        np.allclose(
            self.audio_file_processing.get_audio_data(),
            wav.read(r"src/tests/Data/test_output.wav")[1][:59168],
        )

        self.audio_file_processing = AudioWave(
            input_file=r"src/Data/StarWars3.wav", verbose=True
        )

        with pytest.raises(
            FileNotFoundError, match="The specified output path does not exist."
        ):
            self.audio_file_processing.output(r"spc/sql/no_work/please.wav")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

import unittest
import numpy as np
from scipy.io import wavfile as wav
from services.data_processing import AudioFileProcessing


class TestAudioFileProcessing(unittest.TestCase):
    def setUp(self):
        self.audio_file_processing = AudioFileProcessing(
            input_file=r"src\Data\StarWars3.wav", verbose=True
        )
        self.assertIsInstance(self.audio_file_processing.noise_level, float)
        self.assertIsInstance(self.audio_file_processing.audio_data, np.ndarray)

    def test_get_audio_data(self):
        self.assertIsInstance(self.audio_file_processing.get_audio_data(), np.ndarray)

    def test_get_sample_rate(self):
        self.assertIsInstance(self.audio_file_processing.get_sample_rate(), int)

    def test_data_triming(self):
        self.audio_file_processing.data_triming()
        self.assertIsInstance(self.audio_file_processing.front_trim, int)
        self.assertIsInstance(self.audio_file_processing.back_trim, int)


    def test_output(self):
        # clear the output file located at src\Data\output.wav
        wav.write(r"src\Data\output.wav", 0, np.zeros((1,)))
        sound_wave = self.audio_file_processing.get_audio_data()
        self.audio_file_processing.output(sound_wave)
        np.allclose(
            self.audio_file_processing.get_audio_data(),
            wav.read(r"src\Data\output.wav")[1],
        )

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

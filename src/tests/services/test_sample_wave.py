import unittest
import numpy as np
from scipy.io import wavfile as wav
from services.sample_wave import SampleWave


class TestSampleWave(unittest.TestCase):
    def setUp(self):
        self.sample_wave = SampleWave()

    def test_generate_composite_wave(self):
        audio_data = self.sample_wave.generate_composite_wave()
        self.assertEqual(
            audio_data.shape,
            (self.sample_wave.sample_rate * self.sample_wave.duration,),
        )

    def test_add_noise(self):
        audio_data = self.sample_wave.generate_composite_wave()
        noisy_audio_data = self.sample_wave.add_noise(0.5, audio_data)
        self.assertEqual(noisy_audio_data.shape, audio_data.shape)

    def test_output(self):
        audio_data = self.sample_wave.generate_composite_wave()
        output_file = "src/tests/Data/test_output.wav"
        self.sample_wave.output(audio_data, output_file)
        _, read_audio_data = wav.read(output_file)
        self.assertEqual(read_audio_data.shape, audio_data.shape)
        self.assertTrue(np.all(read_audio_data == audio_data))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

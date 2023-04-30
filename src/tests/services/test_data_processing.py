import unittest
from services.data_processing import (
    input_checker,
    sample_wave_generation,
    get_data,
    output,
)


class test_data_processing(unittest.TestCase):
    def test_input_checker(self):
        """test that the input_checker function returns the correct sample rate and data"""
        sample_rate, data = input_checker(r"data\StarWars3.wav")
        self.assertEqual(sample_rate, 22050)
        self.assertEqual(len(data), 66150)

        sample_rate, data = input_checker(None)
        self.assertEqual(sample_rate, 512)
        self.assertEqual(len(data), 512)

    def test_get_data(self):
        """test that the get_data function returns the correct sample rate and data"""
        sample_rate, data = get_data((r"data\StarWars3.wav"))
        self.assertEqual(sample_rate, 22050)
        self.assertEqual(len(data), 66150)

    def test_test_wave_generation(self):
        """test that the test_wave_generation function returns the correct sample rate and data"""
        sample_rate, data = sample_wave_generation()
        self.assertEqual(sample_rate, 512)
        self.assertEqual(len(data), 512)

    def test_output(self):
        """test that the output function returns the correct sample rate and data"""
        sample_rate, data = input_checker(r"data\StarWars3.wav")
        output(
            sample_rate,
            data,
            r"data\StarWars3.wav",
        )

        sample_rate, data = get_data(r"data\StarWars3.wav")
        self.assertEqual(sample_rate, 22050)
        self.assertEqual(len(data), 66150)


if __name__ == "__main__":
    unittest.main()

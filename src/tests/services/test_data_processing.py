import unittest
import pytest
import io
from contextlib import redirect_stdout
from services.data_processing import (
    input_checker,
    sample_wave_generation,
    get_data,
    output,
)


class test_data_processing(unittest.TestCase):
    def test_input_checker(self):
        """test that the input_checker function returns the correct sample rate and data"""
        sample_rate, data = input_checker(r"src/Data/StarWars3.wav")
        self.assertEqual(sample_rate, 22050)
        self.assertEqual(len(data), 66150)

        sample_rate, data = input_checker(None)
        self.assertEqual(sample_rate, 512)
        self.assertEqual(len(data), 512)

        with pytest.raises(ValueError, match="input file must be a .wav file"):
            sample_rate, data = input_checker("test")

    def test_test_wave_generation(self):
        """test that the test_wave_generation function returns the correct sample rate and data"""
        with io.StringIO() as buf, redirect_stdout(buf):
            sample_rate, data = sample_wave_generation(verbose=True)
            print_output = buf.getvalue()
            print(print_output)
            self.assertIn(
                "no file specified, generating random composite wave of 3 frequencies",
                print_output,
            )
            self.assertIn("wave specification", print_output)
            self.assertIn("duration of wave: 1 seconds", print_output)
            self.assertIn("sample rate: 512 samples per second", print_output)
            self.assertIn("frequencies of composite signal (in hz):", print_output)
            self.assertEqual(sample_rate, 512)
            self.assertEqual(len(data), 512)

    def test_get_data(self):
        """test that the get_data function returns the correct sample rate and data"""
        sample_rate, data = get_data((r"src/Data/StarWars3.wav"))
        self.assertEqual(sample_rate, 22050)
        self.assertEqual(len(data), 66150)
        with pytest.raises(FileNotFoundError, match="input file not found"):
            sample_rate, data = get_data("serasdfg/safdsadf/p.wav")

    def test_output(self):
        """test that the output function returns the correct sample rate and data"""
        sample_rate, data = input_checker(r"src/Data/StarWars3.wav")
        output(
            sample_rate,
            data,
            r"src/Data/StarWars3.wav",
        )
        output(
            sample_rate,
            data,
            None,
        )
        output(
            sample_rate,
            data,
            r"src/dataaaaaa/test.wav",
        )


if __name__ == "__main__":
    unittest.main()

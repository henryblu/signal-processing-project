import unittest

import sys
import os
sys.path.append(os.path.abspath('..'))
import data_processing as DataProcessing

class test_data_processing(unittest.TestCase):
    def test_input_checker(self):
        ''' test that the input_checker function returns the correct sample rate and data
        '''
        sample_rate, data = DataProcessing.input_checker(r"C:\Users\henry\OneDrive - University of Helsinki\Documents\University files\Comp sci\year 2\data structures and algoithms project course\signal-processing-project\main\Data\StarWars3.wav")
        self.assertEqual(sample_rate, 22050)
        self.assertEqual(len(data), 66150)

        sample_rate, data = DataProcessing.input_checker(None)
        self.assertEqual(sample_rate, 512)
        self.assertEqual(len(data), 512)

    def test_get_data(self):
        ''' test that the get_data function returns the correct sample rate and data
        '''
        sample_rate, data = DataProcessing.get_data(r"C:\Users\henry\OneDrive - University of Helsinki\Documents\University files\Comp sci\year 2\data structures and algoithms project course\signal-processing-project\main\Data\StarWars3.wav")
        self.assertEqual(sample_rate, 22050)
        self.assertEqual(len(data), 66150)

    def test_test_wave_generation(self):
        ''' test that the test_wave_generation function returns the correct sample rate and data
        '''
        sample_rate, data = DataProcessing.test_wave_generation()
        self.assertEqual(sample_rate, 512)
        self.assertEqual(len(data), 512)

    def test_output(self):
        ''' test that the output function returns the correct sample rate and data
        '''
        sample_rate, data = DataProcessing.input_checker(r"C:\Users\henry\OneDrive - University of Helsinki\Documents\University files\Comp sci\year 2\data structures and algoithms project course\signal-processing-project\main\Data\StarWars3.wav")
        DataProcessing.output(sample_rate, data, r"C:\Users\henry\OneDrive - University of Helsinki\Documents\University files\Comp sci\year 2\data structures and algoithms project course\signal-processing-project\main\Data\output.wav")

        sample_rate, data = DataProcessing.get_data(r"C:\Users\henry\OneDrive - University of Helsinki\Documents\University files\Comp sci\year 2\data structures and algoithms project course\signal-processing-project\main\Data\StarWars3.wav")
        self.assertEqual(sample_rate, 22050)
        self.assertEqual(len(data), 66150)

if __name__ == '__main__':
    unittest.main()
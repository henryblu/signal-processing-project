import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
import main

class test_main(unittest.TestCase):
    def test_flags_finder(self):
        ''' test that the flags_finder function returns the correct flags
        '''
        flags = main.flags_finder()
        self.assertEqual(flags.helper, False)
        self.assertEqual(flags.input, None)
        self.assertEqual(flags.output, None)
        self.assertEqual(flags.performance_test, 0)
        self.assertEqual(flags.fast_fourier_transform, False)
        self.assertEqual(flags.regular_fourier_transform, False)



if __name__ == '__main__':
    unittest.main()
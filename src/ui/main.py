import argparse
from services.data_processing import *
from visualisations import *
from services.transforms import *
from services.noise_reduction import *
from tests.performance_test import *

def print_help():
    # prints the help message
    print(
        """
        Currently, this program can be used to test the functionality of two types of fourier and inverse fourier transforms.

        current limitations:
        - the program can only read .wav files
        - the program can only write to .csv files
        - the flag --details which prints a detailed output of the algrithm including time taken and memory taken is not yet implemented (if you want to see time taken and memory taken for a test wave you can use the --test_with_details flag)
        - the flag --threadshold which specifies the threadshold level for the noise reduction, default is 0 is not yet implemented (as the noise reduction algorithm is not yet implemented)
        """
    ) 

def flags_finder(performance_test = 0, ):
    # Parse command line arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--helper", help="prints a more detailed help message", action="store_true")
    parser.add_argument("-i", "--input", help="specifies the .wav sound wave file to be read. Default is sound wave provided")
    parser.add_argument("-o", "--output", help="specifies the file to be written to default is output.csv")
    #parser.add_argument("-d", "--details", help="prints the details of the algrithm including time taken and memory taken", action="store_true")
    parser.add_argument("-fft", "--fast_fourier_transform", help="performs a fast fourier transform on the data", action="store_true")
    parser.add_argument("-rft", "--regular_fourier_transform", help="performs a regular fourier transform on the data", action="store_true")
    parser.add_argument("-p", "--performance_test", help="prints the details of the test suite including time taken and memory taken. You may input a positive integer to specify number of tests you want to run", type=int, default=0)
    parser.add_argument("-v", "--verbose", help="prints the details what is happening in the program", action="store_true")
    #parser.add_argument("-th", "--threadshold", help="specifies the threadshold level for the noise reduction, default is 0", type=int, default=0)
    args = parser.parse_args()

    if args.helper:
        print_help()
        return

    return args


def main():
    # first we look for all the flags that have been set 
    flags = flags_finder()

    if flags.performance_test != 0:
        p_test = performance_test(samples = flags.performance_test, verbose = flags.verbose)
        p_test.run()
        return
    
    sample_rate, composite_signal = input_checker(flags.input, flags.verbose)
    fourier_transform, inverse = transform_caller(flags.regular_fourier_transform, flags.fast_fourier_transform, sample_rate, composite_signal)
    plot_all(sample_rate, composite_signal, inverse, fourier_transform)

    if flags.output != None:
        #note that atm this should output the same soundwave as the input
        output(flags.output, inverse)
    
    return


if __name__ == "__main__":
    main()
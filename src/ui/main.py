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
        - the program can only read and write to .wav files
        - the program can only write to .csv files
        - unit tests must be run one by one

        """
    ) 

def flags_finder(performance_test = 0, ):
    ''' this function is used to find all the flags that have been set.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--helper", help="prints a help message on the current state of the project", action="store_true")
    parser.add_argument("-i", "--input", help="specifies the .wav sound wave file to be read. Default is randomly generated sound wave")
    parser.add_argument("-o", "--output", help="specifies the file to be written to default is ./data/output.csv")
    parser.add_argument("-v", "--verbose", help="prints the details of the algrithm including time taken and memory taken", action="store_true")
    parser.add_argument("-r", "--regular_fourier_transform", help="specifies the regular fourier transform to be used", action="store_true")
    parser.add_argument("-f", "--fast_fourier_transform", help="specifies the fast fourier transform to be used", action="store_true")
    parser.add_argument("-t", "--performance_test", help="specifies the number of samples to be used in the performance test. Default is 0", type=int, default=0)
    args = parser.parse_args()

    if args.helper:
        print_help()
        return

    return args


def main():
    ''' This function is the main function of the program it is used to call all the other functions
    '''
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
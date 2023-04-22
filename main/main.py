import argparse
from data_processing import *
from visualisations import *
from transforms import *
from noise_reduction import *
from tests.performance_test import *
from scipy import fftpack



def print_help():
    # prints the help message
    print(
        """
        Currently, this program can be used to test the functionality of two types of fourier and inverse fourier transforms.

        Flags:
        -H, --helper: prints the help message
        -i, --input: specifies the .wav sound wave file to be read. Default is sound wave provided
        -o, --output: specifies the file to be written to default is output.csv
        -dft, --regular_fourier_transform: performs a regular fourier transform on the data
        -fft, --fast_fourier_transform: performs a fast fourier transform on the data
        -t, --test: runs the basic test suite. You may input a positive integer to specify number of tests you want to run 
        -twd, --test_with_details: prints the details of the test suite including time taken and memory taken. You may input a positive integer to specify number of tests you want to run
        
        current limitations:
        - the program can only read .wav files
        - the program can only write to .csv files
        - the flag --details which prints a detailed output of the algrithm including time taken and memory taken is not yet implemented (if you want to see time taken and memory taken for a test wave you can use the --test_with_details flag)
        - the flag --threadshold which specifies the threadshold level for the noise reduction, default is 0 is not yet implemented (as the noise reduction algorithm is not yet implemented)
        """
    ) 

def flags_finder():
    # Parse command line arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--helper", help="prints a more detailed help message", action="store_true")
    parser.add_argument("-i", "--input", help="specifies the .wav sound wave file to be read. Default is sound wave provided")
    parser.add_argument("-o", "--output", help="specifies the file to be written to default is output.csv")
    #parser.add_argument("-d", "--details", help="prints the details of the algrithm including time taken and memory taken", action="store_true")
    parser.add_argument("-fft", "--fast_fourier_transform", help="performs a fast fourier transform on the data", action="store_true")
    parser.add_argument("-rft", "--regular_fourier_transform", help="performs a regular fourier transform on the data", action="store_true")
    parser.add_argument("-t", "--performance_test", help="runs the basic test suite. You may input a positive integer to specify number of tests you want to run", type=int, default=0)
    parser.add_argument("-twd", "--performance_test_with_details", help="prints the details of the test suite including time taken and memory taken. You may input a positive integer to specify number of tests you want to run", type=int, default=0)
    #parser.add_argument("-th", "--threadshold", help="specifies the threadshold level for the noise reduction, default is 0", type=int, default=0)
    args = parser.parse_args()

    if args.helper:
        print_help()
        return

    return args

def perfromance_test_caller(flags):
    ''' this function is used to call the appropreate test suite when a test flag is set
    '''
    if flags.performance_test != 0 or flags.performance_test_with_details != 0:
            perfromance_test_caller(flags.performance_test, flags.performance_test_with_details)
            return

    test = flags.performance_test
    test_with_details = flags.performance_test_with_details
    print("Running the test suite")

    if test != 0 & test_with_details != 0:
        print("You may only run one test suite at a time")
        exit


    if test != 0 :
        test_suite = performance_test(samples = test)

    elif test_with_details != 0:
        test_suite = performance_test(samples = test_with_details, details = True)

    # request input for algorithm to test
    while True:
        imput = input("Please enter the algorithm you would like to test (options:'rft', 'fft', 'irft', 'ifft', 'all'): ")
        print()
        if imput == "rft":
            test_suite.rft_test()
            return
        elif imput == "fft":
            test_suite.fft_test()
            return
        elif imput == "irft":
            test_suite.irft_test()
            return
        elif imput == "ifft":
            test_suite.ifft_test()
            return
        elif imput == "all":
            
            test_suite.fft_test()
            print()
            test_suite.rft_test()
            print()
            test_suite.ifft_test()
            print()
            test_suite.irft_test()
            return
        else:
            print("Invalid input")

def transform_caller(flags, sample_rate, composite_signal):
    '''  this function is used to call the appropreate transform 
    '''
    if flags.regular_fourier_transform and flags.fast_fourier_transform:
        print("You may only select one fourier transform")
        return

    elif flags.regular_fourier_transform:
        fourier_transform = regular_fourier_transform(composite_signal)
        inverse = inverse_regular_fourier_transform(fourier_transform)
    elif flags.fast_fourier_transform:
        fourier_transform = fast_fourier_transform(composite_signal)
        inverse = inverse_fast_fourier_transform(fourier_transform)
    else:
        print("no fourier transform selected")
        print("defaulting to fast fourier transform")
        fourier_transform = fast_fourier_transform(composite_signal)
        inverse = inverse_fast_fourier_transform(fourier_transform)
    
    return fourier_transform, inverse

def input_checker(flags):
    ''' this function is used to check if the input is valid
    '''
    if flags.input != None:
        if flags.input[-4:] != ".wav":
            print("Invalid input file type")
            exit
        else:
            sample_rate, composite_signal = get_data(flags.input)
    else:
        sample_rate, composite_signal = test_wave_generation()

    return sample_rate, composite_signal

def main():
    # first we look for all the flags that have been set 
    flags = flags_finder()

    perfromance_test_caller(flags)        

    sample_rate, composite_signal = input_checker(flags)
    fourier_transform, inverse = transform_caller(flags, sample_rate, composite_signal)

    
    plot_all(sample_rate, composite_signal, inverse, fourier_transform)

    if flags.output != None:
        #note that atm this should output the same soundwave as the input
        output(flags.output, inverse)


if __name__ == "__main__":
    main()
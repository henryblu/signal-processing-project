import argparse
from data_processing import *
from visualisations import *
from fourier import *
from noise_reduction import *
from tests.test_transforms import *
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
    parser.add_argument("-H", "--helper", help="prints the help message", action="store_true")
    parser.add_argument("-i", "--input", help="specifies the .wav sound wave file to be read. Default is sound wave provided")
    parser.add_argument("-o", "--output", help="specifies the file to be written to default is output.csv")
    parser.add_argument("-d", "--details", help="prints the details of the algrithm including time taken and memory taken", action="store_true")
    parser.add_argument("-fft", "--fast_fourier_transform", help="performs a fast fourier transform on the data", action="store_true")
    parser.add_argument("-rft", "--regular_fourier_transform", help="performs a regular fourier transform on the data", action="store_true")
    parser.add_argument("-t", "--test", help="runs the basic test suite. You may input a positive integer to specify number of tests you want to run", type=int, default=0)
    parser.add_argument("-twd", "--test_with_details", help="prints the details of the test suite including time taken and memory taken. You may input a positive integer to specify number of tests you want to run", type=int, default=0)
    parser.add_argument("-th", "--threadshold", help="specifies the threadshold level for the noise reduction, default is 0", type=int, default=0)
    args = parser.parse_args()

    if args.helper:
        print_help()
        return

    return args

def test_caller(test = 0, test_with_details = 0):
    ''' this function is used to call the appropreate test suite when a test flag is set
    '''
    
    print("Running the test suite")

    if test != 0 & test_with_details != 0:
        print("You may only run one test suite at a time")
        exit


    if test != 0 :
        test_suite = unit_test(samples = test)

    elif test_with_details != 0:
        test_suite = unit_test(samples = test_with_details, details = True)

    # request input for algorithm to test
    while True:
        imput = input("Please enter the algorithm you would like to test (options:'rft', 'fft', 'irft', 'ifft', 'all'): ")
        if imput == "rft":
            test_suite.rft_test()
            exit
        elif imput == "fft":
            test_suite.fft_test()
            exit
        elif imput == "irft":
            test_suite.irft_test()
            exit
        elif imput == "ifft":
            test_suite.ifft_test()
            exit
        elif imput == "all":
            test_suite.fft_test()
            test_suite.rft_test()
            test_suite.ifft_test()
            test_suite.irft_test()
            exit
        else:
            print("Invalid input")

def main():
    # first we look for all the flags that have been set 
    flags = flags_finder()

    if flags.test != 0 or flags.test_with_details != 0:
        test_caller(flags.test, flags.test_with_details)

    if flags.input == None:
        sample_rate, composite_signal = test_wave_generation()
    else:
        try:
            sample_rate, composite_signal = get_data(flags.input)
        except TypeError:
            print("file not found")
            exit
    
    if flags.regular_fourier_transform and flags.fast_fourier_transform:
        print("You may only select one fourier transform")
        exit

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

    
    plot_all(sample_rate, composite_signal, inverse, fourier_transform)

    if flags.output != None:
        #note that atm this should output the same soundwave as the input
        output(flags.output, inverse)




if __name__ == "__main__":
    main()
import argparse
import os
import sys

# this is used to import the modules from the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.data_processing import input_checker, output
from services.transforms import transform_caller
from ui.visualisations import plot_all
from tests.performance_test import performance_test


def flags_finder():
    """this function is used to find all the flags that have been set.

    Returns:
        list[int]: a list of all the flags that have been set
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        help="specifies the .wav sound wave file to be read. "
        + "Default is randomly generated sound wave",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="specifies the file to be written to default is ./data/output.csv",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="prints the details of the algrithm including time taken and memory taken",
        action="store_true",
    )
    parser.add_argument(
        "-r",
        "--regular_fourier_transform",
        help="specifies the regular fourier transform to be used",
        action="store_true",
    )
    parser.add_argument(
        "-f",
        "--fast_fourier_transform",
        help="specifies the fast fourier transform to be used",
        action="store_true",
    )
    parser.add_argument(
        "-t",
        "--performance_test",
        help="specifies the number of samples to be used in the performance test. Default is 0",
        type=int,
        default=0,
    )
    args = parser.parse_args()
    return args


def main():
    """This function is the main function of the program it is used to call all the other
    functions"""
    flags = flags_finder()
    print(flags)

    if flags.performance_test != 0:
        p_test = performance_test(samples=flags.performance_test, verbose=flags.verbose)
        p_test.run()
        return

    sample_rate, composite_signal = input_checker(flags.input, flags.verbose)
    
    og_fourier, nr_fourier, nr_signal = transform_caller(
        flags.regular_fourier_transform,
        flags.fast_fourier_transform,
        composite_signal,
    )

    plot_all(
        sample_rate,
        composite_signal,
        og_fourier,
        nr_fourier,
        nr_signal,
    )

    if flags.output is not None:
        # note that atm this should output the same soundwave as the input
        output(sample_rate, nr_signal, flags.output)

    return


if __name__ == "__main__":
    main()

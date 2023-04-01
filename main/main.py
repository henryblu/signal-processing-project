import argparse
from data_processing import get_data

def print_help():
    print(
        """
        This program performs simple noise reduction on a given sound wave.

        Flags:
        -h, --help: Prints this help message.
        -f, --file: [optional] Specifies the sound wave file to be read default is sound wave provided.
        -o, --output: [optional] Specifies the file to be written to default is output.csv
        -F, --fourier: [optional] shows the fourier transform of the sound wave as a graph
        -t, --test [optional] runs the test suite
        """
    ) 
def flags_finder():
    # Parse command line arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--helper", help="prints the help message", action="store_true")
    parser.add_argument("-f", "--file", help="specifies the sound wave file to be read default is sound wave provided")
    parser.add_argument("-o", "--output", help="specifies the file to be written to default is output.csv")
    parser.add_argument("-F", "--fourier", help="shows the fourier transform of the sound wave as a graph", action="store_true")
    parser.add_argument("-t", "--test", help="runs the  test suite", action="store_true")
    args = parser.parse_args()

    if args.helper:
        print_help()
        return

    return args


    
def main():
    # first we look for all the flags that have been set 
    flags = flags_finder()
    # now we load the load the sound wave file
    try:
        sample_rate, audio_data = get_data(flags.file)
    except TypeError:
        print("file not found")
        exit

    # now we grpah the sound wave
    




if __name__ == "__main__":
    main()
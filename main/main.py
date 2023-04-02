import argparse
from data_processing import get_data
from visualisations import *
from Fourier import *

def print_help():
    # prints the help message
    print(
        """
        This program performs simple noise reduction on a given sound wave.

        Flags:
        -H, --helper: Prints this help message.
        -i, --input: [optional] specifies the .wav sound wave file to be read. Default is sound wave provided.
        -o, --output: [optional] Specifies the file to be written to default is output.csv
        -fft, --fast_fourier_transform: [optional] performs a fast fourier transform on the data
        -dft, --discrete_fourier_transform: [optional] performs a discrete fourier transform on the data
        -t, --test [optional] runs the test suite
        """
    ) 
def flags_finder():
    # Parse command line arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--helper", help="prints the help message", action="store_true")
    parser.add_argument("-i", "--input", help="specifies the .wav sound wave file to be read. Default is sound wave provided")
    parser.add_argument("-o", "--output", help="specifies the file to be written to default is output.csv")
    parser.add_argument("-fft", "--fast_fourier_transform", help="performs a fast fourier transform on the data", action="store_true")
    parser.add_argument("-dft", "--discrete_fourier_transform", help="performs a discrete fourier transform on the data", action="store_true")
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
        sample_rate, audio_data = get_data(flags.input)
    except TypeError:
        print("file not found")
        exit
    # now we grpah the sound wave
    plot_sound_wave(sample_rate, audio_data)
    
    # now we perform the fourier transform or fast fourier transform on the wave
    if flags.discrete_fourier_transform:
        fourier_transform = discrete_fourier_transform(audio_data)
    elif flags.fast_fourier_transform:
        fourier_transform = fast_fourier_transform(audio_data)
    else: 
        # for testing purposes we will use the fast fourier transform for now
        # the discrete fourier transform is working but it is very slow
        fourier_transform = fast_fourier_transform(audio_data)

    '''
    else: 
        print("no fourier transform selected")
        exit
    '''


    # now we plot the fourier transform if the flag is set
    plot_fourier_transform(fourier_transform)

    # now we perform noise reduction on the fourier transform
        # this it to be implemented

    # now we transform the fourier transform back into a sound wave using the inverse fourier transform
    new_audio_data = inverse_fast_fourier_transform(fourier_transform)

    # now we plot the new sound wave
    plot_sound_wave(sample_rate, new_audio_data)



    



if __name__ == "__main__":
    main()
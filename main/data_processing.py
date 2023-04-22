import numpy as np
from scipy.io import wavfile as wav

def input_checker(file, verbose = False):
    ''' this function is used to check if the input is valid
    '''
    if file != None:
        if file[-4:] != ".wav":
            print("Invalid input file type")
            exit
        else:
            sample_rate, composite_signal = get_data(file)
    else:
        sample_rate, composite_signal = test_wave_generation(verbose = verbose)

    return sample_rate, composite_signal

def test_wave_generation(duration = 1, sample_rate = 512, verbose = False):
    ''' this function generates a composite wavfe of three random waves of a given sample rate and duration
    '''
    if verbose:
        print()
        print("no file specified, generating random composite wave of 3 frequencies")

    # generate a sine wave with a randome frequency
    frequency_list = [np.random.randint(1, sample_rate), np.random.randint(1, sample_rate), np.random.randint(1, sample_rate)]
    signal_1 = np.sin(2*np.pi*frequency_list[0]*np.arange(sample_rate*duration)/sample_rate)
    signal_2 = np.sin(2*np.pi*frequency_list[1]*np.arange(sample_rate*duration)/sample_rate)
    signal_3 = np.sin(2*np.pi*frequency_list[2]*np.arange(sample_rate*duration)/sample_rate)
    composite_signal = signal_1 + signal_2 + signal_3
    
    if verbose:
        print()
        print('wave specifications: ')
        print('    duration of wave: ' + str(duration) + ' seconds')
        print('    sample rate: ' + str(sample_rate) + ' samples per second')

        print("    frequencies of composite signal (in hz): " + ", ".join([str(x) + "hz" for x in frequency_list]))
        print()
    
    return (sample_rate, composite_signal)

def get_data(audio_file_path):
    ''' this function is used to convert the audiofile to a numpy array
    '''
    try:
        sample_rate, audio_data = wav.read(audio_file_path)
    except FileNotFoundError:
        print("input path not found")
        exit
    
    return (sample_rate, np.array(audio_data))

def output(sample_rate, new_sound_wave, output_file_path):
    ''' this function is used to output the new sound wave to a file with default path: main\Data\output.wav
    '''
    # not working right now 
    
    if(output_file_path == None):
        # if no file is specified then we use the default file this try exept is a workaround for the fact that the file is in a different location when running the tests and debugging
        try:
            wav.write("main\Data\output.wav", sample_rate, new_sound_wave)
        except FileNotFoundError: 
            wav.write("Data\output.wav", sample_rate, new_sound_wave)

    else:
        try:
            wav.write(output_file_path, sample_rate, new_sound_wave)
        except FileNotFoundError: 
            print("output path not found")
            exit

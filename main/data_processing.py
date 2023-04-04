import numpy as np
from scipy.io import wavfile as wav

def get_data(audio_file_path):
    ''' this function is used to convert the audiofile to a numpy array
            for now this only works with .wav files
    '''
    if not audio_file_path:
        # if no file is specified then we use the default file this try exept is a workaround for the fact that the file is in a different location when running the tests and debugging
        try:
            sample_rate, audio_data = wav.read("main\Data\StarWars3.wav")
        except FileNotFoundError: 
            sample_rate, audio_data = wav.read("Data\StarWars3.wav")

    else:
        try:
            sample_rate, audio_data = wav.read(audio_file_path)
        except FileNotFoundError: return None
    return (sample_rate, np.array(audio_data))

def output(sample_rate,new_sound_wave, output_file_path):
    ''' this function is used to output the new sound wave to a file with default path: main\Data\output.wav
    '''
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

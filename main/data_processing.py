import numpy as np
from scipy.io import wavfile as wav

def get_data(audio_file_path):
    ''' this function is used to convert the audiofile to a numpy array
            for now this only works with .wav files
    '''
    if not audio_file_path:
        sample_rate, audio_data = wav.read('main\Data\StarWars3.wav')
    else:
        try:
            sample_rate, audio_data = wav.read(audio_file_path)
        except FileNotFoundError: return None
    return (sample_rate, np.array(audio_data))





import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



def plot_sound_wave(sample_rate, audio_data):
    ''' this function plots a given sound wave using its sample rate and the audio data. 
    '''

    time = np.linspace(0, len(audio_data)/sample_rate, num=len(audio_data))
    plt.plot(time, audio_data)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Sound Wave")
    plt.show()
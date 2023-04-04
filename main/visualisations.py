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

def plot_fourier_transform(fourier_transform):
    ''' this function plots the fourier transform of a given audio data
    '''
    plt.plot(fourier_transform)
    plt.xlabel("Frequency (hz)")
    plt.ylabel("Amplitude")
    plt.title("Fourier Transform")
    plt.show()

def plot_all(sample_rate, og_audio_data, transformed_audio_data, fourier_transform):
    ''' this function plots the original sound wave, the transformed sound wave and the fourier transform side by side
    '''
    fig, axs = plt.subplots(3, 1)
    fig.subplots_adjust(hspace=.5)
    #and we increase the size of each subplot
    fig.set_figheight(10)
    fig.set_figwidth(20)
    # now we make the plots show in fullscrene 
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    # and configure pressing escape to exit fullscreen
    mng.window.bind("<Escape>", lambda event: mng.full_screen_toggle())
    # now we plot the original sound wave, the transformed sound wave and the fourier transform

    time = np.linspace(0, len(og_audio_data)/sample_rate, num=len(og_audio_data))
    try:
        axs[0].plot(time, og_audio_data)
        axs[0].set_title("Original Sound Wave")
        axs[0].set_xlabel("Time (s)")
        axs[0].set_ylabel("Amplitude")
    except ValueError:
        pass
    try: 
        axs[2].plot(time, transformed_audio_data)
        axs[2].set_title("Transformed Sound Wave")
        axs[2].set_xlabel("Time (s)")
        axs[2].set_ylabel("Amplitude")
    except ValueError:
        pass

    try:
        # first we clean up the fourier transform to have only frequencies smaller then 20000 and positive amplitudes    
        # then we plot the fourier transform
        fourier_transform = fourier_transform[:len(fourier_transform)//2]
        try:
            fourier_transform = fourier_transform[:20000]
        except IndexError:
            fourier_transform = np.abs(fourier_transform)
        axs[1].plot(fourier_transform)
        axs[1].set_title("Fourier Transform")
        axs[1].set_xlabel("Frequency (hz)")
        axs[1].set_ylabel("Amplitude")
    except ValueError:
        pass 

    plt.show()
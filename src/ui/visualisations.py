import numpy as np
import matplotlib.pyplot as plt


def plot_sound_wave(time, og_wave, axs):
    """this function plots a given sound wave using its sample rate and the audio data.

    Args:
        sample_rate (int): the sample rate of the audio data
        audio_data (np.array): the audio data to be plotted
    """

    try:
        axs[0].plot(time, og_wave)
        axs[0].set_title("Original Sound Wave")
        axs[0].set_xlabel("Time (s)")
        axs[0].set_ylabel("Amplitude")
    except ValueError:
        pass


def plot_fourier_transform(transform, axs):
    """this function plots the fourier transform of a given audio data

    Args:
        fourier_transform (np.array): the fourier transform of the audio data
    """

    try:
        if len(transform) > 20000:
            try:
                transform = transform[:20000]
            except IndexError:
                transform = transform[: len(transform) // 2]
        try:
            transform = np.abs(transform)
        except ValueError:
            pass

        axs[1].plot(transform)
        axs[1].set_title("Fourier Transform")
        axs[1].set_xlabel("Frequency (hz)")
        axs[1].set_ylabel("Amplitude")
    except ValueError:
        pass


def plot_all(sample_rate, og_wave, transform):
    """this function plots the originafourier_transforml sound wave, the transformed sound wave and
    the fourier transform side by side

    Args:
        sample_rate (int): the sample rate of the audio data
        og_wave (np.array): the original audio data
        transform (np.array): the fourier transform of the audio data
    """
    fig, axs = plt.subplots(2, 1)
    fig.subplots_adjust(hspace=1)
    time = np.linspace(0, len(og_wave) / sample_rate, num=len(og_wave))

    plot_sound_wave(time, og_wave, axs)
    plot_fourier_transform(transform, axs)

    plt.style.use("seaborn")
    plt.show()

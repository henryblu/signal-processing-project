import numpy as np
import matplotlib.pyplot as plt


def plot_sound_wave(time, og_wave, axs, plot: int, title):
    """this function plots a given sound wave using its sample rate and the audio data.

    Args:
        time (np.array): the time of the audio data
        og_wave (np.array): the audio data
        axs (matplotlib.pyplot.subplots): the subplots to plot the data on
        plot (int): the plot to plot the data on
        title (str): the title of the plot
    """

    try:
        axs[plot].plot(time, og_wave)
        axs[plot].set_title(title)
        axs[plot].set_xlabel("Time (s)")
        axs[plot].set_ylabel("Amplitude")
    except ValueError:
        pass


def plot_fourier_transform(transform, axs, plot: int, title):
    """this function plots the fourier transform of a given audio data

    Args:
        fourier_transform (np.array): the fourier transform of the audio data
        axs (matplotlib.pyplot.subplots): the subplots to plot the data on
        plot (int): the plot to plot the data on
        title (str): the title of the plot
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

        axs[plot].plot(transform)
        axs[plot].set_title(title)
        axs[plot].set_xlabel("Frequency (hz)")
        axs[plot].set_ylabel("Amplitude")
    except ValueError:
        pass


def plot_all(sample_rate, og_wave, transform, altered_transform, noise_reduced_wave):
    """This function plots the original sound wave, the fourier transform of the original sound wave,
    the altered fourier transform and the altered sound wave.

    Args:
        sample_rate (int): the sample rate of the audio data
        og_wave (np.array): the original audio data
        transform (np.array): the fourier transform of the original audio data
        altered_transform (np.array): the altered fourier transform of the original audio data
        noise_reduced_wave (np.array): the altered audio data
    """
    fig, axs = plt.subplots(4, 1)
    fig.subplots_adjust(hspace=2)
    fig.set_size_inches(10, 6)
    time = np.linspace(0, len(og_wave) / sample_rate, num=len(og_wave))
    noise_reduced_wave = noise_reduced_wave[: len(og_wave)]

    plot_sound_wave(time, og_wave, axs, plot=0, title="Original Sound Wave")
    plot_fourier_transform(transform, axs, plot=1, title="Fourier Transform")
    plot_fourier_transform(
        altered_transform, axs, plot=2, title="Altered Fourier Transform"
    )
    plot_sound_wave(time, noise_reduced_wave, axs, plot=3, title="Altered Sound Wave")

    plt.style.use("seaborn")
    plt.show()

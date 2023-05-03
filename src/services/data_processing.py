import numpy as np
from scipy.io import wavfile as wav


def input_checker(file, verbose=False):
    """this function is used to check if the input is valid

    Args:
        file (str): the path to the input file
        verbose (bool): if true the function will print out the wave specifications

    Returns:
        int: the sample rate of the audio data
        np.array: the audio data
        np.array: the noisy audio data
    """
    if file is not None:
        if file[-4:] != ".wav":
            raise ValueError("input file must be a .wav file")
        sample_rate, composite_signal = get_data(file)

    else:
        sample_rate, composite_signal = sample_wave_generation(verbose=verbose)
        composite_signal = add_noise(composite_signal, verbose=verbose)

    return sample_rate, composite_signal


def sample_wave_generation(duration=1, sample_rate=512, verbose=False):
    """
    this function generates a composite wavfe of three random waves of a given
    sample rate and duration

    Args:
        duration (int): the duration of the wave in seconds
        sample_rate (int): the sample rate of the wave
        verbose (bool): if true the function will print out the wave specifications

    Returns:
        int: the sample rate of the audio data
        np.array: the audio data
    """
    if verbose:
        print()
        print("no file specified, generating random composite wave of 3 frequencies")

    frequency_list = [
        np.random.randint(1, sample_rate),
        np.random.randint(1, sample_rate),
        np.random.randint(1, sample_rate),
    ]
    signal_1 = np.sin(
        2 * np.pi * frequency_list[0] * np.arange(sample_rate * duration) / sample_rate
    )
    signal_2 = np.sin(
        2 * np.pi * frequency_list[1] * np.arange(sample_rate * duration) / sample_rate
    )
    signal_3 = np.sin(
        2 * np.pi * frequency_list[2] * np.arange(sample_rate * duration) / sample_rate
    )
    composite_signal = signal_1 + signal_2 + signal_3

    if verbose:
        print()
        print("wave specifications: ")
        print("    duration of wave: " + str(duration) + " seconds")
        print("    sample rate: " + str(sample_rate) + " samples per second")
        print(
            "    frequencies of composite signal (in hz): "
            + ", ".join([str(x) + "hz" for x in frequency_list])
        )
        print()

    return (sample_rate, composite_signal)


def add_noise(composite_signal, noise_level=0.7, verbose=False):
    """this function adds noise to the composite wave

    Args:
        composite_signal (np.array): the composite wave
        noise_level (float): the level of noise to be added
        verbose (bool): if true the function will print out the wave specifications

    Returns:
        np.array: the noisy wave
    """
    if verbose:
        print("adding noise to composite wave")
    noise = np.random.randn(len(composite_signal))
    noisy_signal = composite_signal + noise_level * noise

    return noisy_signal


def get_data(audio_file_path):
    """this function is used to convert the audiofile to a numpy array

    Args:
        audio_file_path (str): the path to the audio file

    Returns:
        int: the sample rate of the audio data
        np.array: the audio data
    """
    try:
        sample_rate, audio_data = wav.read(audio_file_path)
    except FileNotFoundError as exc:
        raise FileNotFoundError("input file not found") from exc

    return (sample_rate, np.array(audio_data))


def output(sample_rate, new_sound_wave, output_file_path=None):
    """this function is used to output the new sound wave to a file.
    if no file is specified then the default file is used

    Args:
        sample_rate (int): the sample rate of the audio data
        new_sound_wave (np.array): the audio data
    """
    # not working right now
    if not output_file_path:
        wav.write(r"src\data\output.wav", sample_rate, new_sound_wave)

    else:
        try:
            wav.write(output_file_path, sample_rate, new_sound_wave)
        except FileNotFoundError:
            print("output path not found")

import numpy as np


def high_pitch_reduction(fourier_transform, max_frequency):
    """This function sets high frequency components of the fourier transform to 0

    Args:
        fourier_transform (np.array): the fourier transform to be noise reduced
        max_frequency (int): the cutoff frequency for which all frequencies above will be set to 0

    Returns:
        np.array: the pitch reduced fourier transform
    """
    new_transform = np.copy(fourier_transform)
    new_transform[max_frequency : len(fourier_transform)] = 0
    return new_transform


def low_pitch_reduction(fourier_transform, min_frequency=0):
    """This function sets high frequency components of the fourier transform to 0

    Args:
        fourier_transform (np.array): the fourier transform to be noise reduced
        min_frequency (int): the cutoff frequency for which all frequencies below will be set to 0
            defaults to 0

    Returns:
        np.array: the pitch reduced fourier transform
    """
    new_transform = np.copy(fourier_transform)
    new_transform[0:min_frequency] = 0
    return new_transform


def noise_reduction(fourier_transform, threadshold_level=0):
    """this function performs a simple noise reduction on a given fourier transform depended
    on the given threashold.

    Args:
        fourier_transform (np.array): the fourier transform to be noise reduced
        threadshold_level (int): the threashold is how many standard deviations below the mean
                                we want to make the cut off point

    Returns:
        np.array: the noise reduced fourier transform
    """
    max_val = np.max(np.abs(fourier_transform))
    threadshold = threadshold_level / 100 * max_val
    noise_reduced_transform = np.copy(fourier_transform)
    noise_reduced_transform[np.abs(noise_reduced_transform) < threadshold] = 0
    return noise_reduced_transform

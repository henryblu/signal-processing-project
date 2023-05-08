import numpy as np


class TransformAlterations:
    """This class is used to alter the fourier transform of a given audio file"""

    def high_pitch_reduction(self, fourier_transform, threadshold_level=0):
        """This function sets high frequency components of the fourier transform to 0

        Args:
            fourier_transform (np.array): the fourier transform to be noise reduced
            threadshold_level (int): the threashold is what persent of the max value
                                    we want to make the cut off point (min = 0, max = 100)

        Returns:
            np.array: the pitch reduced fourier transform
        """
        max_len = len(fourier_transform) if len(fourier_transform) < 20000 else 20000
        threadshold = threadshold_level / 100
        new_transform = np.copy(fourier_transform)
        new_transform[int(max_len * (1 - threadshold)) : len(fourier_transform)] = 0
        return new_transform

    def low_pitch_reduction(self, fourier_transform, threadshold_level=0):
        """This function sets high frequency components of the fourier transform to 0

        Args:
            fourier_transform (np.array): the fourier transform to be noise reduced
            threadshold_level (int): the threashold is what persent of the max value
                                    we want to make the cut off point (min = 0, max = 100)

        Returns:
            np.array: the pitch reduced fourier transform
        """
        cutoff = len(fourier_transform) if len(fourier_transform) < 20000 else 20000
        threadshold = threadshold_level / 100
        new_transform = np.copy(fourier_transform)
        new_transform[0 : int(cutoff * threadshold)] = 0
        return new_transform

    def noise_reduction(self, fourier_transform, threadshold_level=0):
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

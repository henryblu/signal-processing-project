import numpy as np

class noise_reduction:

    def __init__(self, fourier_transform, threadshold_level):
        self.fourier_transform = fourier_transform
        self.threadshold_level = threadshold_level
    def noise_reduction(fourier_transform, threadshold_level):
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

import numpy as np


class Transforms:
    """this class is used to perform fourier transforms on a given audio data"""

    def __init__(self, rft, fft, verbose=False):
        """this function is used to initialize the class

        Args:
            rft (bool): if true the regular fourier transform will be used
            fft (bool): if true the fast fourier transform will be used
            audio_data (np.array): the audio data
            verbose (bool, optional): if true the class will print out information. Defaults to False.
        """
        self.verbose = verbose
        self.fourier_transform = None
        if rft and fft:
            raise ValueError("both rft and fft cannot be true")
        self.transform_type = "rft" if rft else "fft"

    def run_transform(self, audio_data):
        """this function runs the correct type of fourier transform on the audio data

        Args:
            audio_data (np.array): the audio data to be transformed

        Returns:
            np.array: the fourier transform of the audio data
        """
        if self.transform_type == "rft":
            self.fourier_transform = self.regular_fourier_transform(audio_data)

        else:
            if np.log2(len(audio_data)) % 1 != 0:
                if self.verbose:
                    print("the length of the audio data is not a power of 2")
                    print("using bluestein's fft")
                    print()
                self.fourier_transform = self.bluestein_fft(audio_data)
            else:
                self.fourier_transform = self.fast_fourier_transform(audio_data)

        return self.fourier_transform

    def run_inverse(self, fourier_transform):
        """this function runs the correct type of inverse fourier transform on the fourier transform

        Args:
            fourier_transform (np.array): the fourier transform to be transformed

        Returns:
            np.array: the inverse fourier transform of the fourier transform
        """

        if self.transform_type == "rft":
            inverse = self.inverse_regular_fourier_transform(fourier_transform)
        else:
            inverse = self.inverse_fast_fourier_transform(fourier_transform)
        inverse = np.real(inverse)

        return inverse

    def regular_fourier_transform(self, audio_data):
        """this function performs a regualr fourier transform on a given audio data

        Args:
            audio_data (np.array): the audio data to be transformed

        Returns:
            np.array: the fourier transform of the audio data
        """
        N = len(audio_data)
        fourier_transform = np.zeros(N, dtype=complex)
        for k in range(N):
            for q in range(N):
                fourier_transform[k] += audio_data[q] * np.exp(-2j * np.pi * k * q / N)
        return fourier_transform

    def fast_fourier_transform(self, audio_data):
        """This function performs a fast fourier transform on a given audio data it only
        worked for audio data with a length that is a power of 2

        Args:
            audio_data (np.array): the audio data to be transformed

        Returns:
            np.array: the fourier transform of the audio data
        """
        N = len(audio_data)
        if N <= 1:
            return audio_data
        if N % 2 != 0:
            raise ValueError("size of audio_data must be a power of 2")

        even = self.fast_fourier_transform(audio_data[:N:2])
        odd = self.fast_fourier_transform(audio_data[1:N:2])

        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate(
            [even + factor[: N // 2] * odd, even + factor[N // 2 :] * odd]
        )

    def bluestein_fft(self, audio_data):
        """This function performs a Bluestein's algorithm Fourier transform on a given audio data

        Args:
            audio_data (np.array): the audio data to be transformed

        Returns:
            np.array: the Fourier transform of the audio data
        """

        N = len(audio_data)
        if N <= 1:
            return audio_data

        if np.log2(N) % 1 != 0:
            padding = 1
            while padding < N:
                padding *= 2
            N = padding
            padding_arr = np.zeros(N - len(audio_data))
            audio_data = np.concatenate((audio_data, padding_arr))

        even = self.bluestein_fft(audio_data[:N:2])
        odd = self.bluestein_fft(audio_data[1:N:2])

        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate(
            [even + factor[: N // 2] * odd, even + factor[N // 2 :] * odd]
        )

    def inverse_regular_fourier_transform(self, fourier_transform):
        """this function performs an inverse regular fourier transform on a given fourier transform

        Args:
            fourier_transform (np.array): the fourier transform to be transformed

        Returns:
            np.array: the inverse fourier transform of the fourier transform
        """
        N = len(fourier_transform)
        inverse_fourier_transform = np.zeros(N, dtype=complex)
        for k in range(N):
            for q in range(N):
                inverse_fourier_transform[k] += fourier_transform[q] * np.exp(
                    2j * np.pi * k * q / N
                )

        return inverse_fourier_transform / N

    def inverse_fast_fourier_transform(self, fourier_transform):
        """this function performs an inverse fast fourier transform on a given fourier transform

        Args:
            fourier_transform (np.array): the fourier transform to be transformed

        Returns:
            np.array: the inverse fourier transform of the fourier transform
        """

        N = len(fourier_transform)
        if N <= 1:
            return fourier_transform
        if N % 2 != 0:
            raise ValueError("size of audio_data must be a power of 2")

        even = self.inverse_fast_fourier_transform(fourier_transform[:N:2])
        odd = self.inverse_fast_fourier_transform(fourier_transform[1:N:2])

        factor = np.exp(2j * np.pi * np.arange(N) / N)
        return (
            np.concatenate(
                [even + factor[: N // 2] * odd, even + factor[N // 2 :] * odd]
            )
            / 2
        )

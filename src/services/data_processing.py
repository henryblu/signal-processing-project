import numpy as np
from scipy.io import wavfile as wav


class AudioFileProcessing:
    """this class is used to handel audio file processing"""

    def __init__(
        self, input_file=None, output_file=r"src\Data\output.wav", verbose=False
    ):
        """this function is used to initialize the audio_processing class

        Args:
            input_file (str): the path to the input file.
                Defaults to None.
            output_file (str, optional): the path to the output file.
                Defaults to ("src\\data\\output.wav").
            verbose (bool, optional): whether or not to print verbose output.
                Defaults to False.

        Raises:
            ValueError: if the input file is not a .wav file
            FileNotFoundError: if the input file is not found
            ValueError: if the input file is too long
        """

        self.input_file = input_file
        self.output_file = output_file
        self.verbose = verbose
        self.sample_rate, self.audio_data = self.get_data(self.input_file)
        self.data_triming()
        self.front_trim = 0
        self.back_trim = 0
        self.length = None
        self.noise_level = 0.1

    def get_audio_data(self):
        """Returns the audio data as a numpy array."""
        return self.audio_data

    def get_sample_rate(self):
        """Returns the sample rate of the audio data."""
        return self.sample_rate

    def get_data(self, input_file=None):
        """this function is used to convert the audiofile to a numpy array

        Raises:
            ValueError: if the input file is not a .wav file
            FileNotFoundError: if the input file is not found
        """
        if input_file[-4:] != ".wav":
            raise ValueError("input file must be a .wav file")
        try:
            sample_rate, audio_data = wav.read(input_file)
        except FileNotFoundError as exc:
            raise FileNotFoundError("input file not found") from exc

        return sample_rate, audio_data

    def data_triming(self):
        """this function trims the audio data to remove any leading or trailing zeros

        Raises:
            ValueError: if the input file is too long
        """
        self.length = len(self.audio_data)
        self.front_trim = len(self.audio_data) - len(
            np.trim_zeros(self.audio_data, "f")
        )
        self.back_trim = len(self.audio_data) - len(np.trim_zeros(self.audio_data, "b"))

        self.audio_data = np.trim_zeros(self.audio_data)

        if len(self.audio_data) > 2**16:
            raise ValueError("input file is too long")

    def output(self, new_sound_wave, output_file=r"src\Data\output.wav"):
        """this function is used to output the new sound wave to a file.
        if no file is specified then the default file is used

        Args:
            new_sound_wave (numpy array): the new sound wave to be outputted

        Raises:
            FileNotFoundError: if the output file path is not found
        """
        if self.front_trim > 0:
            new_sound_wave = np.concatenate((np.zeros(self.front_trim), new_sound_wave))
        if self.back_trim > 0:
            new_sound_wave = np.concatenate((new_sound_wave, np.zeros(self.back_trim)))
        new_sound_wave = new_sound_wave.astype(np.int16)
        try:
            wav.write(output_file, self.sample_rate, new_sound_wave)
        except FileNotFoundError:
            print("output path not found")

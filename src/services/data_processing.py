import numpy as np
from scipy.io import wavfile as wav


class audio_preprocessing:
    """this class is used to handel the audio file processing or the random audio data generation"""

    def __init__(
        self, input_file=None, output_file=r"src\data\output.wav", verbose=False
    ):
        """this function is used to initialize the audio_processing class

        Args:
            input_file (str): the path to the input file. Defaults to None.
            output_file (str, optional): the path to the output file. Defaults to r"src\data\output.wav".
            verbose (bool, optional): whether or not to print verbose output. Defaults to False.

        Raises:
            ValueError: if the input file is not a .wav file
            FileNotFoundError: if the input file is not found
            ValueError: if the input file is too long
        """

        self.input_file = input_file
        self.output_file = output_file
        self.verbose = verbose
        self.sample_rate = None
        self.duration = None
        self.audio_data = None
        self.og_length = None
        self.noise_level = None

        if self.input_file is not None:
            if self.input_file[-4:] != ".wav":
                raise ValueError("input file must be a .wav file")
            self.get_data()
            self.data_triming()
            self.duration = len(self.audio_data) / self.sample_rate
        else:
            self.sample_wave_generation()
            self.add_noise()

    def get_data(self):
        """this function is used to convert the audiofile to a numpy array

        Raises:
            FileNotFoundError: if the input file is not found
        """
        try:
            self.sample_rate, self.audio_data = wav.read(self.input_file)
        except FileNotFoundError as exc:
            raise FileNotFoundError("input file not found") from exc


    def data_triming(self):
        """this function trims the audio data to remove any leading or trailing zeros
        
        Raises:
            ValueError: if the input file is too long
        """
        self.og_length = len(self.audio_data)
        self.audio_data = np.trim_zeros(self.audio_data)
        if len(self.audio_data) > 2**16:
            raise ValueError("input file is too long \n max length is 2^16 \n current length is {}".format(len(self.audio_data)))

    def sample_wave_generation(self):
        """
        this function generates a composite wavfe of three random waves of a given
        sample rate and duration

        """

        if self.verbose:
            print()
            print(
                "no file specified, generating random composite wave of 3 frequencies"
            )

        frequency_list = [
            np.random.randint(1, self.sample_rate),
            np.random.randint(1, self.sample_rate),
            np.random.randint(1, self.sample_rate),
        ]
        signal_1 = np.sin(
            2
            * np.pi
            * frequency_list[0]
            * np.arange(self.sample_rate * self.duration)
            / self.sample_rate
        )
        signal_2 = np.sin(
            2
            * np.pi
            * frequency_list[1]
            * np.arange(self.sample_rate * self.duration)
            / self.sample_rate
        )
        signal_3 = np.sin(
            2
            * np.pi
            * frequency_list[2]
            * np.arange(self.sample_rate * self.duration)
            / self.sample_rate
        )
        self.audio_data = signal_1 + signal_2 + signal_3

        if self.verbose:
            print()
            print("wave specifications: ")
            print("    duration of wave: " + str(self.duration) + " seconds")
            print("    sample rate: " + str(self.sample_rate) + " samples per second")
            print(
                "    frequencies of composite signal (in hz): "
                + ", ".join([str(x) + "hz" for x in frequency_list])
            )
            print()

    def add_noise(self):
        """this function adds noise to the composite wave"""
        if self.verbose:
            print("adding noise to composite wave")

        noise = np.random.randn(len(self.audio_data))
        self.audio_data += self.noise_level * noise

    def output(self, new_sound_wave):
        """this function is used to output the new sound wave to a file.
        if no file is specified then the default file is used

        Args:
            new_sound_wave (numpy array): the new sound wave to be outputted

        Raises:
            FileNotFoundError: if the output file path is not found
        """
        try:
            wav.write(self.output_file_path, self.sample_rate, new_sound_wave)
        except FileNotFoundError:
            print("output path not found")

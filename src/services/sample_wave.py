import numpy as np
from scipy.io import wavfile as wav


class SampleWave:
    """this class is used to handel sample random audio data generation"""

    def __init__(self, verbose=False, sample_rate=256, duration=1, noise_amplitude=1):
        """this class is used to generate a composite wave of three random sine waves

        Args:
            verbose (bool, optional): whether or not to print verbose output.
                Defaults to False.
            sample_rate (int, optional): the sample rate of the audio data.
                Defaults to 256.
            duration (int, optional): the duration of the audio data.
                Defaults to 1.
            noise_amplitude (int, optional): the amplitude of the noise to be added to the audio data.
                Defaults to 1.
        """
        self.verbose = verbose
        self.sample_rate = sample_rate
        self.duration = duration
        self.noise_amplitude = noise_amplitude
        self.audio_data = None
        self.sample_wave_generation()
        self.add_noise(self.noise_amplitude)

    def get_audio_data(self):
        """this function returns the audio data generated by the class

        Returns:
            numpy array: the audio data generated by the class
        """
        return self.audio_data

    def set_audio_data(self, new_audio_data):
        """this function sets the audio data generated by the class
        
        Args:
            new_audio_data (numpy array): the new audio data to be set
        """
        self.audio_data = new_audio_data.astype(np.int16)

    def get_sample_rate(self):
        """this function returns the sample rate of the audio data generated by the class

        Returns:
            int: the sample rate of the audio data generated by the class
        """
        return self.sample_rate

    def sample_wave_generation(self):
        """This function generates a composite wave of three random waves of a given
        sample rate and duration.
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

    def add_noise(self, noise_level=0.1):
        """this function adds noise to the composite wave

        Args:
            noise_level (float, optional): the amplitude of the noise to be added.
                Defaults to 0.1.
        """
        noise = np.random.randn(len(self.audio_data))
        self.audio_data += noise_level * noise

    def output(self, output_file=r"src/Data/output.wav"):
        """this function outputs the composite wave to a file
        Args:
            audiodata (numpy array): the audio data to be outputted
            output_file (str, optional): the path to the output file.
                Defaults to ("src/data/output.wav").
        """
        try:
            wav.write(output_file, self.sample_rate, self.audio_data)
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                "The specified output path does not exist."
            ) from exc

import numpy as np


class TransformAlterations:
    """This class is used to alter the fourier transform of a given audio file"""

    def __init__(self):
        """This function initializes the class"""
        self.threadshold_level = None
        self.old_fourier_transform = None
        self.length = None

    def run(self, fourier_transform):
        """This function runs the wave alteration on the fourier transform given the
        user input

        Args:
            fourier_transform (np.array): the fourier transform to be altered

        Returns:
            np.array: the altered fourier transform
        """

        self.old_fourier_transform = fourier_transform
        self.length = len(fourier_transform)

        while True:
            self.threadshold_level = input(
                "Please enter the desired threadshold_level (0 to 100): "
            )
            try:
                self.threadshold_level = int(self.threadshold_level)
                if self.threadshold_level < 0 or self.threadshold_level > 100:
                    print("Invalid input, please try again")
                    print()
                else:
                    break
            except ValueError:
                print("Invalid input, please try again")
                print()

        while True:
            print("What type of wave alteration would you like to perform?")
            print("1. High Pitch Reduction")
            print("2. Low Pitch Reduction")
            print("3. Noise Reduction")
            print("4. No Alteration")
            print()

            user_input = input(
                "Please enter the number of the option you would like to perform: "
            )

            if user_input == "1":
                altered_fourier_transform = self.high_pitch_reduction(
                    self.old_fourier_transform, self.threadshold_level
                )
                break
            elif user_input == "2":
                altered_fourier_transform = self.low_pitch_reduction(
                    self.old_fourier_transform, self.threadshold_level
                )
                break
            elif user_input == "3":
                altered_fourier_transform = self.noise_reduction(
                    self.old_fourier_transform, self.threadshold_level
                )
                break
            elif user_input == "4":
                altered_fourier_transform = self.old_fourier_transform
                break
            else:
                print("Invalid input, please try again")
                print()

        return altered_fourier_transform

    def high_pitch_reduction(self, fourier_transform, threadshold_level):
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
        new_transform[int(cutoff * (1 - threadshold)) : self.length] = 0
        return new_transform

    def low_pitch_reduction(self, fourier_transform, threadshold_level):
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

    def noise_reduction(self, fourier_transform, threadshold_level):
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

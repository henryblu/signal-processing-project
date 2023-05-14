from src.services.transform_alternations import (
    high_pitch_reduction,
    low_pitch_reduction,
    noise_reduction,
)


def run_alterations(old_fourier_transform):
    """This function lets the user choose the amount of alterations they would
    like to perform

    Args:
        old_fourier_transform (np.array): the fourier transform to be altered

    Returns:
        np.array: the altered fourier transform
    """
    altered_fourier_transform = options(old_fourier_transform)
    while True:
        print("Would you like to run another alteration?")
        print("1. Yes")
        print("2. No")
        print()
        user_input = input(
            "Please enter the number of the option you would like to perform: "
        )
        if user_input == "1":
            altered_fourier_transform = options(altered_fourier_transform)
            continue
        if user_input == "2":
            break
        print("Invalid input, please try again")
        print()
    return altered_fourier_transform


def options(old_fourier_transform):
    """This function lets the user choose which alteration they would like to perform

    Args:
        old_fourier_transform (np.array): the fourier transform to be altered

    Returns:
        np.array: the altered fourier transform
    """

    while True:
        print("What type of wave alteration would you like to perform?")
        print("1. High Pitch Reduction")
        print("2. Low Pitch Reduction")
        print("3. Noise Reduction")
        print()
        user_input = input(
            "Please enter the number of the option you would like to perform: "
        )

        if user_input == "1":
            altered_fourier_transform = call_hpr(old_fourier_transform)
            break
        if user_input == "2":
            altered_fourier_transform = call_lpr(old_fourier_transform)
            break
        if user_input == "3":
            altered_fourier_transform = call_nr(old_fourier_transform)
            break

        print("Invalid input, please try again")
        print()

    return altered_fourier_transform


def call_hpr(old_fourier_transform):
    """This function calls the high pitch reduction function

    Args:
        old_fourier_transform (np.array): the fourier transform to be altered

    Returns:
        np.array: the altered fourier transform
    """
    while True:
        try:
            size = len(old_fourier_transform)
            max_frequency = int(
                input(
                    "Please enter the desired maximum frequency in hz: (1 to "
                    + ("20000):" if size > 20000 else str(size) + "):")
                )
            )
            if max_frequency < 1 or max_frequency > (20000 if size > 20000 else size):
                print("Invalid input, please try again")
                print()
            else:
                break
        except ValueError:
            print("Invalid input, please input either 1 or 2")
            print()
    return high_pitch_reduction(old_fourier_transform, max_frequency)


def call_lpr(old_fourier_transform):
    """This function calls the low pitch reduction function

    Args:
        old_fourier_transform (np.array): the fourier transform to be altered

    Returns:
        np.array: the altered fourier transform
    """
    while True:
        try:
            size = len(old_fourier_transform)
            max_frequency = int(
                input(
                    "Please enter the desired minimum frequency in hz: (1 to "
                    + ("20000):" if size > 20000 else str(size) + "):")
                )
            )
            if max_frequency < 1 or max_frequency > (20000 if size > 20000 else size):
                print("Invalid input, please try again")
                print()
            else:
                break
        except ValueError:
            print("Invalid input, please try again")
            print()
    return low_pitch_reduction(old_fourier_transform, max_frequency)


def call_nr(old_fourier_transform):
    """This function calls the noise reduction function

    Args:
        old_fourier_transform (np.array): the fourier transform to be altered

    Returns:
        np.array: the altered fourier transform
    """
    while True:
        try:
            threadshold_level = input(
                "Please enter the desired threadshold_level (0 to 100): "
            )
            threadshold_level = int(threadshold_level)
            if threadshold_level < 0 or threadshold_level > 100:
                print("Invalid input, please try again")
                print()
            else:
                break
        except ValueError:
            print("Invalid input, please try again")
            print()
    return noise_reduction(old_fourier_transform, threadshold_level)

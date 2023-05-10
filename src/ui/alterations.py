from services.transform_alternations import (
    high_pitch_reduction,
    low_pitch_reduction,
    noise_reduction,
)


def run_alterations(old_fourier_transform):
    """This function runs the wave alteration on the fourier transform given the
    user input

    Args:
        fourier_transform (np.array): the fourier transform to be altered

    Returns:
        np.array: the altered fourier transform
    """

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
            while True:
                try:
                    max_frequency = int(
                        input(
                            "Please enter the desired maximum frequency in hz (0 to 20000): "
                        )
                    )
                    if max_frequency < 0 or max_frequency > 20000:
                        print("Invalid input, please try again")
                        print()
                    else:
                        break
                except ValueError:
                    print("Invalid input, please try again")
                    print()
            altered_fourier_transform = high_pitch_reduction(
                old_fourier_transform, max_frequency
            )
            break
        elif user_input == "2":
            while True:
                try:
                    min_frequency = int(
                        input(
                            "Please enter the desired minimum frequency in hz (0 to 20000): "
                        )
                    )
                    if min_frequency < 0 or min_frequency > 20000:
                        print("Invalid input, please try again")
                        print()
                    else:
                        break
                except ValueError:
                    print("Invalid input, please try again")
                    print()

            altered_fourier_transform = low_pitch_reduction(
                old_fourier_transform, min_frequency
            )
            break
        elif user_input == "3":
            while True:
                threadshold_level = input(
                    "Please enter the desired threadshold_level (0 to 100): "
                )
                try:
                    threadshold_level = int(threadshold_level)
                    if threadshold_level < 0 or threadshold_level > 100:
                        print("Invalid input, please try again")
                        print()
                    else:
                        break
                except ValueError:
                    print("Invalid input, please try again")
                    print()

            altered_fourier_transform = noise_reduction(
                old_fourier_transform, threadshold_level
            )

            break
        elif user_input == "4":
            altered_fourier_transform = old_fourier_transform
            break
        else:
            print("Invalid input, please try again")
            print()

    return altered_fourier_transform

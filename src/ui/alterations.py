from services.transform_alternations import TransformAlterations


def run_alterations(old_fourier_transform):
    """This function runs the wave alteration on the fourier transform given the
    user input

    Args:
        fourier_transform (np.array): the fourier transform to be altered

    Returns:
        np.array: the altered fourier transform
    """

    ta = TransformAlterations()

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
            altered_fourier_transform = ta.high_pitch_reduction(
                old_fourier_transform, threadshold_level
            )
            break
        elif user_input == "2":
            altered_fourier_transform = ta.low_pitch_reduction(
                old_fourier_transform, threadshold_level
            )
            break
        elif user_input == "3":
            altered_fourier_transform = ta.noise_reduction(
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

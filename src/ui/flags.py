import argparse


def flags_finder():
    """this function is used to find all the flags that have been set.

    Returns:
        list[int]: a list of all the flags that have been set
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        help="specifies the .wav sound wave file to be read. "
        + "Default is randomly generated sound wave",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="specifies the file to be written to default is ./data/output.wav",
        default=r"src/Data/output.wav",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="prints the details of the algrithm including time taken and memory taken",
        action="store_true",
    )
    parser.add_argument(
        "-d",
        "--discrete_fourier_transform",
        help="specifies the discrete fourier transform to be used",
        action="store_true",
    )
    parser.add_argument(
        "-f",
        "--fast_fourier_transform",
        help="specifies the fast fourier transform to be used",
        action="store_true",
    )

    args = parser.parse_args()
    return args

import os
import sys

# this is used to import the modules from the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.audio_file_wave import AudioWave
from services.sample_wave import SampleWave
from services.transforms import Transforms
from ui.visualisations import plot_all
from ui.flags import flags_finder
from ui.alterations import run_alterations

# from tests.performance_test import performance_test


def main():
    """This function is the main function of the program it is used to call all the other
    functions"""
    flags = flags_finder()

    if flags.input is not None:
        wave = AudioWave(
            input_file=flags.input,
            output_file=flags.output,
            verbose=flags.verbose,
        )
    else:
        wave = SampleWave(verbose=flags.verbose)
    sample_rate = wave.get_sample_rate()
    audio_data = wave.get_audio_data()

    t = Transforms(
        flags.discrete_fourier_transform,
        flags.fast_fourier_transform,
        flags.verbose,
    )

    og_fourier = t.run_transform(audio_data)
    altered_fourier = run_alterations(og_fourier)
    altered_signal = t.run_inverse(altered_fourier)

    plot_all(
        sample_rate,
        audio_data,
        og_fourier,
        altered_fourier,
        altered_signal,
    )

    if flags.verbose:
        print()
        print("outputting composite wave to file: " + flags.output + "\n")
    wave.set_audio_data(altered_signal)
    wave.output(output_file=flags.output)

    return


if __name__ == "__main__":
    main()

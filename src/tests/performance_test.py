import numpy as np
import matplotlib.pyplot as plt
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join("../..")))
from src.services.transforms import Transforms
from src.services.sample_wave import SampleWave


class PerformanceTesting:
    """This class is used to run the performance tests"""

    def __init__(self, iterations=50) -> None:
        """This function is used to initialise the PerformanceTesting class"""
        self.titles = []
        self.iterations = iterations
        self.samples = [i * 16 for i in range(1, self.iterations + 1)]
        pass

    def run(self, dft=False, fft=False, bluestines=False, idft=False, ifft=False):
        """This function is used to run the performance tests

        Args:
            dft (bool, optional): This is used to determine if the dft performance test should be run. Defaults to False.
            fft (bool, optional): This is used to determine if the fft performance test should be run. Defaults to False.
            bluestines (bool, optional): This is used to determine if the bluestines fft performance test should be run. Defaults to False.
            idft (bool, optional): This is used to determine if the idft performance test should be run. Defaults to False.
            ifft (bool, optional): This is used to determine if the ifft performance test should be run. Defaults to False.
        """

        self.ptest_dft(dft)
        self.ptest_fft(fft)
        self.ptest_bluestines_fft(bluestines)
        self.ptest_idft(idft)
        self.ptest_ifft(ifft)

        plt.xlabel(
            "size of sample wave (samples)",
            fontdict={"fontsize": 12, "fontweight": "bold"},
        )
        plt.ylabel(
            "time taken (seconds)", fontdict={"fontsize": 12, "fontweight": "bold"}
        )
        title_name = "Performance Test for: " + ", ".join(self.titles)
        plt.title(
            title_name,
            fontdict={"fontsize": 16, "fontweight": "bold"},
        )
        plt.grid(True)
        plt.grid(color="grey", linestyle="--", linewidth=0.5, alpha=0.5)
        plt.style.use("seaborn")
        plt.legend(fontsize=12)
        plt.show()

    def ptest_dft(self, used=False):
        """This function is used to test the dft function in the transforms class

        Args:
            used (bool, optional): This is used to determine if the dft performance test should be run. Defaults to False.
        """
        if not used:
            return
        self.titles.append("dft")
        t = Transforms(dft=True, fft=False, verbose=False)
        dft_time = []
        for i in range(1, self.iterations + 1):
            print("running dft iteration: " + str(i) + " of " + str(self.iterations))
            sample_wave = SampleWave(verbose=False, duration=i, sample_rate=16)
            audio_data = sample_wave.get_audio_data()
            start = time.time()
            t.run_transform(audio_data)
            end = time.time()
            dft_time.append(end - start)
        plt.plot(self.samples, dft_time, label="dft", color="red")

    def ptest_fft(self, used=False):
        """This function is used to test the fft function in the transforms class it only uses
        inputs of size 2^n as those are the only inputs that the fft function can handle.

        Args:
            used (bool, optional): This is used to determine if the fft performance test should be run. Defaults to False.
        """
        if not used:
            return
        self.titles.append("fft")
        t = Transforms(dft=False, fft=True, verbose=False)
        fft_time = np.zeros(self.iterations)
        max_size = self.iterations
        max_power_of_two = int(np.log2(max_size))
        for i in range(1, max_power_of_two + 1):
            print("running fft iteration: " + str(i) + " of " + str(max_power_of_two))
            sample_wave = SampleWave(verbose=False, duration=2**i, sample_rate=16)
            audio_data = sample_wave.get_audio_data()
            start = time.time()
            t.run_transform(audio_data)
            end = time.time()
            fft_time[2 ** (i) - 1] = end - start
        plt.plot(self.samples, fft_time, label="fft", color="green")

    def ptest_bluestines_fft(self, used=False):
        """This function is used to test the bluestines fft function in the transforms class

        Args:
            used (bool, optional): This is used to determine if the bluestines fft performance test should be run. Defaults to False.
        """
        if not used:
            return
        self.titles.append("bluestines_fft")
        t = Transforms(dft=False, fft=True, verbose=False)
        fft_time = []
        for i in range(1, self.iterations + 1):
            print(
                "running bluestines fft iteration: "
                + str(i)
                + " of "
                + str(self.iterations)
            )
            sample_wave = SampleWave(verbose=False, duration=i, sample_rate=16)
            audio_data = sample_wave.get_audio_data()
            start = time.time()
            t.run_transform(audio_data)
            end = time.time()
            fft_time.append(end - start)
        plt.plot(self.samples, fft_time, label="bluestines_fft", color="blue")

    def ptest_idft(self, used=False):
        """This function is used to test the idft function in the transforms class

        Args:
            used (bool, optional): This is used to determine if the idft performance test should be run. Defaults to False.
        """
        if not used:
            return
        self.titles.append("idft")
        t = Transforms(dft=True, fft=False, verbose=False)
        idft_time = []
        for i in range(1, self.iterations + 1):
            print("running idft iteration: " + str(i) + " of " + str(self.iterations))
            sample_wave = SampleWave(verbose=False, duration=i, sample_rate=16)
            audio_data = sample_wave.get_audio_data()
            fourier = np.fft.fft(audio_data)
            start = time.time()
            t.run_inverse(fourier)
            end = time.time()
            idft_time.append(end - start)
        plt.plot(self.samples, idft_time, label="idft", color="orange")

    def ptest_ifft(self, used=False):
        """This function is used to test the ifft function in the transforms class

        Args:
            used (bool, optional): This is used to determine if the ifft performance test should be run. Defaults to False.
        """
        if not used:
            return
        self.titles.append("ifft")
        t = Transforms(dft=False, fft=True, verbose=False)
        ifft_time = []
        for i in range(1, self.iterations + 1):
            print("running ifft iteration: " + str(i) + " of " + str(self.iterations))
            sample_wave = SampleWave(verbose=False, duration=i, sample_rate=16)
            audio_data = sample_wave.get_audio_data()
            fourier = t.run_transform(audio_data)
            start = time.time()
            t.run_inverse(fourier)
            end = time.time()
            ifft_time.append(end - start)
        plt.plot(self.samples, ifft_time, label="ifft", color="navy")


if __name__ == "__main__":
    pt = PerformanceTesting(500)
    pt.run(dft=False, bluestines=True, idft=False, ifft=True)

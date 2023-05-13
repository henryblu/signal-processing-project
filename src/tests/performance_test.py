import numpy as np
import matplotlib.pyplot as plt
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.sample_wave import SampleWave
from services.transforms import Transforms


class PerformanceTesting:
    def __init__(self) -> None:
        self.times = []
        self.iterations = 50
        self.samples = [i * 16 for i in range(1, self.iterations + 1)]
        pass

    def run(self):
        self.ptest_rft()
        # self.ptest_fft()

        self.ptest_bluestines_fft()
        self.ptest_irft()
        self.ptest_ifft()
        # plot the rft and the fft time on the same graph
        plt.plot(self.samples, self.times[0], label="rft", color="red")
        plt.plot(self.samples, self.times[1], label="fft", color="blue")
        plt.plot(self.samples, self.times[2], label="irft", color="orange")
        plt.plot(self.samples, self.times[3], label="ifft", color="lightblue")

        # table of contents

        plt.xlabel(
            "size of sample wave (samples)",
            fontdict={"fontsize": 12, "fontweight": "bold"},
        )
        plt.ylabel(
            "time taken (seconds)", fontdict={"fontsize": 12, "fontweight": "bold"}
        )
        plt.title(
            "rft & irft vs Bluestines_fft & ifft",
            fontdict={"fontsize": 16, "fontweight": "bold"},
        )
        plt.grid(True)
        plt.grid(color="grey", linestyle="--", linewidth=0.5, alpha=0.5)
        plt.style.use("seaborn")
        plt.legend(fontsize=12)
        plt.show()

    def ptest_fft(self):
        """This function is used to test the fft function in the transforms class it only uses
        inputs of size 2^n
        """
        t = Transforms(rft=False, fft=True, verbose=False)
        fft_time = []
        max_size = 256 * 8
        max_power_of_two = int(np.log2(max_size))
        for i in range(1, max_power_of_two + 1):
            print("running fft iteration: " + str(i) + " of " + str(max_power_of_two))
            sample_wave = SampleWave(verbose=False, duration=i, sample_rate=2**i)
            audio_data = sample_wave.get_audio_data()
            start = time.time()
            t.run_transform(audio_data)
            end = time.time()
            fft_time.append(end - start)
        self.times.append(fft_time)

    def ptest_rft(self):
        t = Transforms(rft=True, fft=False, verbose=False)
        rft_time = []
        for i in range(1, self.iterations + 1):
            print("running rft iteration: " + str(i) + " of " + str(self.iterations))
            sample_wave = SampleWave(verbose=False, duration=i, sample_rate=16)
            audio_data = sample_wave.get_audio_data()
            start = time.time()
            t.run_transform(audio_data)
            end = time.time()
            rft_time.append(end - start)
        self.times.append(rft_time)

    def ptest_bluestines_fft(self):
        t = Transforms(rft=False, fft=True, verbose=False)
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
        self.times.append(fft_time)

    def ptest_irft(self):
        t = Transforms(rft=True, fft=False, verbose=False)
        irft_time = []
        for i in range(1, self.iterations + 1):
            print("running irft iteration: " + str(i) + " of " + str(self.iterations))
            sample_wave = SampleWave(verbose=False, duration=i, sample_rate=16)
            audio_data = sample_wave.get_audio_data()
            fourier = np.fft.fft(audio_data)
            start = time.time()
            t.run_inverse(fourier)
            end = time.time()
            irft_time.append(end - start)
        self.times.append(irft_time)

    def ptest_ifft(self):
        t = Transforms(rft=False, fft=True, verbose=False)
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
        self.times.append(ifft_time)


if __name__ == "__main__":
    pt = PerformanceTesting()
    pt.run()

import numpy as np
import matplotlib.pyplot as plt
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.services.sample_wave import SampleWave
from src.services.transforms import Transforms

class PerformanceTesting():

    def __init__(self) -> None:
        self.times = []
        pass

    def ptest_rft(self):
        t = Transforms(rft=True, fft=False, verbose=True)
        rft_time = []
        for i in range(20):
            sample_wave = SampleWave(verbose=False, duration=i)
            audio_data = sample_wave.get_audio_data()
            start = time.time()
            t.run_transform(audio_data)
            end = time.time()
            rft_time.append(end-start)
        self.times.append(rft_time)

    def ptest_fft(self):
        t = Transforms(rft=False, fft=True, verbose=True)
        fft_time = []
        for i in range(20):
            sample_wave = SampleWave(verbose=False, duration=i)
            audio_data = sample_wave.get_audio_data()
            start = time.time()
            t.run_transform(audio_data)
            end = time.time()
            fft_time.append(end-start)
        self.times.append(fft_time)

if __name__ == "__main__":
    pt = PerformanceTesting()
    pt.ptest_rft()
    pt.ptest_fft()
    plt.plot(np.arange(20), pt.times[0], label="RFT")
    plt.plot(np.arange(20), pt.times[1], label="FFT")
        
        

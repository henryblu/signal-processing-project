import time
from scipy.fft import fft, ifft
from memory_profiler import memory_usage
from services.transforms import (
    fast_fourier_transform,
    inverse_fast_fourier_transform,
    regular_fourier_transform,
    inverse_regular_fourier_transform,
)
from services.data_processing import test_wave_generation


class performance_test:
    def __init__(self, duration=1, sample_rate=256, samples=1, verbose=False):
        self.duration = duration
        self.sample_rate = sample_rate
        self.details = verbose
        self.samples = samples

        if self.samples == 1:
            self.signal = test_wave_generation()
            self.fourier_transform = fft(self.signal[0])
            self.inverse_transform = ifft(self.fourier_transform)
        else:
            self.signals_and_frequencies = [
                test_wave_generation() for i in range(self.samples)
            ]
            self.signal_list = [
                self.signals_and_frequencies[i][0] for i in range(self.samples)
            ]
            self.frequencies_list = [
                self.signals_and_frequencies[i][1] for i in range(self.samples)
            ]
            self.fourier_transform_list = [
                fft(self.signal_list[i]) for i in range(self.samples)
            ]
            self.inverse_transform_list = [
                ifft(self.fourier_transform_list[i]) for i in range(self.samples)
            ]

    def run(self):
        print("Running the test suite")

        # request input for algorithm to test
        while True:
            imput = input(
                "Please enter the algorithm you would like to test (options:'rft', 'fft', 'irft', 'ifft', 'all'): "
            )
            print()
            if imput == "rft":
                self.rft_test()
                return
            elif imput == "fft":
                self.fft_test()
                return
            elif imput == "irft":
                self.irft_test()
                return
            elif imput == "ifft":
                self.ifft_test()
                return
            elif imput == "all":
                self.fft_test()
                self.rft_test()
                self.ifft_test()
                self.irft_test()
                print("All tests complete")
                return
            else:
                print("Invalid input")

    def test_specifications(self, test_num: int = -1):
        """this function prints the specifications of the test"""

        if test_num == -1:
            print()
            print("test specifications: ")
            print("    duration of wave: " + str(self.duration) + " seconds")
            print("    sample rate: " + str(self.sample_rate) + " samples per second")
            print("    samples: " + str(self.samples))
            if self.samples == 1:
                print(
                    "    frequencies of composite signal (in hz): "
                    + ", ".join([str(x) + "hz" for x in self.signal[1]])
                )
            else:
                test_num = -2
            print()
        elif test_num >= 0:
            # in this case, we only ever print out the testnumber that is given in the function call
            print()
            print("failed test number: " + str(test_num))
            print(
                "    frequencies of composite signal (in hz): "
                + ", ".join([str(x) + "hz" for x in self.frequencies_list[test_num]])
            )

    def fft_test(self):
        """this function tests the home made fast fourier transform function using the scipy fft function if details are true, it will run a time and memory test as well"""
        if self.details:
            print()
            print("unit test starting for algorithm:  fast fourier transform")
            print()
            self.test_specifications()

        start_time = time.time()
        if self.samples == 1:
            transform = fast_fourier_transform(self.signal[0])
            end_time = time.time()
            time_taken = end_time - start_time
            memory_use_list_over_function_duration = memory_usage(
                (fast_fourier_transform, (self.signal[0],), {})
            )
            if self.details:
                print("time taken: " + str(time_taken) + " seconds")
                print(
                    "memory usage: "
                    + str(
                        memory_use_list_over_function_duration[-1]
                        - memory_use_list_over_function_duration[0]
                    )
                    + "MB"
                )
        else:
            transforms = [
                fast_fourier_transform(self.signal_list[i]) for i in range(self.samples)
            ]
            end_time = time.time()
            time_taken = end_time - start_time
            memory_use_list_over_function_duration = memory_usage(
                (fast_fourier_transform, (self.signal_list[0],), {})
            )
            mem_use = (
                memory_use_list_over_function_duration[-1]
                - memory_use_list_over_function_duration[0]
            )

            if self.details:
                print("total time taken: " + str(time_taken) + " seconds")
                if mem_use == 0:
                    print(
                        "ERROR: memory usage is about 0MB, this is likely due to the fact that the function has already been called once before this test, please fully stop the program and run it again"
                    )
                else:
                    print(
                        "Average memory usage over each function call: "
                        + str(mem_use)
                        + "MB"
                    )

    def rft_test(self):
        """this function tests the home made regular fourier transform function using the scipy fft function. If details are requested, it will run a time and memory test as well"""
        if self.details:
            print()
            print("unit test starting for algorithm:  regular fourier transform")
            print()
            self.test_specifications()

        start_time = time.time()
        if self.samples == 1:
            transform = regular_fourier_transform(self.signal[0])
            end_time = time.time()
            time_taken = end_time - start_time
            memory_use_list_over_function_duration = memory_usage(
                (regular_fourier_transform, (self.signal[0],), {})
            )

            if self.details:
                print("time taken: " + str(time_taken) + " seconds")
                print(
                    "memory usage: "
                    + str(
                        memory_use_list_over_function_duration[-1]
                        - memory_use_list_over_function_duration[0]
                    )
                    + "MB"
                )

        else:
            transforms = [
                regular_fourier_transform(self.signal_list[i])
                for i in range(self.samples)
            ]
            end_time = time.time()
            time_taken = end_time - start_time
            memory_use_list_over_function_duration = memory_usage(
                (regular_fourier_transform, (self.signal_list[0],), {})
            )
            mem_use = (
                memory_use_list_over_function_duration[-1]
                - memory_use_list_over_function_duration[0]
            )

            if self.details:
                print("total time taken: " + str(time_taken) + " seconds")
                if mem_use == 0:
                    print(
                        "ERROR: memory usage is about 0MB, this is likely due to the fact that the function has already been called once before this test, please fully stop the program and run it again"
                    )
                else:
                    print(
                        "Average memory usage over each function call: "
                        + str(mem_use)
                        + "MB"
                    )

    def ifft_test(self):
        """this function tests the home made inverse fast fourier transform function using the scipy ifft function if details are true, it will run a time and memory test as well"""
        if self.details:
            print()
            print("unit test starting for algorithm:  inverse fast fourier transform")
            print()
            self.test_specifications()

        start_time = time.time()
        if self.samples == 1:
            inverse_fast_fourier_transform(self.fourier_transform)
            end_time = time.time()
            time_taken = end_time - start_time
            memory_use_list_over_function_duration = memory_usage(
                (inverse_fast_fourier_transform, (self.fourier_transform,), {})
            )
            if self.details:
                print("time taken: " + str(time_taken) + " seconds")
                print(
                    "memory usage: "
                    + str(
                        memory_use_list_over_function_duration[-1]
                        - memory_use_list_over_function_duration[0]
                    )
                    + "MB"
                )
        else:
            for i in range(self.samples):
                inverse_fast_fourier_transform(self.fourier_transform_list[i])

            end_time = time.time()
            time_taken = end_time - start_time
            memory_use_list_over_function_duration = memory_usage(
                (inverse_fast_fourier_transform, (self.fourier_transform_list[0],), {})
            )
            mem_use = (
                memory_use_list_over_function_duration[-1]
                - memory_use_list_over_function_duration[0]
            )

            if self.details:
                print("total time taken: " + str(time_taken) + " seconds")
                if mem_use == 0:
                    print(
                        "ERROR: memory usage is about 0MB, this is likely due to the fact that the function has already been called once before this test, please fully stop the program and run it again"
                    )
                else:
                    print(
                        "Average memory usage over each function call: "
                        + str(mem_use)
                        + "MB"
                    )

    def irft_test(self):
        """this function tests the home made inverse regular fourier transform function using the scipy ifft function. If details requested, it will run a time and memory test as well"""
        if self.details:
            print()
            print(
                "unit test starting for algorithm:  inverse regular fourier transform"
            )
            print()
            self.test_specifications()

        start_time = time.time()
        if self.samples == 1:
            inverse_regular_fourier_transform(self.fourier_transform)
            end_time = time.time()
            time_taken = end_time - start_time
            memory_use_list_over_function_duration = memory_usage(
                (inverse_regular_fourier_transform, (self.fourier_transform,), {})
            )

            if self.details:
                print("time taken: " + str(time_taken) + " seconds")
                print(
                    "memory usage: "
                    + str(
                        memory_use_list_over_function_duration[-1]
                        - memory_use_list_over_function_duration[0]
                    )
                    + "MB"
                )

        else:
            for i in range(self.samples):
                inverse_regular_fourier_transform(self.fourier_transform_list[i])

            end_time = time.time()
            time_taken = end_time - start_time
            memory_use_list_over_function_duration = memory_usage(
                (
                    inverse_regular_fourier_transform,
                    (self.fourier_transform_list[0],),
                    {},
                )
            )
            mem_use = (
                memory_use_list_over_function_duration[-1]
                - memory_use_list_over_function_duration[0]
            )

            if self.details:
                print("total time taken: " + str(time_taken) + " seconds")
                if mem_use == 0:
                    print(
                        "ERROR: memory usage is about 0MB, this is likely due to the fact that the function has already been called once before this test, please fully stop the program and run it again"
                    )
                else:
                    print(
                        "Average memory usage over each function call: "
                        + str(mem_use)
                        + "MB"
                    )

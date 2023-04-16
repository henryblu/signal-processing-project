from transforms import *
from visualisations import *
from scipy.fft import fft, ifft
from scipy.fft import fftfreq, rfftfreq
from memory_profiler import memory_usage
import time
import numpy as np

class performance_test():

    def __init__(self, duration = 1, sample_rate = 256, details = False, samples = 1,):
        self.duration = duration
        self.sample_rate = sample_rate
        self.details = details
        self.samples = samples
        if self.samples == 1:
            self.signal = self.test_wave_generation()
            self.fourier_transform = fft(self.signal[0])
            self.inverse_transform = ifft(self.fourier_transform)
        else:
            self.signals_and_frequencies = [self.test_wave_generation() for i in range(self.samples)]
            self.signal_list = [self.signals_and_frequencies[i][0] for i in range(self.samples)]
            self.frequencies_list = [self.signals_and_frequencies[i][1] for i in range(self.samples)]
            self.fourier_transform_list = [fft(self.signal_list[i]) for i in range(self.samples)]
            self.inverse_transform_list = [ifft(self.fourier_transform_list[i]) for i in range(self.samples)]

    def test_specifications(self, test_num:int = -1):
        ''' this function prints the specifications of the test (is only called if details is true)
        '''

        if test_num == -1:
            print()
            print('test specifications: ')
            print('    duration of wave: ' + str(self.duration) + ' seconds')
            print('    sample rate: ' + str(self.sample_rate) + ' samples per second')
            print('    samples: ' + str(self.samples))
            if self.samples == 1:
                print("    frequencies of composite signal (in hz): " + ", ".join([str(x) + "hz" for x in self.signal[1]]))
            else:
                test_num = -2
            print()
        elif test_num >= 0:
            # in this case, we only ever print out the testnumber that is given in the function call 
            print()
            print('failed test number: ' + str(test_num))        
            print('    frequencies of composite signal (in hz): ' + ", ".join([str(x) + "hz" for x in self.frequencies_list[test_num]]))

    def test_wave_generation(self):
        ''' this function generates a composite wavfe of three random waves of a given sample rate and duration
        '''
        # generate a sin wave with a randome frequency
        duration = self.duration
        sample_rate = self.sample_rate
        frequency_list = [np.random.randint(1, 1000), np.random.randint(1, 1000), np.random.randint(1, 1000)]
        signal_1 = np.sin(2*np.pi*frequency_list[0]*np.arange(sample_rate*duration)/sample_rate)
        signal_2 = np.sin(2*np.pi*frequency_list[1]*np.arange(sample_rate*duration)/sample_rate)
        signal_3 = np.sin(2*np.pi*frequency_list[2]*np.arange(sample_rate*duration)/sample_rate)
        composite_signal = signal_1 + signal_2 + signal_3
        return (composite_signal, frequency_list)

    def fft_test(self):
        ''' this function tests the home made fast fourier transform function using the scipy fft function if details are true, it will run a time and memory test as well
        '''
        print('unit test starting for algorithm:  fast fourier transform')

        if self.details:
            self.test_specifications()
            start_time = time.time()
            if self.samples == 1:
                transform = fast_fourier_transform(self.signal[0])
                end_time = time.time()
                if np.allclose(transform, self.fourier_transform):
                    print('fft function passed test = working correctly')
                else:
                    print('fft function failed test = not working correctly')
                time_taken = end_time - start_time
                print ('time taken: ' + str(time_taken) + ' seconds')
                memory_use_list_over_function_duration = memory_usage((fast_fourier_transform, (self.signal[0],), {}))
                print('memory usage: ' + str(memory_use_list_over_function_duration[-1]-memory_use_list_over_function_duration[0]) + 'MB')
            
            else: 
                transforms = [fast_fourier_transform(self.signal_list[i]) for i in range(self.samples)]
                end_time = time.time()
                if np.allclose(transforms, self.fourier_transform_list):
                    print('fft function passed all tests = working correctly')
                else:
                    print('fft function failed following tests:')
                    for i in range(self.samples):
                        if not np.allclose(transforms[i], self.fourier_transform_list[i]):
                            self.test_specifications(i)
                        
                time_taken = end_time - start_time
                print ('total time taken: ' + str(time_taken) + ' seconds')

                memory_use_list_over_function_duration = memory_usage((fast_fourier_transform, (self.signal_list[0],), {}))
                mem_use = (memory_use_list_over_function_duration[-1]-memory_use_list_over_function_duration[0])
                if mem_use == 0:
                    print('ERROR: memory usage is about 0MB, this is likely due to the fact that the function has already been called once before this test, please fully stop the program and run it again')
                else:
                    print('Average memory usage over each function call: ' + str(mem_use) + 'MB')
                
        else:
            if self.samples == 1:
                transform = fast_fourier_transform(self.signal[0])
                if np.allclose(transform, self.fourier_transform):
                    print('fft function passed test = working correctly')
                else:
                    print('fft function failed test = not working correctly')
            else:
                transforms = [fast_fourier_transform(self.signal_list[i]) for i in range(self.samples)]
                if np.allclose(transforms, self.fourier_transform_list):
                    print('fft function passed test = working correctly')
                else:
                    print('fft function failed test = not working correctly')

    def rft_test(self):
        ''' this function tests the home made regular fourier transform function using the scipy fft function. If details are requested, it will run a time and memory test as well
        '''
        print('unit test starting for algorithm:  regular fourier transform')

        if self.details:
            self.test_specifications()
            start_time = time.time()
            if self.samples == 1:
                transform = regular_fourier_transform(self.signal[0])
                end_time = time.time()
                if np.allclose(transform, self.fourier_transform):
                    print('rft function passed test = working correctly')
                else:
                    print('rft function failed test = not working correctly')
                time_taken = end_time - start_time
                print ('time taken: ' + str(time_taken) + ' seconds')
                memory_use_list_over_function_duration = memory_usage((regular_fourier_transform, (self.signal[0],), {}))
                print('memory usage: ' + str(memory_use_list_over_function_duration[-1]-memory_use_list_over_function_duration[0]) + 'MB')
            
            else: 
                transforms = [regular_fourier_transform(self.signal_list[i]) for i in range(self.samples)]
                end_time = time.time()
                if np.allclose(transforms, self.fourier_transform_list):
                    print('rft function passed all tests = working correctly')
                else:
                    print('rft function failed following tests:')
                    for i in range(self.samples):
                        if not np.allclose(transforms[i], self.fourier_transform_list[i]):
                            self.test_specifications(i)
                        
                time_taken = end_time - start_time
                print ('total time taken: ' + str(time_taken) + ' seconds')

                memory_use_list_over_function_duration = memory_usage((regular_fourier_transform, (self.signal_list[0],), {}))
                mem_use = (memory_use_list_over_function_duration[-1]-memory_use_list_over_function_duration[0])
                if mem_use == 0:
                    print('ERROR: memory usage is about 0MB, this is likely due to the fact that the function has already been called once before this test, please fully stop the program and run it again')
                else:
                    print('Average memory usage over each function call: ' + str(mem_use) + 'MB')
                
        else:
            if self.samples == 1:
                transform = regular_fourier_transform(self.signal[0])
                if np.allclose(transform, self.fourier_transform):
                    print('rft function passed test = working correctly')
                else:
                    print('rft function failed test = not working correctly')
            else:
                transforms = [regular_fourier_transform(self.signal_list[i]) for i in range(self.samples)]
                if np.allclose(transforms, self.fourier_transform_list):
                    print('rft function passed test = working correctly')
                else:
                    print('rft function failed test = not working correctly')

    def ifft_test(self):
        ''' this function tests the home made inverse fast fourier transform function using the scipy ifft function if details are true, it will run a time and memory test as well
        '''
        print('unit test starting for algorithm:  inverse fast fourier transform')

        if self.details:
            self.test_specifications()
            start_time = time.time()

            if self.samples == 1:
                home_inverse_transform = inverse_fast_fourier_transform(self.fourier_transform)
                end_time = time.time()
                if np.allclose(home_inverse_transform, self.inverse_transform):
                    print('ifft function passed test = working correctly')
                else:
                    print('ifft function failed test = not working correctly')
                    difference = home_inverse_transform - self.inverse_transform
                    print('difference between home made ifft and scipy ifft: ' + str(difference))
                time_taken = end_time - start_time
                print ('time taken: ' + str(time_taken) + ' seconds')
                memory_use_list_over_function_duration = memory_usage((inverse_fast_fourier_transform, (self.fourier_transform,), {}))
                print('memory usage: ' + str(memory_use_list_over_function_duration[-1]-memory_use_list_over_function_duration[0]) + 'MB')
            
            else: 
                home_inverse_transforms = [inverse_fast_fourier_transform(self.fourier_transform_list[i]) for i in range(self.samples)]
                end_time = time.time()
                if np.allclose(home_inverse_transforms, self.inverse_transform_list):
                    print('ifft function passed all tests = working correctly')
                else:
                    print('ifft function failed following tests:')
                    for i in range(self.samples):
                        if not np.allclose(home_inverse_transforms[i], self.inverse_transform_list[i]):
                            self.test_specifications(i)
                        
                time_taken = end_time - start_time
                print ('total time taken: ' + str(time_taken) + ' seconds')

                memory_use_list_over_function_duration = memory_usage((inverse_fast_fourier_transform, (self.fourier_transform_list[0],), {}))
                mem_use = (memory_use_list_over_function_duration[-1]-memory_use_list_over_function_duration[0])
                if mem_use == 0:
                    print('ERROR: memory usage is about 0MB, this is likely due to the fact that the function has already been called once before this test, please fully stop the program and run it again')
                else:
                    print('Average memory usage over each function call: ' + str(mem_use) + 'MB')
                
        else:
            if self.samples == 1:
                home_inverse_transform = inverse_fast_fourier_transform(self.fourier_transform)
                if np.allclose(home_inverse_transform, self.inverse_transform):
                    print('ifft function passed test = working correctly')
                else:
                    print('ifft function failed test = not working correctly')
            else:
                home_inverse_transforms = [inverse_fast_fourier_transform(self.fourier_transform_list[i]) for i in range(self.samples)]
                if np.allclose(home_inverse_transforms, self.inverse_transform_list):
                    print('ifft function passed test = working correctly')
                else:
                    print('ifft function failed test = not working correctly')
        print()

    def irft_test(self):
        ''' this function tests the home made inverse regular fourier transform function using the scipy ifft function. If details requested, it will run a time and memory test as well
        '''

        print('unit test starting for algorithm:  inverse regular fourier transform')

        if self.details:
            self.test_specifications()
            start_time = time.time()

            if self.samples == 1:
                home_inverse_transform = inverse_regular_fourier_transform(self.fourier_transform)
                end_time = time.time()
                if np.allclose(home_inverse_transform, self.inverse_transform):
                    print('irft function passed test = working correctly')
                else:
                    print('irft function failed test = not working correctly')
                    difference = home_inverse_transform - self.inverse_transform
                    print('difference between home made irft and scipy ifft: ' + str(difference))
                time_taken = end_time - start_time
                print ('time taken: ' + str(time_taken) + ' seconds')
                memory_use_list_over_function_duration = memory_usage((inverse_regular_fourier_transform, (self.fourier_transform,), {}))
                print('memory usage: ' + str(memory_use_list_over_function_duration[-1]-memory_use_list_over_function_duration[0]) + 'MB')
            
            else: 
                inverse_transforms = [inverse_regular_fourier_transform(self.fourier_transform_list[i]) for i in range(self.samples)]
                end_time = time.time()
                if np.allclose(inverse_transforms, self.inverse_transform_list):
                    print('irft function passed all tests = working correctly')
                else:
                    print('irft function failed following tests:')
                    for i in range(self.samples):
                        if not np.allclose(inverse_transforms[i], self.inverse_transform_list[i]):
                            self.test_specifications(i)
                        
                time_taken = end_time - start_time
                print ('total time taken: ' + str(time_taken) + ' seconds')

                memory_use_list_over_function_duration = memory_usage((inverse_regular_fourier_transform, (self.fourier_transform_list[0],), {}))
                mem_use = (memory_use_list_over_function_duration[-1]-memory_use_list_over_function_duration[0])
                if mem_use == 0:
                    print('ERROR: memory usage is about 0MB, this is likely due to the fact that the function has already been called once before this test, please fully stop the program and run it again')
                else:
                    print('Average memory usage over each function call: ' + str(mem_use) + 'MB')
                
        else:
            if self.samples == 1:
                home_inverse_transform = inverse_regular_fourier_transform(self.fourier_transform)
                if np.allclose(home_inverse_transform, self.inverse_transform):
                    print('irft function passed test = working correctly')
                else:
                    print('irft function failed test = not working correctly')
            else:
                home_inverse_transforms = [inverse_regular_fourier_transform(self.fourier_transform_list[i]) for i in range(self.samples)]
                if np.allclose(home_inverse_transforms, self.inverse_transform_list):
                    print('irft function passed test = working correctly')
                else:
                    print('irft function failed test = not working correctly')
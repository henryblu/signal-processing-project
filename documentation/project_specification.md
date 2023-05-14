# Project Specification Document
### Degree Programme: **Bachelor in Science**
### Documentation Language: **English** 
### Coding Language: **Python** 

## Problem:
In this project, I make a program that implements sound wave alterations on a given sound wave. This is done using fourier transforms and simple wave alterations. The program will be able to read in a .wav file and output a .wav file with the altered sound wave. The user will be able to specify the alterations they want to make to the sound wave. 
</n>
The fowing alterations are available in this program:
1. Noise reduction
    this is done by filtering out the low power noise in the wave. The user can specify the threshold of the noise reduction.
2. high pitch frequency reduction
    this is done by filtering out the high pitch frequencies in the wave. The user can specify the threshold of the high pitch frequency reduction.
3. low pitch frequency reduction
    this is done by filtering out the low pitch frequencies in the wave. The user can specify the threshold of the low pitch frequency reduction.

## Datastructures and Algorithms Choice:
This project will mainly focus on a set of fourier transformation algorithms. 
#### The following algorithms are used in this project:
1. Discrete Fourier transform (DFT) 
2. Inverse Discrete Fourier transform (IDFT)
3. Cooly Turky Fast Fourier transform (hereby Fast Fourier Transform (FFT))
4. Inverse Fast Fourier transform (IFFT)
3. Bluestein's FFT

The reason for choosing fourier transformations is that they are able to decompose a sound wave into its constituent frequencies, and then recompose the frequencies back into a sound wave. This allows for us to alter the sound wave by filtering out certain frequencies. As for the choice of individual algorithms, I chose to implement the DFT and FFT algorithms as they are the most common fourier transformation algorithms. Furthermore I also chose to implement Bluestein's FFT as it is the most efficient FFT algorithm for non-power-of-two sized data sets (which almost all data is).

#### The following data structures are used in this project:
1. numpy arrays.
2. python lists.

For datastrucutres, all data will be stored in the basic python list and in the python library numpy's array data structure. This choice was made as both lists and numpy arrays are simple to use. However, numpy arrays are used for larger data strucutes as they allow for a variety of data types and have some fast builtin methods.


## Program Input and use:
- the input will be a sample sound wave stored in a .wav file. wav files store their data in an array of the form: [sample_rate:int, [intensity_values:int]] 
- the input sound wave will be run through the fourier transformation algorithms and then altered using the alteration functions, finally the altered sound wave will be run through the inverse fourier transformation algorithms and outputted as a .wav file. 

## time and space complexity:
*Here for all algorithms n is the number of data points in the sound wave.*

- Discrete Fourier transform
    - average time complexity: O(n^2)
    - worst case time complexity: O(n^2)
    - space complexity: O(n)

- Inverse Discrete Fourier transform
    - average time complexity: O(n^2)
    - worst case time complexity: O(n^2)
    - space complexity: O(n)

- Fast Fourier transform
    - average time complexity: O(n*log(n))
    - worst case time complexity: O(n^2)
    - space complexity: O(n)

- BlueStein's Fast forier transform
    - average time complexity: O(n*log(n))
    - worst case time complexity: O(n^2)
    - space complexity: O(n)

- Inverse Fast forier transform
    - average time complexity: O(n*log(n))
    - worst case time complexity: O(n^2)
    - space complexity: O(n)

Firstly, to process the sound wave, I will use a regular Fourier transformation which is very time inefficient given the large size of noise waves. Then, I filter out the noise of the sound wave using different cutoff thresholds to represent more and less noise filtering. The noise wave then undergoes an inverse Fourier transform and is visualised using a pychart.
Finally, the same process is done using a fast Fourier transformation algorithm and the time and space requirements for the two programs are compared. 

## Sources:
- Driven Science and Engineering: Machine Learning, Dynamical Systems, and Control 1st Edition by Steven L. Brunton & J. Nathan Kutz (chapter 2)
- Noise cancellation with Python and Fourier Transform: https://towardsdatascience.com/noise-cancellation-with-python-and-fourier-transform-97303314aa71
- Bluestein's FFT Algorithm: https://ccrma.stanford.edu/~jos/st/Bluestein_s_FFT_Algorithm.html
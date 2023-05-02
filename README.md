[![codecov](https://codecov.io/gh/henryblu/signal-processing-project/branch/main/graph/badge.svg?token=05TLDCQDNI)](https://codecov.io/gh/henryblu/signal-processing-project)
# Project Specification Document
### Degree Programme: **Bachelor in Science**
### Documentation Language: **English** 
### Coding Language: **Python** 

<br>

## Problem and Algorithm Choice 
In this project, I make a program that implements noise filtering on a sound wave using Fourier transforms. In this project, I investigate the following algorithms: the Discrete Fourier transform (DFT) and Fast Fourier transform (FFT). The program takes in a sample noisy input wave and outputs graphs of the same wave with different noise cancellation thresholds using my own Fourier transform program. For testing, I used the python library Scripty's DFT  and FFT algorithms and compared their output and efficiency. 


## Program Input
- the input will be a sample radio wave stored in a matrix of time/power pairs. 

## Data structures and algorithms
- Fourier transform 
- Fast forier transform

Firstly, to process the sound wave, I will use a regular Fourier transformation which is very time inefficient given the large size of noise waves. Then, I filter out the noise of the sound wave using different cutoff thresholds to represent more and less noise filtering. The noise wave then undergoes an inverse Fourier transform and is visualised using a pychart.
Finally, the same process is done using a fast Fourier transformation algorithm and the time and space requirements for the two programs are compared. 

## Time complexity
Fourier transformations require O(n^2) time complexity and O(n) space complexity. Here, n is the number of data points in the radio wave.
Fast Fourier transformations require an O(n^2)to O(n*log(n)) time complexity and O(n) space complexity. Once again, here n is the number of data points in the radio wave.
Hilbert transformation inherits the regular Fourier transformation time and space complexity of O(n^2) and O(n). 

## Sources:
Driven Science and Engineering: Machine Learning, Dynamical Systems, and Control 1st Edition by Steven L. Brunton & J. Nathan Kutz (chapter 2)
Noise cancellation with Python and Fourier Transform https://towardsdatascience.com/noise-cancellation-with-python-and-fourier-transform-97303314aa71

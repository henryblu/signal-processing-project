[![codecov](https://codecov.io/gh/henryblu/signal-processing-project/branch/main/graph/badge.svg?token=05TLDCQDNI)](https://codecov.io/gh/henryblu/signal-processing-project)

# Testing

## Unit testing:

to run unit testing run the following command in the terminal from the root directory:
```python -m pytest```

### Coverage Report:
![img](/documentation/test_coverage/coverage_report.png)


### Unit testing contents and strucutre:
There are four testing files which test the classes and functions in src/services: 
- ```test_data_processing.py``` with ```TestAudioFileProcessing()``` class for testing ```AudioFileProcessing()``` class 
- ```test_sample_wave.py``` with ```TestSampleWave()``` class for testing ```SampleWave()``` class.
- ```test_transforms.py``` with ```TestTransforms()``` class for testing ```Transforms()``` class.
- ```test_transform_alternations.py``` with ```TestTransformAlternations()``` class for testing the functions in ```transform_alternations.py````.

Testing is not run on UI elements such as ```flags.py``` and ```visualisations.py``` as these files are graphical and thus should be tested by user vvision rather then unit tests.

This Program runs all unit testing using the ```unittest``` library by default with some individual tests being run using the pytest library functions. Functions of the classes are tested using exemplary input. 

the following functions are used for individual unit tests:
1. ```pytest.raises``` for testing errors calls such as ```ValueError``` and ```FileError``` and their outputs.
2. ```.assert np.allclose``` is used to compare list outputs to their correct couterparts.
3. ```.assertEqual()``` is used for comparing expected and returned values,
4. ```.assertTrue()``` is used for checking the Boolean values of variables.
5. ```assert np.all``` is used for checking the Boolean values of lists.

## Performance testing:
the performance tests can be run from the file ```performance_testing.py``` in the src/tests/ directory.
### Performance testing results:
<p align="center">
<img src="graph_analysis\all.png" width="500">
<img src="graph_analysis\bluestines_fft vs fft.png" width="500">
<img src="graph_analysis\bluestines_fft vs ifft.png" width="500">
<img src="graph_analysis\rft vs bluestines_fft.png" width="500">
<img src="graph_analysis\rft vs irft.png" width="500">
</p>

### Performance testing contents and strucutre:
The results of the performance testing are presented in the graphs above.

Performance tests have been generate for each of the following algorithms:
1. regular fourier transform
2. fast fourier transform
3. bluestines fast fourier transform
4. inverse regular fourier transform
5. inverse fast fourier transform

Each algorithm has been tested and assesed by measuting the time it takes to return the expected output. Performance testing has been done using ```time``` library. The time was measured by capturing ```start_time = time.time()``` at the beginning of the function call and ```end_time = time.time()``` after the function halts. 

### General performance testing observations:
1. the fast fourier transform only works with arrays of length 2^n.
2. Bluestines fast fourier transform and the fast fourier tranform have a realitive time complexity of O(nlog(n)) however as bluestines algorithm requires padding the input array with zeros, it is slightly slower then the fast fourier transform.
3. the regular fourier transform has a time complexity of O(n^2) and is thus much slower then the fast fourier transform.
4. the inverse fast fourier transform and the inverse regular fourier transform have the same time complexity as their counterparts.
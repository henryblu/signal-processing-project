# User Guide

## Program Execusion and dependencies 

1. close repository 
2. install base packages:

    Program interpreter: python (>=3.9,<=3.11)
    - for installation refer to: https://www.python.org/downloads/

    Dependency Installer: Poetry (version 1.4.2)
    - for installation refer to: https://python-poetry.org/docs/

3. install dependencies using poetry using comand:
        
        poetry install

- now you should be ready to run the program!

## Executalbes

starting from path/to/repository/signal-processing-project/

- To execute this program please run: 

        poetry run python src/ui/main.py 

- there are a number of flags that can be set, to discover them use:

        poetry run python src/ui/main.py -h

- if you want to run the test suite, please run: 

        pytest src



## Program inputs

- using the --input flag, you can specify the input .wav file you want to decompose
        
        *#1 at the moment, the fast fourier transform only works with files which have a length which is power of two
        *#2 regular fourier transforms are really, really slow for imputs, so watch out. 


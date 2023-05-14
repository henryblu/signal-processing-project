# User Guide

## Program Execusion and dependencies 

1. close repository 
2. install base packages:

    Program interpreter: python (>=3.9,<=3.11)
    - for installation refer to: https://www.python.org/downloads/

    Dependency Installer: Poetry (version 1.4.2)
    - for installation refer to: https://python-poetry.org/docs/

3. install dependencies using poetry using comand:
        
        ```poetry install```

- now you should be ready to run the program!

## Executalbes

starting from path/to/repository/signal-processing-project/

- To execute this program please run: 

        ```poetry run python src/ui/main.py```

- there are a number of flags that can be set, to discover them use:

        ```poetry run python src/ui/main.py -h```

- if you want to run the test suite, please run: 

        ```python -m pytest```


## Program inputs

- using the --input flag, you can specify the input .wav file you want to decompose and alter.
        limited to .wav files
        limited to files of size less then 70000 data points

        For example:
                ```poetry run python src/ui/main.py --input src/data/StarWars3.wav```
        will run the program on the StarWars3.wav file in the src/data/ directory.

- if no input is specified, the program will generate a random composite wave of 3 frequencies.

## Program outputs

- using the --output flag, you can specify the output .wav file you want to save the altered wave to.
        limited to .wav files
        limited to files of size less then 70000 data points

        For example:
                ```poetry run python src/ui/main.py --output src/data/StarWars3.wav```
        will save the output of the program to the StarWars3.wav file in the src/data/ directory.






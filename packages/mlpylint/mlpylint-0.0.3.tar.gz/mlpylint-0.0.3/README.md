# mlpylint

A static code analyzer tool for identifying ml-specific code smells.

## Description

MLpylint is a static code analyzer designed specifically for Python applications. Drawing from extensive research in the
field of ML-specific code smells, MLpylint focuses on identifying ML-specific issues in your code. This assists in
enhancing the readability, maintainability, and efficiency of your ML codebase, ensuring it adheres to best practices in
the field of artificial intelligence and machine learning software development.

## Getting started

The project structure is organized into three main components:

1. Code Smell Checkers: These are the core of our tool, designed to identify specific code smells in your Python scripts.

2. Test Scripts: Each code smell checker comes with an associated test script. These are used to validate the functionality of each checker, ensuring it correctly identifies its corresponding code smell.

3. Code Smell Test Files: These are Python scripts that contain examples of code smells. They serve as practical test cases for the code smell checkers, helping to ensure that the checkers are accurately identifying the intended code smells.

This organization allows for easy identification of different aspects of the tool, facilitating testing, extension, and maintenance.


## Installation

```
cd mlpylint
py -m venv venv
source venv/Scripts/activate
pip install -e .[dev]
```

## Update PyPI Package

```
=== Token required from PyPI ===
Create .pypirc file in C:\Users\<user_name> with pypi token parameters

=== In project root dir ===
py -m pip install --upgrade pip
py -m pip install --upgrade build
py -m build
py -m pip install --upgrade twine
py -m twine upload dist/*

```

## Usage

```
$ mlpylint --help                          # View tool options
$ mlpylint <path>                          # Check for code smells (CS)
$ mlpylint -a,  --advice <path>            # Check for code smells (CS) and include advisory results (CSA)
$ mlpylint -ls, --list-smells              # List all available code smells
$ mlpylint -ds, --describe-smell <id>      # Get code smell description by id
$ mlpylint -c,  --color <path>             # Enable colorized analysis output
```

## Analysis assumptions:

- Imports and ImportFrom are done at the top of the .py file. It is considered a best practice to put all import
  statements at the top of a Python file. This makes it easier to read and understand the dependencies of the file, and
  can help prevent issues with circular imports.


## Author

Peter Hamfelt - [peter.hamfelt@gmail.com, pehd16@student.bth.se]

## Acknowledgements
This work is inspired by and built upon the research conducted by the following individuals:

* Haiyin Zhang from AI for Fintech Research, ING, Amsterdam, Netherlands.
* Luís Cruz from Delft University of Technology, Delft, Netherlands.
* Arie van Deursen from Delft University of Technology, Delft, Netherlands.

Their contribution towards identifying and categorizing "Code Smells for Machine Learning Applications" has played a
crucial role in the development of this tool. I would like to express my deepest gratitude for their pioneering work
in this field.

Research link: https://arxiv.org/abs/2203.13746

## License

MIT License

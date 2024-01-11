# Lab: Class 3 - File IO and Exceptions

## Author: Xin Deng, chatGPT

## Links and Resources

- chatGPT on how to use tuple, .format, .strip, and what raising exceptions meant

## Overview - madlib-cli

In this lab assignment you will be creating a command line application which takes advantage of Python’s built in capabilities for reading and writing files.



## Feature Tasks and Requirements

- Create a local git repo with project named madlib-cli and root folder madlib_cli
- Create a new repository named madlib-cli.
- Link your local and remote repositories.

1. Create a file called madlib.py at root of madlib_cli folder, which will contain all of the Python code that you will write relating to your Madlib game.
2. Keeping in mind the concept of Single Responsibility Principle, build a command line tool which will perform the following:
    - Print a welcome message to the user, explaining the Madlib process and command line interactions
    - Read a template Madlib file (Example), and parse that file into usable parts.
    - Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
    - With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
    - After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
    - Write the completed text (Example)to a new file on your file system (in the repo).
    - Note: A smaller example file is included as well which can be handy when developing/testing.
3. Create and test a read_template function that takes in a path to text file and returns a stripped string of the file’s contents.
read_template should raise a FileNotFoundError if path is invalid.
4. Create and test a parse_template function that takes in a template string and returns a string with language parts removed and a separate tuple of those language parts.
5. Create and test a merge function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.


## Setup

### Creating Project

```bash
mkdir example-lab
cd example-lab
touch README.md
```

### Create virtual environment

```bash
python3 -m venv .venv
```

### Activate virtual environment

#### Mac/Linux

```bash
source .venv/bin/activate
```

### Git

#### On Local System

#### Initialize local Git repository

```bash
git init
touch .gitignore
```

Add `.venv` folder to `.gitignore`

```bash
git add .
git commit -m "first commit"
```

#### On GitHub site

- Create an EMPTY repository `example-lab` on GitHub. 
  - DO NOT initialize with README, license, or gitignore. Those will be added soon.
  - The next screen will have a "Quick Setup" section with a URL available to copy. Copy it ;)

#### On Local System (again)

```bash
git remote add origin the_url_you_copied_that_ends_with_git
git push -u origin main
```

#### Create modules and scripts

- mkdir example_lab

- touch example_lab/example_script.py


#### Install packages

```For example:

pip install favorite-library

Record package dependencies
pip freeze > requirements.txt

Should result in this file tree:

└── example-lab
    ├── README.md
    ├── requirements.txt
    └── example_lab
        └── example_script.py

```      

### Tests

Many labs will require automated testing. If your lab requires it then install `pytest` or `pytest-watch`.

`pip install pytest` # or pytest-watch

`pip freeze > requirements.txt`

`touch tests/__init__.py `(Note: 2 underscores on both sides.)

`touch tests/test_example.py`

Should result in a file tree like this:

```└── example-lab
    ├── README.md
    ├── requirements.txt
    ├── example_lab
    │   └── example_script.py
    └── tests
        ├── __init__.py
        └── test_example.py
```
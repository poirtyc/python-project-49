### Hexlet tests and linter status:
[![Actions Status](https://github.com/poirtyc/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/poirtyc/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/ad4e5460b75269211f60/maintainability)](https://codeclimate.com/github/poirtyc/python-project-49/maintainability)

Welcome to Brain-games project
In each game the user is asked a question, the user needs to enter the answer from the keyboard. 
The game always lasts up to three points if the user hits three questions in a row - he won, 
if the user misses the game will interrupt and tell which answer was correct.

The project has 5 games:
- brain-even
- brain-calc
- brain-gcd
- brain-progression
- brain-prime

### How to install:
1. Install Python: Make sure you have Python 3.10 or later installed on your computer.

You can download it from the official [Python website](https://www.python.org/downloads/).

2. Install Poetry: This project uses Poetry to manage dependencies

Install Poetry by running

3. Than write name game in comand line (Example `brain-even` or `brain-calc`)

curl -sSL https://install.python-poetry.org | python3 -

4. Open a terminal and clone the project repository from GitHub:

git clone https://github.com/yourusername/python-project-49.git
cd python-project-49

5.Once inside the project folder, install the dependencies:

poetry install

6. After installation, activate the virtual environment provided by Poetry:

poetry shell

To play a specific game, use one of the following commands in the terminal:\
	•	brain-even: python -m brain_games.scripts.brain_even\
	•	brain-calc: python -m brain_games.scripts.brain_calc\
	•	brain-gcd: python -m brain_games.scripts.brain_gcd\
	•	brain-progression: python -m brain_games.scripts.brain_progression\
	•	brain-prime: python -m brain_games.scripts.brain_prime

Alternatively, you can configure entry points in the pyproject.toml file to make these commands available directly as:

brain-even\
brain-calc\
brain-gcd\
brain-progression\
brain-prime

To enable this, add the following under [tool.poetry.scripts] in your pyproject.toml:

[tool.poetry.scripts]\
brain-even = "brain_games.scripts.brain_even:main"\
brain-calc = "brain_games.scripts.brain_calc:main"\
brain-gcd = "brain_games.scripts.brain_gcd:main"\
brain-progression = "brain_games.scripts.brain_progression:main"\
brain-prime = "brain_games.scripts.brain_prime:main"

After configuring the scripts, install the project as a package:

poetry install

Now, you can run each game directly by its name (e.g., brain-even, brain-calc, etc.).

### How to use:
Write the name of the game in the command line:\
**brain-even**\
The game will ask if the number is even, you have to answer 'yes' if the number\
is even, 'no®  if the number is odd
![Brain-even](/asciinema/Brain-even.gif)

**brain-calc**\
The game will ask a question with mathematical expression, you need to calculate\
the answer in your mind and write it in the field 'your answer'
![Brain-calc](/asciinema/Brain-calc.gif)

**brain-gcd**\
The game will ask a question with two numbers, you need to calculate in your mind\
the largest common divisor and write it in the field 'your answer'
![Brain-gcd](/asciinema/Brain-gcd.gif)

**brain-progression**\
The game will ask a question with mathematical progression, one of the numbers will be skipped,\
you need in mind to calculate the answer and write it in the field 'your answer'\
![Brain-progression](/asciinema/Brain-progression.gif)

**brain-prime**
The game asks a question with one number, the player needs to enter the answer 'yes'\
if the number is prime, or 'no' if the number is not prime.\
(A prime is a natural number, a larger number that has exactly two different\
natural divisors: 1 and the number itself.)
![Brain-prime](/asciinema/Brain-prime.gif)

import random

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_even(number):
    return number % 2 == 0


def generate_number():
    return random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)


def generate_round():
    question = generate_number()
    answer = 'yes' if is_even(question) else 'no'
    return question, answer


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

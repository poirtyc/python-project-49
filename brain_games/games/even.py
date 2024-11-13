import random


def is_even(number):
    return number % 2 == 0


def generate_round():
    question = random.randint(1, 100)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

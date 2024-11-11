import random


def get_random_number():
    return random.randint(1, 100)


def is_even(number):
    return number % 2 == 0


def generate_round():
    question = get_random_number()
    answer = 'yes' if is_even(question) else 'no'
    return question, answer


rules = 'Answer "yes" if the number is even, otherwise answer "no".'

import random

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 10


def get_gcd(first_number, second_number):
    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    return first_number


def generate_round():
    first_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    second_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = f'{first_number} {second_number}'
    answer = str(get_gcd(first_number, second_number))
    return question, answer


RULES = 'Find the greatest common divisor of given numbers.'

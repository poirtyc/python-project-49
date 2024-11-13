import random


def get_gcd(first_number, second_number):
    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    return first_number


def generate_round():
    FIRST_NUMBER = random.randint(1, 10)
    SECOND_NUMBER = random.randint(1, 10)
    question = f'{FIRST_NUMBER} {SECOND_NUMBER}'
    answer = str(get_gcd(FIRST_NUMBER, SECOND_NUMBER))
    return question, answer


RULES = 'Find the greatest common divisor of given numbers.'

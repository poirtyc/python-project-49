import random


def get_gcd(FIRST_NUMBER, SECOND_NUMBER):
    while FIRST_NUMBER != SECOND_NUMBER:
        if FIRST_NUMBER > SECOND_NUMBER:
            FIRST_NUMBER = FIRST_NUMBER - SECOND_NUMBER
        else:
            SECOND_NUMBER = SECOND_NUMBER - FIRST_NUMBER
    return FIRST_NUMBER


def generate_round():
    FIRST_NUMBER = random.randint(1, 10)
    SECOND_NUMBER = random.randint(1, 10)
    question = f'{FIRST_NUMBER} {SECOND_NUMBER}'
    answer = str(get_gcd(FIRST_NUMBER, SECOND_NUMBER))
    return question, answer


RULES = 'Find the greatest common divisor of given numbers.'

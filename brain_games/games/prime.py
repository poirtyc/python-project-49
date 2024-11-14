import random

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def generate_round():
    question = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

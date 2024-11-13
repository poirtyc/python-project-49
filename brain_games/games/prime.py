import random


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
    question = random.randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

from brain_games.utils import get_random_number


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
    question = get_random_number(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'

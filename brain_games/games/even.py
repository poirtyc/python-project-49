from brain_games import utils


def is_even(number):
    return number % 2 == 0


def generate_round():
    question = utils.get_random_number(1, 100)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer


rules = 'Answer "yes" if the number is even, otherwise answer "no".'
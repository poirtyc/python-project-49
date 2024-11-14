import random

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 9


def get_progression(start, step, length_progression=10):
    progression = []
    for i in range(length_progression):
        progression.append(start + i * step)
    return progression


def generate_round():
    start_progression = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    step_progression = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    progression = get_progression(start_progression, step_progression)

    random_index = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    original_value_from_progression = progression[random_index]
    progression[random_index] = '..'

    question = ' '.join(map(str, progression))
    answer = str(original_value_from_progression)
    return question, answer


RULES = 'What number is missing in the progression?'

import random

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 9


def get_progression(start, step, length_progression=10):
    progression = []
    for i in range(length_progression):
        progression.append(start + i * step)
    return progression


def generate_random_progression():
    start_progression = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    step_progression = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    progression = get_progression(start_progression, step_progression)
    return progression


def create_progression_with_missing(progression):
    random_index = random.randint(0, len(progression) - 1)
    original_value = progression[random_index]
    progression[random_index] = '..'
    return progression, original_value


def generate_round():
    progression = generate_random_progression()
    progression_with_missing, original_value = (
        create_progression_with_missing(progression)
    )
    question = ' '.join(map(str, progression_with_missing))
    answer = str(original_value)
    return question, answer


RULES = 'What number is missing in the progression?'

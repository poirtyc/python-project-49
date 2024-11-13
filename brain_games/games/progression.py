import random


def get_progression(start, step, length_progression=10):
    progression = []
    for i in range(length_progression):
        progression.append(start + i * step)
    return progression


def generate_round():
    START_PROGRESSION = random.randint(1, 3)
    STEP_PROGRESSION = random.randint(1, 4)
    progression = get_progression(START_PROGRESSION, STEP_PROGRESSION)

    random_index = random.randint(1, 10)
    original_value_from_progression = progression[random_index]
    progression[random_index] = '..'

    question = ' '.join(map(str, progression))
    answer = str(original_value_from_progression)
    return question, answer


RULES = 'What number is missing in the progression?'

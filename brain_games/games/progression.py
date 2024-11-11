from brain_games import utils


def get_progression():
    progression = []
    progression_num = utils.get_random_number(1, 4)

    progression_lenght = 10
    drive = progression_num

    while progression_lenght > 0:
        progression.append(drive)
        drive += progression_num
        progression_lenght -= 1

    return progression


def generate_round():
    progression = get_progression()
    random_index = utils.get_random_number(0, 9)
    original_value = progression[random_index]
    progression[random_index] = '..'

    question = ' '.join(map(str, progression))
    answer = str(original_value)
    return question, answer


rules = 'What number is missing in the progression?'

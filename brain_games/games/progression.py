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
    number_string = " ".join(map(str, progression))
    random_number_in_progression = str(progression[utils.get_random_number(1, 10)])

    question = number_string.replace(random_number_in_progression, '..')
    answer = random_number_in_progression
    return question, answer


rules = 'What number is missing in the progression?'

from brain_games import utils


def get_gcd(first_num, second_num):

    while first_num != second_num:
        if first_num > second_num:
            first_num = first_num - second_num
        else:
            second_num = second_num - first_num
    return first_num


def generate_round():
    first_num = utils.get_random_number(1, 10)
    second_num = utils.get_random_number(1, 10)
    question = f'{first_num} {second_num}'
    answer = str(get_gcd(first_num, second_num))
    return question, answer


rules = 'Find the greatest common divisor of given numbers.'

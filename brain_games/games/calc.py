from brain_games import utils


operators = {
    1: '+',
    2: '-',
    3: '*',
    4: '/',
}


def calculate(first_operand, second_operand, random_operator):
    match random_operator:
        case '+':
            return first_operand + second_operand
        case '-':
            return first_operand - second_operand
        case '*':
            return first_operand * second_operand
        case '/':
            return first_operand / second_operand


def generate_round():
    first_operand = utils.get_random_number(1, 100)
    second_operand = utils.get_random_number(1, 100)
    random_operator = operators[utils.get_random_number(1, 3)]
    question = f'{first_operand} {random_operator} {second_operand}'
    answer = str(int(calculate(first_operand, second_operand, random_operator)))
    return question, answer


rules = 'What is the result of the expression?'

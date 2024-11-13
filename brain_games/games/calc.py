import random


OPERATORS = ('+', '-', '*')


def calculate(FIRST_OPERAND, SECOND_OPERAND, random_operator):
    match random_operator:
        case '+':
            return FIRST_OPERAND + SECOND_OPERAND
        case '-':
            return FIRST_OPERAND - SECOND_OPERAND
        case '*':
            return FIRST_OPERAND * SECOND_OPERAND


def generate_round():
    FIRST_OPERAND = random.randint(1, 100)
    SECOND_OPERAND = random.randint(1, 100)
    random_operator = OPERATORS[random.randint(0, 2)]
    question = f'{FIRST_OPERAND} {random_operator} {SECOND_OPERAND}'
    answer = str(int(calculate(FIRST_OPERAND, SECOND_OPERAND, random_operator)))
    return question, answer


RULES = 'What is the result of the expression?'

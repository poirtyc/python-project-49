import random


OPERATORS = ('+', '-', '*')
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def calculate(first_operand, second_operand, random_operator):
    match random_operator:
        case '+':
            return first_operand + second_operand
        case '-':
            return first_operand - second_operand
        case '*':
            return first_operand * second_operand


def create_operands_and_operator():
    first_operand = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    second_operand = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    random_operator = OPERATORS[random.randint(0, 2)]
    return first_operand, second_operand, random_operator


def generate_round():
    first_operand, second_operand, random_operator = (
        create_operands_and_operator()
    )
    question = f'{first_operand} {random_operator} {second_operand}'
    answer = str(int(calculate(first_operand, second_operand, random_operator)))
    return question, answer


RULES = 'What is the result of the expression?'

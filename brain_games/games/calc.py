import random
import operator
from random import randint


def describe_game():
    print('What is the result of the expression?')


def calculate(number1, number2, picked_operator):

    if picked_operator == '+':
        answer = operator.add(number1, number2)

    if picked_operator == '-':
        answer = operator.sub(number1, number2)

    if picked_operator == '*':
        answer = operator.mul(number1, number2)

    return answer


def get_question_and_answer():
    number1 = randint(1, 20)
    number2 = randint(1, 20)
    operators = ['+', '-', '*']
    picked_operator = random.choice(operators)
    question = '{} {} {}'.format(number1, picked_operator, number2)
    correct_answer = str(calculate(number1, number2, picked_operator))

    return question, correct_answer

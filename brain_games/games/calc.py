import random
from random import randint
import brain_games.game_logic


def calculator():
    number1 = randint(-100, 100)
    number2 = randint(-100, 100)
    operators = ['+', '-', '*']
    picked_operator = random.choice(operators)
    question = '{} {} {}'.format(number1, picked_operator, number2)

    if picked_operator == '+':
        correct_answer = str(number1 + number2)

    if picked_operator == '-':
        correct_answer = str(number1 - number2)

    if picked_operator == '*':
        correct_answer = str(number1 * number2)

    brain_games.game_logic.user_answers(question, correct_answer)

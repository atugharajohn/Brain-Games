from random import randint
import brain_games.game_logic


def find_gcd():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    question = '{} {}'.format(number1, number2)

    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    correct_answer = str(number1 + number2)

    brain_games.game_logic.user_answers(question, correct_answer)

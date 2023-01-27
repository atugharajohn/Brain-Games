from random import randint
import brain_games.game_logic


def is_even():
    question = randint(-100, 100)

    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    brain_games.game_logic.user_answers(question, correct_answer)

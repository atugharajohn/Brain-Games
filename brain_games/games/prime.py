from random import randint
import brain_games.game_logic


def is_prime():
    question = randint(1, 1000)

    if question == 1:
        correct_answer = 'no'

    for i in range(2, question):
        if question % i == 0:
            correct_answer = 'no'
            break
        correct_answer = 'yes'

    brain_games.game_logic.user_answers(question, correct_answer)

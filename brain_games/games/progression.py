import random
from random import randint
import brain_games.game_logic


def a_progression():
    d = randint(-10, 10)
    a1 = randint(-100, 100)
    n = randint(5, 10)
    list_progr = [a1]
    a_current = a1
    a_next = a_current + d

    for i in range(n):
        a_current = a_next
        a_next = a_current + d
        list_progr.append(a_current)

    random_element = random.choice(list_progr)

    for index, elem in enumerate(list_progr):
        if elem == random_element:
            list_progr[index] = '..'

    question = " ".join(map(str, list_progr))
    correct_answer = str(random_element)

    brain_games.game_logic.user_answers(question, correct_answer)

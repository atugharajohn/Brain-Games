import random
from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def build_progression():
    difference = randint(1, 10)
    first_elem = randint(1, 50)
    number_of_elem = randint(6, 11)
    n_elem = first_elem + (number_of_elem - 1) * difference
    list_progr = []

    for elem in range(first_elem, n_elem, difference):
        list_progr.append(elem)
    return list_progr


def get_question_and_answer():
    result_progression = build_progression()
    random_index = random.randrange(len(result_progression))
    correct_answer = str(result_progression[random_index])
    result_progression[random_index] = '..'
    question = " ".join(map(str, result_progression))

    return question, correct_answer

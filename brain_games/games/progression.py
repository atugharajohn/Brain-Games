import random
from random import randint


def describe_game():
    print("What number is missing in the progression?")


def build_progression():
    d = randint(1, 10)
    a1 = randint(1, 50)
    n = randint(6, 11)
    a_n = a1 + (n - 1) * d
    list_progr = []

    for elem in range(a1, a_n, d):
        list_progr.append(elem)
    return list_progr


def get_question_and_answer():
    result_progression = build_progression()
    random_index = random.randrange(len(result_progression))
    correct_answer = str(result_progression[random_index])

    for index in range(len(result_progression)):
        if index == random_index:
            result_progression[index] = '..'

    question = " ".join(map(str, result_progression))

    return question, correct_answer

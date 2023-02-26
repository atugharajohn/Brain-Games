from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def get_question_and_answer():
    question = randint(1, 100)
    answers = ['no', 'yes']
    correct_answer = answers[is_even(question)]

    return question, correct_answer

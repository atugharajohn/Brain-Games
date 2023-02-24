from random import randint


def describe_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number):
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def get_question_and_answer():
    question = randint(1, 100)
    correct_answer = is_even(question)

    return question, correct_answer

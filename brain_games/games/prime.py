from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def get_question_and_answer():
    question = randint(1, 1000)
    answers = ['no', 'yes']
    correct_answer = answers[is_prime(question)]

    return question, correct_answer

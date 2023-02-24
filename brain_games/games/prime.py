from random import randint


def describe_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(number):
    if number == 1:
        return 'no'
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def get_question_and_answer():
    question = randint(1, 1000)
    correct_answer = is_prime(question)

    return question, correct_answer
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(number1, number2):

    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1

    return number1 + number2


def get_question_and_answer():
    number1 = randint(0, 50)
    number2 = randint(0, 50)
    question = '{} {}'.format(number1, number2)
    correct_answer = str(find_gcd(number1, number2))

    return question, correct_answer

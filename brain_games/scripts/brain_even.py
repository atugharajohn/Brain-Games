#!/usr/bin/env python3

import prompt
from random import randint


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def user_answers():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0

    while i < 3:
        random_num = randint(1, 100)
        print(f'Question: {random_num}')
        answer = prompt.string('Your answer: ')

        if (answer == is_even(random_num)):
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{is_even(random_num)}'.\nLet's try again, {name}!")
            break


def main():
    print("Welcome to the Brain Games!")
    user_answers()


if __name__ == '__main__':
    main()

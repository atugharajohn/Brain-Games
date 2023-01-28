import prompt

current_score = 0
last_score = 0
name = ''


def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def user_answers(question, correct_answer):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    global current_score, last_score

    if answer == correct_answer:
        print('Correct!')
        last_score = current_score
        current_score += 1

        if current_score == 3:
            print(f'Congratulations, {name}!')
    else:
        last_score = current_score
        print(f"'{answer}' is wrong answer ;(. Correct answer was "
              f"'{correct_answer}'.\nLet's try again, {name}!")

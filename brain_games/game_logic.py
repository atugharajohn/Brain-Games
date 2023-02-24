import prompt
from brain_games.cli import welcome_user


def play(game):
    score = 0
    count_of_game = 3
    name = welcome_user()
    game.describe_game()

    while True:
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.\nLet's try again, {name}!")
            break

        if score == count_of_game:
                print(f'Congratulations, {name}!')
                break

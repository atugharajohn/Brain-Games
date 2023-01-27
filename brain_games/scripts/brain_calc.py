#!/usr/bin/env python3

import brain_games.game_logic
import brain_games.games.even
import brain_games.games.calc


def main():
    print("Welcome to the Brain Games!")
    brain_games.game_logic.welcome_user()
    print('What is the result of the expression?')
    brain_games.games.calc.calculator()
    while brain_games.game_logic.current_score < 3 \
        and brain_games.game_logic.current_score \
            != brain_games.game_logic.last_score:
        brain_games.games.calc.calculator()


if __name__ == '__main__':
    main()

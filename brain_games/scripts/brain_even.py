#!/usr/bin/env python3

import brain_games.game_logic
import brain_games.games.even


def main():
    brain_games.game_logic.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    brain_games.games.even.is_even()
    while brain_games.game_logic.current_score < 3 \
        and brain_games.game_logic.current_score \
            != brain_games.game_logic.last_score:
        brain_games.games.even.is_even()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import brain_games.game_logic
import brain_games.games.gcd


def main():
    brain_games.game_logic.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    brain_games.games.gcd.find_gcd()
    while brain_games.game_logic.current_score < 3 \
        and brain_games.game_logic.current_score \
            != brain_games.game_logic.last_score:
        brain_games.games.gcd.find_gcd()


if __name__ == '__main__':
    main()

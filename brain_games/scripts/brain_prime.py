#!/usr/bin/env python3

import brain_games.game_logic
import brain_games.games.prime


def main():
    brain_games.game_logic.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    brain_games.games.prime.is_prime()
    while brain_games.game_logic.current_score < 3 \
        and brain_games.game_logic.current_score \
            != brain_games.game_logic.last_score:
        brain_games.games.prime.is_prime()


if __name__ == '__main__':
    main()

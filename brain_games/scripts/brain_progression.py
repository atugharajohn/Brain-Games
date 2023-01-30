#!/usr/bin/env python3

import brain_games.game_logic
import brain_games.games.progression


def main():
    brain_games.game_logic.welcome_user()
    print('What number is missing in the progression?')
    brain_games.games.progression.a_progression()
    while brain_games.game_logic.current_score < 3 \
        and brain_games.game_logic.current_score \
            != brain_games.game_logic.last_score:
        brain_games.games.progression.a_progression()


if __name__ == '__main__':
    main()

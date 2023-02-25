#!/usr/bin/env python3
"""This is the script of brain-progression game."""
from brain_games.game_logic import play
from brain_games.games import progression


def main():
    """Launch brain-progression game."""
    play(progression)


if __name__ == '__main__':
    main()

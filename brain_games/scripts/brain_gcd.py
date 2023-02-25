#!/usr/bin/env python3
"""This is the script of brain greatest common divisor game."""
from brain_games.game_logic import play
from brain_games.games import gcd


def main():
    """Launch brain-gcd game."""
    play(gcd)


if __name__ == '__main__':
    main()

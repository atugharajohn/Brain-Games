#!/usr/bin/env python3
"""This is the script of brain-prime game."""
from brain_games.game_logic import play
from brain_games.games import prime


def main():
    """Launch brain-prime game."""
    play(prime)


if __name__ == '__main__':
    main()

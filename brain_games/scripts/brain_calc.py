#!/usr/bin/env python3
"""This is the script of brain-calc game."""
from brain_games.game_logic import play
from brain_games.games import calc


def main():
    """Launch brain-calc game."""
    play(calc)


if __name__ == '__main__':
    main()

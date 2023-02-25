#!/usr/bin/env python3
"""This is the script of brain-even game."""
from brain_games.game_logic import play
from brain_games.games import even


def main():
    """Launch brain-even game."""
    play(even)


if __name__ == '__main__':
    main()

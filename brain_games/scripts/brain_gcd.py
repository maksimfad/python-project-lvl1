#!/usr/bin/env python
"""This module starts gcd game."""

from brain_games.games.gcd_game import (  # isort:skip
    description_of_game,
    game_question_and_answer,
)
from brain_games.games.games_logic import game_logic


def main():
    """Use this function to call game_logic function."""
    game_logic(description_of_game, game_question_and_answer)


if __name__ == '__main__':
    main()

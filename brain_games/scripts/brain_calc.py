#!/usr/bin/env python
"""This module starts 'is nubmer even' game."""

from brain_games.games.calc_game import description_of_game, game_question_and_answer
from brain_games.games.games_logic import game_logic


def main():
    """Use this function to call game_logic function"""
    game_logic(description_of_game, game_question_and_answer)



if __name__ == '__main__':
    main()

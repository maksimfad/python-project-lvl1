"""This is module where even game logic defined."""

from random import randint  # isort:skip


description_of_game = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_question_and_answer():
    """Use this cunction to generate question and right answer\
         and return them."""
    question_number = randint(1, 100)
    if question_number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return (question_number, answer)

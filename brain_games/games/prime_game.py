"""This is module where pprime game logic defined."""

from random import randint  # isort:skip


description_of_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_question_and_answer():
    """Use this function to generate question and right answer and return them."""
    question_number = randint(2, 100)
    question = str(question_number)
    divisor = 2
    right_answer = 'yes'
    while divisor <= question_number / 2:
        if question_number % divisor == 0:
            right_answer = 'no'
        divisor += 1
    return question, right_answer

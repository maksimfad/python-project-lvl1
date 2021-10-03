"""This is module where gcd game logic defined."""

from random import randint  # isort:skip


description_of_game = 'Find the greatest common divisor of given numbers.'


def game_question_and_answer():
    """Use this function to generate question and right\
         answer and returns them."""
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    question = '{0} {1}'.format(first_number, second_number)
    if first_number < second_number:
        min_number = first_number
    else:
        min_number = second_number
    test_divisor = 1
    max_divisor = 1
    while test_divisor <= min_number:
        first_condition = first_number % test_divisor == 0
        second_condition = second_number % test_divisor == 0
        if first_condition & second_condition:
            max_divisor = test_divisor
        test_divisor += 1
    right_answer = str(max_divisor)
    return question, right_answer

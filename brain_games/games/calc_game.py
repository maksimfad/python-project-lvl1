"""This is module where calc game logic defined."""

from random import randint


description_of_game = 'What is the result of the expression?' 

def game_question_and_answer():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    random_for_operation_choose = randint(1, 3)
    if random_for_operation_choose == 1:
        question = '{0} + {1}'.format(first_number, second_number)
        right_answer = str(first_number + second_number)
    elif random_for_operation_choose == 2:
        question = '{0} - {1}'.format(first_number, second_number)
        right_answer = str(first_number - second_number)
    else:
        question = '{0} * {1}'.format(first_number, second_number)
        right_answer = str(first_number * second_number)
    return question, right_answer



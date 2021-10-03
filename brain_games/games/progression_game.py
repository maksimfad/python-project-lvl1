"""This is module where progression game logic defined."""

from random import randint  # isort:skip


description_of_game = 'What number is missing in the progression?'


def game_question_and_answer():
    """Use this function to generate question and right answer and returns them."""
    lenght_of_progression = randint(5, 10)
    # print(lenght_of_progression)
    max_start_of_progression = 20
    start_of_progression = randint(1, max_start_of_progression)
    incrementor = randint(1, 10)
    progression = [start_of_progression]
    counter = 0
    while counter < lenght_of_progression - 1:
        progression.append(progression[counter] + incrementor)
        counter += 1
    position_of_missing_number = randint(0, lenght_of_progression - 1)
    right_answer = str(progression[position_of_missing_number])
    progression[position_of_missing_number] = '..'
    question = ''
    for number in progression:
        question = question + '{0} '.format(number)
    return question, right_answer

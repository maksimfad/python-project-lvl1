"""This module describes logic of games."""

import prompt


def welcome_user_return_name():
    """Use this function to get user name and print greeting with it."""
    name_of_user = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name_of_user))
    return name_of_user


def game_logic(description_of_game, game_question_and_answer):
    """Use this function to control games."""
    score = 0
    name_of_user = welcome_user_return_name()
    print(description_of_game)
    while score < 3:
        question, right_answer = game_question_and_answer()
        print('Question: {0}'.format(question))
        answer_of_user = prompt.string('Your answer: ')
        if answer_of_user == right_answer:
            print('Correct!')
            score += 1
        else:
            print("'{0}' is wrong answer\
                 ;(. Correct answer was '{1}'.".format(answer_of_user, right_answer))
            print("Let's try again, {0}!".format(name_of_user))
            break
    if score == 3:
        print('Congratulations, {0}!'.format(name_of_user))

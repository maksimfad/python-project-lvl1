"""This is module where even game logic defined."""

import prompt
from random import randint


def welcome_user_return_name():
    """Use this function to get user name and print greeting with it."""
    name_of_user = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name_of_user))
    return(name_of_user)

def even_game():
    """Use this function to run even game."""
    score = 0
    name_of_user = welcome_user_return_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while score < 3:
        question_number = randint(1, 100)
        print('Question: {0}'.format(question_number))
        answer_of_user = prompt.string('Your answer: ')
        if question_number % 2 == 0:
            if answer_of_user == 'yes':
                print('Correct!')
                score+=1
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'")
                print("Let's try again, {0}!".format(name_of_user))
                break
        else:
            if answer_of_user == 'no':
                print('Correct!')
                score+=1
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'")
                print("Let's try again, {0}!".format(name_of_user))
                break
    if score == 3:
        print("Congratulations, {0}!".format(name_of_user))

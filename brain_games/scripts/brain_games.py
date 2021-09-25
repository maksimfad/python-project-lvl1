#!/usr/bin/env python
"""This module is script that do all the stuff."""

from brain_games.cli import welcome_user


def main():
    """Use this function to welcome and to greet user."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()

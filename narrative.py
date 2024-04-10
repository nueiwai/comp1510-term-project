import time
import pyfiglet

"""
This module contains:

the bonus level of the game (which appears in between level 2 and level 3 if certain criteria of the character is met).
Other narrative, ascii art related components of the game will also go here.
"""


def check_met_criteria(character):
    """
    Check if the player meets the criteria to enter bonus level (co-op).
    """
    return character['GPA'] >= 3.8


def print_gradually(text):
    """
    Print the narrative text slowly, with progressive reveal.
    """
    for character in text:
        print(character, end="")
        time.sleep(0.03)
    print()


def co_op_term():
    """
    Display the narrative 'co-op.'
    """
    print_gradually(f"Welcome to your co-op term! We are just thrilled~ you made it here.")
    print_gradually(f"Prepare yourself for exciting projects valuable industry experience, ahem.")
    for _ in range(2):
        print('Tick')
        time.sleep(1)
        print('Tock')
        time.sleep(1)
    print_gradually(f"Looks like it's time to get back to work . . .")


def bonus_part(character):
    """
    Drive the bonus part of the game.
    """
    if check_met_criteria(character):
        co_op_term()
    else:
        print(f"Sorry, you did not meet the criteria to go into co-op. Chin-up! Grades aren't everything.")


def welcome_message():
    print("Welcome Player. You will be role playing as a computing student in this game. There will be a lot of "
          "challenges for you. Make sure to manage your life well. Balance of your life is the key to success in this "
          "game.")
    f = pyfiglet.figlet_format("Computing Ranger", font="slant")
    print(f)


if __name__ == "__main__":
    co_op_term()

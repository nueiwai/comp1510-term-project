import time
import map_components
import pyfiglet

"""
This module contains:

the bonus level of the game (which appears in between level 2 and level 3 if certain criteria of the character is met).
Other narrative, ascii art related components of the game will also go here.
"""


def check_met_criteria(player):
    """
    Check if the player meets the criteria to enter bonus level (co-op).
    """
    return player['GPA'] >= 3.5


def print_gradually(text):
    """
    Print the narrative text slowly, with progressive reveal.
    """
    for character in text:
        print(character, end="")
        time.sleep(0.03)
    print()


def waiting(count_ticktock):
    """
    Display the narrative 'waiting.'
    """
    print_gradually(f"Waiting . . .")
    for _ in range(count_ticktock):
        print('Tick')
        time.sleep(1)
        print('Tock')
        time.sleep(1)


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


def bonus_part(player):
    """
    Drive the bonus part of the game.
    """
    if check_met_criteria(player):
        co_op_term()
    else:
        print(f"Sorry, you did not meet the criteria to go into co-op. Chin-up! Grades aren't everything.")


def welcome_message():
    print_gradually("Welcome Player. You will be role playing as a computing student in this game.\n"
                    "There will be a lot of challenges for you. Make sure to manage your life well.\n Balance of your "
                    "life is the key to success in this game.\nYou need to graduate from the program to win the game. "
                    "\nYou will be taking quizzes, attending events")
    f = pyfiglet.figlet_format("Computing Ranger", font="slant")
    print(f)


def drop_out():
    # Print the dropout message with some encouragement and advice
    print_gradually(f"Unfortunately, you failed the exam, you must leave the program due to failing the exam.")
    print_gradually("This is not the end of your journey! Here are a few things you might consider:")
    print_gradually("- Take some time off to gather your thoughts and decide your next steps.")
    print_gradually("- Explore other educational opportunities or different fields that might suit your strengths.")
    print_gradually("- Consider gaining some practical experience through internships or part-time jobs.")
    print_gradually("- When ready, you can reapply or pursue alternative certification programs.")
    return


def print_map_repeatedly(player, game_map):
    map_components.print_game_map(player)
    map_components.describe_current_location(game_map, player)
    return player


if __name__ == "__main__":
    co_op_term()

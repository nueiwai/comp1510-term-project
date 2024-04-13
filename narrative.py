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
    :param player: a dictionary representing the player's state
    :precondition: player must be a dictionary with a key "GPA"
    :postcondition: return True if the player meets the criteria, False otherwise
    :return: a boolean representing if the player meets the criteria

    >>> check_met_criteria({'GPA': 3.5})
    True

    >>> check_met_criteria({'GPA': 3.4})
    False
    """
    return player['GPA'] >= 3.5


def print_gradually(text):
    """
    Print the narrative text slowly, with progressive reveal.

    :param text: a string
    :precondition: text must be a string
    :postcondition: print out the text with a delay of 0.03 seconds between each character
    """
    for character in text:
        print(character, end="")
        time.sleep(0.02)
    print()


def waiting(count_ticktock):
    """
    Display the narrative 'waiting.'

    :param count_ticktock: a positive int
    :precondition: count_ticktock must be an int
    :postcondition: print out 'Tick' and 'Tock' with a delay of 1 second between each
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

    :postcondition: print out the narrative for the co-op term
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

    :param player: a dictionary representing the player's state
    :precondition: player must be a dictionary with a key "GPA"
    :postcondition: print out the narrative for the bonus part of the game

    """
    if check_met_criteria(player):
        co_op_term()
    else:
        print(f"Sorry, you did not meet the criteria to go into co-op. Chin-up! Grades aren't everything.")


def welcome_message():
    """
    Display the welcome message.

    :postcondition: print out the welcome message
    """
    print_gradually("Welcome Player. You will be role playing as a computing student in this game.\n"
                    "There will be a lot of challenges for you. Make sure to manage your life well.\n Balance of your "
                    "life is the key to success in this game.\nYou need to graduate from the program to win the game. "
                    "\nYou will be taking quizzes, attending events")
    f = pyfiglet.figlet_format("CST SIM", font="slant")
    print(f)


def drop_out():
    """
    Display the dropout message.

    :postcondition: print out the dropout message

    """
    # Print the dropout message with some encouragement and advice
    print_gradually(f"Unfortunately, you failed the exam, you must leave the program due to failing the exam.")
    print_gradually("This is not the end of your journey! Here are a few things you might consider:")
    print_gradually("- Take some time off to gather your thoughts and decide your next steps.")
    print_gradually("- Explore other educational opportunities or different fields that might suit your strengths.")
    print_gradually("- Consider gaining some practical experience through internships or part-time jobs.")
    print_gradually("- When ready, you can reapply or pursue alternative certification programs.")


def print_map_repeatedly(player, game_map):
    """
    Print the game map and the player's current location repeatedly.

    :param player: a dictionary representing the player's state
    :param game_map: a dictionary representing the game map
    :precondition: player must be a dictionary with a key "location"
    :precondition: game_map must be a dictionary with keys representing the cell numbers
    :postcondition: print out the game map and the player's current location

    """
    map_components.print_game_map(player)
    map_components.describe_current_location(game_map, player)
    return player


def bid_farewell_message():
    """
    Display the farewell message.

    :postcondition: print out the farewell message
    """
    print(f"Thank you for playing our game, I hope it didn't get too real for you...")
    print(f"Think of it as a prelude of what is to come~")
    print(f"You are going to do well as CST Students, and in many other things.")
    print_gradually(f"From the game-makers themselves you are given a straw.")
    print_gradually(f"I think they are telling you when life gets hard, suck it up.")
    print_gradually(f"Keep going, you are doing great. You might not think so but. Truly exceptional. Bye for now.")


def welcome_to_term_two():
    """
    Display the welcome message for term two.

    :postcondition: print out the welcome message for term two
    :return:
    """
    print_gradually(f"You are in term two now.")
    print_gradually(f"Feeling okay? Don't hate us, hate the game~ Wait, don't hate the game.")
    print_gradually(f"Here we go~")


def welcome_to_term_three():
    """
    Display the welcome message for term three.

    :postcondition: print out the welcome message for term three
    :return:
    """
    print_gradually(f"Whoa. We always thought this would be the hardest level to reach.")
    print_gradually(f"Perhaps you proved us wrong?")
    print_gradually(f"If you didn't get into co-op don't feel bad.")
    print_gradually(f"Nothing to lose sleep over.")
    print_gradually(f"Ready?")


def welcome_to_term_four():
    """
    Display the welcome message for term four.

    :postcondition: print out the welcome message for term four
    """
    print_gradually(f"Last term.")
    print_gradually(f"Can't believe you're still here.")
    print_gradually(f"We estimated about a 95% drop-out rate.")
    print_gradually(f"Seems like you were born to prove us wrong.")
    print_gradually(f"Tsk. Well, good luck~")


if __name__ == "__main__":
    """
    Run the functions in this module to demonstrate their behavior.
    """
    welcome_message()
    drop_out()
    waiting(2)
    co_op_term()

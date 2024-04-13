import random
"""
This module contains:

Functions related to the character's attributes:
    - generating the character's new attributes at the start of the game & each term (level)
    - character's encounter with instructors (dependent on character's position in the game)
    - character's enrollment (did not drop out)
    - character's ability to proceed to the next level/term (graduation from term)
"""


def make_character():
    """
    Create a dictionary that contains character's attributes at the beginning of the game.

    :postcondition: create a dictionary with keys "time", "GPA", "social", and "location"
    :return: character attributes "time," "GPA," "social" and "location" as a dictionary

    >>> test_player = make_character()
    >>> test_player
    {'time': 100, 'GPA': 3.5, 'social': 50, 'location': 1}
    """
    return {'time': 100, 'GPA': 3.5, 'social': 50, 'location': 1}


def make_character_each_term_start(player):
    """
    Create a dictionary that contains character's attributes at the start of each term that corresponds to that level.

    :postcondition: create a dictionary with keys "time", "GPA", "social", and "location"
    :return: character attributes "time," "GPA," "social" and "location" as a dictionary

    >>> test_player = {'time': 50, 'GPA': 3.8, 'social': 50, 'location': 26}
    >>> result = make_character_each_term_start(test_player)
    >>> result
    {'time': 120, 'GPA': 3.5, 'social': 60, 'location': 26}
    """
    if player['location'] == 26:
        player = {'time': 120, 'GPA': 3.5, 'social': 60, 'location': 26}
    elif player['location'] == 51:
        player = {'time': 150, 'GPA': 3.5, 'social': 70, 'location': 51}
    elif player['location'] == 76:
        player = {'time': 180, 'GPA': 3.5, 'social': 80, 'location': 76}
    return player


# def check_for_instructors():
#     """
#     Generate an instructor encounter 25% of the time.
#
#     :postcondition: after each move, a random number is generated and 25% of the time, player encounters an instructor
#     :return: if an instructor is encountered or not as a bool
#     """
#     chance_of_encounter = random.random()
#     return chance_of_encounter <= 0.25


def check_if_graduated_this_term(player):
    """
    Check if the goal of meeting term graduation criteria is attained.

    :param player: a dictionary that stores the character's attributes
    :precondition: player must be a dictionary with keys "time", "GPA", "social", and "location"
    :postcondition: check if player's character attributes has reached the criteria for term graduation:
                 - 'GPA': greater than or equal to 2.0
    :return: if player's character attributes has met graduation criteria or not as a bool

    >>> test_player = {'time': 50, 'GPA': 3.5, 'social': 50, 'location': 75}
    >>> check_if_graduated_this_term(test_player)
    True

    >>> test_player = {'time': 50, 'GPA': 1.0, 'social': 50, 'location': 25}
    >>> check_if_graduated_this_term(test_player)
    False
    """
    if player['GPA'] >= 2.0:
        return True
    else:
        return False


def is_enrolled(player):
    """
    Evaluate if the player is still enrolled in the program as a student.

    :param player: a dictionary that stores the character's attributes
    :precondition: player must be a dictionary with keys "time", "GPA", "social", and "location"
    :postcondition: evaluate if the player is still enrolled in the program as a student
    :return: if the player's GPA has dipped below 2.0 or not as a bool

    >>> test_player = {'time': 50, 'GPA': 1.0, 'social': 50, 'location': 25}
    >>> is_enrolled(test_player)
    False

    >>> test_player = {'time': 50, 'GPA': 3.5, 'social': 50, 'location': 75}
    >>> is_enrolled(test_player)
    True
    """
    return player['GPA'] >= 2.0


def update_player_location(player, accomplishment_state=False):
    """
    Update the player's location based on whether the player sleeps that day.

    :param player: a dictionary that stores the character's attributes
    :param accomplishment_state: a boolean that determines if the player has accomplished something that day
    :precondition: player must be a dictionary with keys "time", "GPA", "social", and "location"
    :postcondition: correctly adjust the player's location in the event the player chooses to sleep
    :return: a list containing the updated slept_yesterday boolean and the player dictionary
    """
    if not accomplishment_state:
        print(f"You did not accomplish anything today. Need to work on something before you sleep.\nDon't waste time!!")
        return player

    while accomplishment_state:
        try:
            sleep_through = input(f"Do you want to sleep now? (Y/N): ").strip().upper()
            if not sleep_through.isalpha() or sleep_through == "":
                raise ValueError(f"That was an invalid choice. Input must be 'Y' or 'N'.")
            break
        except ValueError as error:
            print(error)

    if sleep_through == "Y":
        if player["location"] in [24, 49, 74, 99]:
            player["location"] += 2  # skip two day sleeping
            print(f"Oops. You slept through the entire day. Your woke up with full energy.")
            return player
        else:
            player["location"] += 1  # skip just one day sleeping
            print(f"Oops. You slept through the entire day. Your woke up with full energy.")
            return player
    else:
        print(f"You chose not to sleep...you probably should have slept though.")
        return player


def test_run_sleep():
    player = {"time": 85, "GPA": 3.2, "social": 60, "location": 26}
    print(update_player_location(player))


if __name__ == "__main__":
    test_run_sleep()

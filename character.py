"""
This module contains:

Functions related to the character's attributes:
    - generating the character's new attributes at the start of the game & each term (level)
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

    :param player: a dictionary that stores the character's attributes
    :precondition: player must be a dictionary with keys "time", "GPA", "social", and "location"
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


def update_player_location(player, accomplishment_state):
    """
    Update the player's location based on whether the player sleeps that day.

    :param player: a dictionary that stores the character's attributes
    :param accomplishment_state: a boolean that determines if the player has accomplished something that day
    :precondition: player must be a dictionary with keys "time", "GPA", "social", and "location"
    :postcondition: correctly adjust the player's location in the event the player chooses to sleep
    :return: a list containing the updated slept_yesterday boolean and the player dictionary
    :raises ValueError: if the input for sleeping decision is not 'Y' or 'N' or if the input is empty or not alphabetic
    """
    if not accomplishment_state:
        print(f"You did not accomplish anything today. Need to work on something before you sleep.\nDon't waste time!!")
        return player

    sleep_through = None
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
            player["location"] += 1  # skip just one day sleeping
            print(f"Oops. You slept through the entire day. Your woke up with full energy.")
            return player

        else:
            player["location"] += 2  # skip just one day sleeping
            print(f"Oops. You slept through the whole two days. Your woke up with full energy.")
            return player
    else:
        print(f"You chose not to sleep...you probably should have slept though.")
        return player


def test_run_sleep():
    """
    Test the function update_player_location().
    """
    player = {"time": 85, "GPA": 3.2, "social": 60, "location": 26}
    print(update_player_location(player, True))


if __name__ == "__main__":
    test_run_sleep()

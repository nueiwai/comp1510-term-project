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


def check_for_instructors():
    """
    Generate an instructor encounter 25% of the time.

    :postcondition: after each move, a random number is generated and 25% of the time, player encounters an instructor
    :return: if an instructor is encountered or not as a bool
    """
    chance_of_encounter = random.random()
    return chance_of_encounter <= 0.25


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


def quiz_question():
    """
    Generate a quiz question that draws from a question bank to ask the player.
    """
    questions = ['question 1', 'question 2', 'question 3', 'question 4', 'question 5']
    random.shuffle(questions)
    return questions[0]


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


def update_player_location(player, slept_yesterday):
    """
    Update the player's location based on whether the player sleeps that day.

    :param player: a dictionary that stores the character's attributes
    :param slept_yesterday: a boolean that indicates if the player slept yesterday
    :precondition: player must be a dictionary with keys "time", "GPA", "social", and "location"
    :precondition: slept_yesterday must be a boolean
    :postcondition: correctly adjust the player's location in the event the player chooses to sleep
    :postcondition: correctly print the narrative according to whether the player slept yesterday
    """
    if slept_yesterday is False:
        sleep_through = input(f"Do you want to sleep today? (Y/N): ").upper()
        if sleep_through == "Y":
            player["location"] += 1  # skip one day sleeping
            print(f"Oops. You slept through the entire day. Your location on the map is updated.")
            slept_yesterday = True
        elif sleep_through == "N":
            print(f"You chose not to sleep...you probably should have slept though. Location on the map is unchanged.")
        else:
            print(f"That was an invalid input. Please enter either 'Y' or 'N'.")
    else:
        sleep_through = input(f"Do you want to sleep today? (Y/N): ").upper()
        if sleep_through == "Y":
            print(f"You slept yesterday so~ sorry, you have work to do today. Your location on the map is unchanged.")
        elif sleep_through == "N":
            print(f"I guess that makes sense. You DID sleep yesterday. Just take a nap later.")
        else:
            print(f"That was an invalid input. Please enter either 'Y' or 'N'.")
    return slept_yesterday


def test_run_sleep():
    player = {"time": 85, "GPA": 3.2, "social": 60, "location": 26}
    slept_yesterday = False
    update_player_location(player, slept_yesterday)


if __name__ == "__main__":
    test_run_sleep()

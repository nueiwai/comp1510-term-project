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

    >>> test_character = make_character()
    >>> test_character
    {'time': 100, 'GPA': 3.5, 'social': 50, 'location': 1}
    """
    return {'time': 100, 'GPA': 3.5, 'social': 50, 'location': 1}


def make_character_each_term_start(character):
    """
    Create a dictionary that contains character's attributes at the start of each term that corresponds to that level.

    :postcondition: create a dictionary with keys "time", "GPA", "social", and "location"
    :return: character attributes "time," "GPA," "social" and "location" as a dictionary

    >>> test_character = {'time': 50, 'GPA': 3.8, 'social': 50, 'location': 26}
    >>> result = make_character_each_term_start(test_character)
    >>> result
    {'time': 120, 'GPA': 3.5, 'social': 60, 'location': 26}
    """
    if character['location'] == 26:
        character = {'time': 120, 'GPA': 3.5, 'social': 60, 'location': 26}
    elif character['location'] == 51:
        character = {'time': 150, 'GPA': 3.5, 'social': 70, 'location': 51}
    elif character['location'] == 76:
        character = {'time': 180, 'GPA': 3.5, 'social': 80, 'location': 76}
    return character


def check_for_instructors():
    """
    Generate an instructor encounter 25% of the time.

    :postcondition: after each move, a random number is generated and 25% of the time, player encounters an instructor
    :return: if an instructor is encountered or not as a bool
    """
    chance_of_encounter = random.random()
    return chance_of_encounter <= 0.25


def check_if_graduated_this_term(character):
    """
    Check if the goal of meeting term graduation criteria is attained.

    :param character: a dictionary that stores the character's attributes
    :precondition: character must be a dictionary with keys "time", "GPA", "social", and "location"
    :postcondition: check if player's character attributes has reached the criteria for term graduation:
                 - 'GPA': greater than or equal to 2.0
    :return: if player's character attributes has met graduation criteria or not as a bool

    >>> test_character = {'time': 50, 'GPA': 3.5, 'social': 50, 'location': 75}
    >>> check_if_graduated_this_term(test_character)
    True

    >>> test_character = {'time': 50, 'GPA': 1.0, 'social': 50, 'location': 25}
    >>> check_if_graduated_this_term(test_character)
    False
    """
    if character['GPA'] >= 2.0:
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


def is_enrolled(character):
    """
    Evaluate if the player is still enrolled in the program as a student.

    :param character: a dictionary that stores the character's coordinates and GPA
    :precondition: character must be a dictionary with the format "X-coordinate": 0, "Y-coordinate": 0, "GPA": 2.0
    :postcondition: evaluate if the player's HP is still enrolled in the program as a student
    :return: if the player's GPA has dipped below 2.0 or not as a bool

    >>> test_character = {'time': 50, 'GPA': 1.0, 'social': 50, 'location': 25}
    >>> is_enrolled(test_character)
    False

    >>> test_character = {'time': 50, 'GPA': 3.5, 'social': 50, 'location': 75}
    >>> is_enrolled(test_character)
    True
    """
    return character['GPA'] >= 2.0

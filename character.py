import random
"""
This module contains:

Functions related to the character's attributes:
    - character's position in the game
    - character's GPA
    - character's encounter with instructors (dependent on character's position in the game)
    - character's enrollment (did not drop out)
    - character's ability to proceed to the next level/term (graduation from term)
"""


def make_character():
    """
    Create a dictionary that contains character coordinates and GPA.

    :postcondition: create a dictionary with key:value pairs "X-coordinate": 0, "Y-coordinate": 0, "GPA": 2.0
    :return: "X-coordinate": 0, "Y-coordinate": 0, "GPA": 2.0 as a dictionary

    >>> student = make_character()
    >>> student
    {'X-coordinate': 0, 'Y-coordinate': 0, 'GPA': 2.0}
    """
    return {"X-coordinate": 0, "Y-coordinate": 0, "GPA": 2.0}


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
    :precondition: character must be a dictionary with the format {'X-coordinate': 0, 'Y-coordinate': 0, 'GPA': 2.0}
    :postcondition: check if player's character attributes has reached the criteria for term graduation:
                 - 'GPA': greater than or equal to 2.0
    :return: if player's character attributes has met graduation criteria or not as a bool

    >>> test_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'GPA': 3.0}
    >>> check_if_graduated_this_term(test_character)
    True

    >>> test_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'GPA': 1.0}
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

    >>> test_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'GPA': 1.0}
    >>> is_enrolled(test_character)
    False

    >>> test_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'GPA': 3.0}
    >>> is_enrolled(test_character)
    True
    """
    return character['GPA'] >= 2.0

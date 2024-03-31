import random


def adjust_gpa(gpa, change):
    """
    Adjust player's GPA based on the given change, ensuring it does not exceed 4.0.

    :param gpa: current GPA of the player
    :param change: amount to adjust the GPA by
    :precondition: gpa must be a float within the range 0.0 to 4.0, inclusive
    :precondition: change must be a float
    :postcondition: calculate the GPA correctly to 2 decimal places and does not exceed 4.0 according to the change
    :return: adjusted GPA, rounded to 2 decimal places

    >>> adjust_gpa(3.95, 0.1)
    4.0
    >>> adjust_gpa(2.5, -0.3)
    2.2

    """
    updated_gpa = gpa + change
    if updated_gpa > 4.0:
        return 4.0
    return round(updated_gpa, 2)


def adjust_social(social, change):
    """
    Adjust a player's social score based on the given change, ensuring it stays within 0 to 100.

    :param social: current social score of the player
    :param change: amount to adjust the social score by
    :precondition: social must be an integer within the range 0 to 100
    :precondition: change must be an integer that can be positive or negative
    :postcondition: calculate social score correctly, ensuring it stays within the range 0 to 100, inclusive
    :return: the adjusted social score as an integer

    >>> adjust_social(95, 10)
    100
    >>> adjust_social(5, -10)
    0
    >>> adjust_social(50, -20)
    30
    """
    updated_social = social + change
    if updated_social > 100:
        return 100
    if updated_social < 0:
        return 0
    return updated_social


def assignment_event_adjustment(player):
    """
    Adjust the player's attributes for doing assignment, affecting time and GPA.

    :param player: a dictionary representing the player's state, including "time" and "GPA"
    :precondition: player must be a dictionary with keys "time" and "GPA" and values as int and float, respectively
    :postcondition: reduce player's time by 5 and increase GPA by 0.1
    :return: the updated player dictionary

    >>> assignment_event_adjustment({"time": 100, "GPA": 3.5, "social": 50})
    {'time': 95, 'GPA': 3.6, 'social': 50}

    >>> assignment_event_adjustment({"time": 50, "GPA": 3.9, "social": 50})
    {'time': 45, 'GPA': 4.0, 'social': 50}
    """
    player["time"] -= 5
    player["GPA"] = adjust_gpa(player["GPA"], 0.1)
    return player


def exam_event_adjustment(player, state):  # state True == pass, state False == fail
    """
    Adjust the player's attributes based on the outcome of an exam, affecting time and GPA.

    :param player: a dictionary representing the player's state, including "time" and "GPA"
    :param state: a boolean indicating whether the exam was passed (True) or failed (False)
    :precondition: player must be a dictionary with keys "time" and "GPA" and values as int and float, respectively
    :precondition: state must be a boolean
    :postcondition: reduce player's time by 15 and adjusts GPA by +0.2 if passed, or -0.2 if failed
    :return: the updated player dictionary

    >>> exam_event_adjustment({"time": 200, "GPA": 3.0, "social": 50}, True)
    {'time': 185, 'GPA': 3.2, 'social': 50}

    >>> exam_event_adjustment({"time": 200, "GPA": 3.0, "social": 50}, False)
    {'time': 185, 'GPA': 2.8, 'social': 50}
    """

    player["time"] -= 15
    if state is True:
        player["GPA"] = adjust_gpa(player["GPA"], 0.2)
    else:
        player["GPA"] = adjust_gpa(player["GPA"], - 0.2)
    return player


def study_session_event_adjustment(player):
    """
    Adjust the player's attributes for doing a study session, affecting time, GPA and social.

    :param player: a dictionary representing the player's state, including "time", "GPA", and "social"
    :precondition: player must be a dictionary with keys "time", "GPA" and "social" values as int, float, and int
                   respectively
    :postcondition: reduce player's time by 8, increase GPA by 0.05 and reduce social score by 5
    :return: the updated player dictionary

    >>> study_session_event_adjustment({"time": 120, "GPA": 2.8, "social": 50})
    {'time': 112, 'GPA': 2.85, "social": 45}

    >>> study_session_event_adjustment({"time": 80, "GPA": 3.95, "social": 10})
    {'time': 72, 'GPA': 4.0, "social": 5}
    """
    player["time"] -= 8
    player["GPA"] = adjust_gpa(player["GPA"], 0.05)
    player["social"] = adjust_social(player["social"], -5)
    return player


def social_event_adjustment(player):
    """
    Adjust the player's attributes for going to a social event, affecting time, GPA and social.

    :param player: a dictionary representing the player's state, including "time" and "GPA"
    :precondition: player must be a dictionary with keys "time", "GPA" and "social" values as int, float, and int
                   respectively
    :postcondition: reduce player's time by 10, GPA by 0.08 and increase social score by 10
    :return: the updated player dictionary

    >>> social_event_adjustment({"time": 150, "GPA": 3.6, "social": 30})
    {'time': 140, 'GPA': 3.52, 'social': 40}

    >>> social_event_adjustment({"time": 90, "GPA": 2.0, "social": 60})
    {'time': 80, 'GPA': 1.92, 'social': 70}

    """
    player["time"] -= 10
    player["GPA"] = adjust_gpa(player["GPA"], -0.08)
    player["social"] = adjust_social(player["social"], 10)
    return player


def sick_event_adjustment(player):
    """
    Adjust the player's attributes for being sick, affecting time, GPA and social.

    :param player: a dictionary representing the player's state, including "time" and "GPA"
    :precondition: player must be a dictionary with keys "time", "GPA" and "social" values as int, float, and int
                   respectively
    :postcondition: reduce player's time by a random amount in range [1, 10], GPA by 0.2 and social score by 15
    :return: the updated player dictionary
    """
    player["time"] -= random.randint(1, 10)  # Random time reduction between 1 and 10 (severeness)
    player["GPA"] = adjust_gpa(player["GPA"], -0.2)
    player["social"] = adjust_social(player["social"], -15)
    return player


def volunteering_event_adjustment(player):
    """
    Adjust the player's attributes for volunteering, affecting time, GPA and social.

    :param player: a dictionary representing the player's state, including "time" and "GPA"
    :precondition: player must be a dictionary with keys "time", "GPA" and "social" values as int, float, and int
                   respectively
    :postcondition: reduce player's time by 20, GPA by 0.05 and increase social score by 20
    :return: the updated player dictionary

    >>> volunteering_event_adjustment({"time": 200, "GPA": 2.5, "social": 10})
    {'time': 180, 'GPA': 2.55, 'social': 30}

    >>> volunteering_event_adjustment({"time": 180, "GPA": 3.95, "social": 5})
    {'time': 160, 'GPA': 4.0, 'social': 25}
    """
    player["time"] -= 20
    player["GPA"] = adjust_gpa(player["GPA"], 0.05)
    player["social"] = adjust_social(player["social"], 20)
    return player


def recovery_exam_event_adjustment(player, state):  # state is True when player pass recovery exam and False otherwise
    """
    Adjust the player's attributes based on the outcome of a recovery exam, affecting time and GPA.

    :param player: a dictionary representing the player's state, including "time" and "GPA"
    :param state: a boolean indicating the outcome of the recovery exam: True for pass, False for fail
    :precondition: player must be a dictionary with keys "time" and "GPA" and values as int and float, respectively
    :precondition: state must be a boolean
    :postcondition:  -reduces player's time by 20 and sets the GPA to 2.8 if the exam is passed (state is True)
                     -a message is printed and the player's state is unchanged if the exam is failed (state is False)
    :return: -the updated player dictionary if the exam is passed
             -None and print a message if failed

    >>> recovery_exam_event_adjustment({"time": 100, "GPA": 2.5, "social": 50}, True)
    {'time': 80, 'GPA': 2.8, 'social': 50}
    >>> recovery_exam_event_adjustment({"time": 100, "GPA": 1.8, "social": 50}, False)
    You failed the recovery exam, so you are not graduating. Sorry
    """
    if state is False:
        print("You failed the recovery exam, so you are not graduating. Sorry.")
    else:
        player["time"] -= 20
        player["GPA"] = 2.8  # GPA is set to 2.8 for next year if player passes the recovery exam
        return player


def test_run_adjustments():
    # Initialize a player dictionary
    user = {"time": 100, "GPA": 1.8, "social": 50}

    # Example cases to see functions are working properly or not
    user = assignment_event_adjustment(user)
    print(user)
    user = study_session_event_adjustment(user)
    print(user)
    user = sick_event_adjustment(user)
    print(user)
    user = social_event_adjustment(user)
    print(user)
    user = volunteering_event_adjustment(user)
    print(user)

    user = exam_event_adjustment(user, True)  # Player passes the exam
    print(user)

    if user["GPA"] < 2.0:  # Check the need for recovery exam
        user = recovery_exam_event_adjustment(user, True)  # Player passes recovery exam
    else:
        print("No need for a recovery exam, GPA is above 2.0")
    print(user)


if __name__ == "__main__":
    test_run_adjustments()

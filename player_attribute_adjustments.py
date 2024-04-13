import random
from narrative import print_gradually
"""
This module contains functions that adjust the player's attributes based on the events that occur in the game.

The functions in this module are used to adjust the player's attributes based on the events that occur in the game.
The player's attributes include time, GPA, and social score. The functions in this module adjust these attributes
based on the events that occur in the game, such as completing an assignment, taking an exam, attending a social event,
and volunteering.

functions:
- adjust_gpa(gpa, change)
- adjust_social(social, change, limit)
- adjust_time(time, change)
- assignment_event_adjustment(player)
- exam_event_adjustment(player, state)
- study_session_event_adjustment(player, social_limit)
- social_event_adjustment(player, social_limit)
- sick_event_adjustment(player, social_limit)
- volunteering_event_adjustment(player, social_limit)
- test_run_adjustments()
"""


def adjust_gpa(gpa, change):
    """
    Adjust player's GPA based on the given change, ensuring it is in range [0.0, 4.0].

    :param gpa: current GPA of the player
    :param change: amount to adjust the GPA by
    :precondition: gpa must be a float within the range 0.0 to 4.0, inclusive
    :precondition: change must be a float
    :postcondition: calculate the GPA correctly to 2 decimal places in range [0.0, 4.0] according to the change
    :return: adjusted GPA as float, rounded to 2 decimal places

    >>> adjust_gpa(3.95, 0.1)
    4.0
    >>> adjust_gpa(2.5, -0.3)
    2.2

    """
    updated_gpa = round(float(gpa + change), 3)
    if updated_gpa > 4.0:
        return 4.0
    elif updated_gpa < 0:
        return 0
    else:
        return updated_gpa


def adjust_social(social, change):
    """
    Adjust a player's social score based on the given change, ensuring it stays within 0 to limit.

    :param social: current social score of the player
    :param change: amount to adjust the social score by
    :precondition: social must be an integer within the range 0 to limit
    :precondition: change must be an integer that can be positive or negative
    :postcondition: calculate social score correctly, ensuring it stays within the range 0 to limit, inclusive
    :return: the adjusted social score as an integer

    >>> adjust_social(95, 10)
    105
    >>> adjust_social(5, -10)
    0
    >>> adjust_social(50, -20)
    30
    """
    updated_social = social + change
    if updated_social < 0:
        return 0
    return updated_social


def adjust_time(time, change):
    """
    Adjust a player's time on the given change, ensuring it stays within 0 to limit.
    :param time: current time of the player
    :param change: amount to adjust the time by
    :precondition: time must be an integer within the range 0 to limit
    :precondition: change must be an integer that can be positive or negative
    :postcondition: calculate time correctly, ensuring it stays within the range 0 to limit, inclusive
    :return: the adjusted time as an integer

    >>> adjust_time(5, -3)
    2
    >>> adjust_time(14, 5)
    15
    >>> adjust_time(1, -5)
    0
    """
    updated_time = time + change
    if updated_time < 0:
        return 0
    return updated_time


def assignment_event_adjustment(player):
    """
    Adjust the player's attributes for doing assignment, affecting time and GPA.

    :param player: a dictionary representing the player's state, including "time" and "GPA"
    :precondition: player must be a dictionary with keys "time" and "GPA" and values as int and float, respectively
    :postcondition: reduce player's time by 5 and increase GPA by 0.1
    :return: the updated player dictionary

    >>> assignment_event_adjustment({"time": 100, "GPA": 3.5, "social": 50})
    You have completed an assignment, Great Job!
    You have earned 0.05 GPA points and lost 5 units of time in the process.
    Now you have 3.55 GPA points and 95 units of time left.
    Remember you need to balance your time, GPA and social to graduate.
    <BLANKLINE>
    {'time': 95, 'GPA': 3.55, 'social': 50}

    >>> assignment_event_adjustment({"time": 50, "GPA": 3.9, "social": 50})
    You have completed an assignment, Great Job!
    You have earned 0.05 GPA points and lost 5 units of time in the process.
    Now you have 3.95 GPA points and 45 units of time left.
    Remember you need to balance your time, GPA and social to graduate.
    <BLANKLINE>
    {'time': 45, 'GPA': 3.95, 'social': 50}
    """
    player["time"] = adjust_time(player["time"], -5)
    player["GPA"] = adjust_gpa(player["GPA"], 0.05)
    print(f"You have completed an assignment, Great Job!\n"
          f"You have earned 0.05 GPA points and lost 5 units of time in the process.\n"
          f"Now you have {player['GPA']:.2f} GPA points and {player['time']} units of time left.\n"
          f"Remember you need to balance your time, GPA and social to graduate.\n")
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
    You have passed the exam. Congratulations!
    You have earned 0.2 GPA points.
    Now you have 3.20 GPA and 185 units of time left.
    <BLANKLINE>
    {'time': 185, 'GPA': 3.2, 'social': 50}

    >>> exam_event_adjustment({"time": 200, "GPA": 3.0, "social": 50}, False)
    You have failed the exam. You have lost 0.2 GPA points.
    Remember you need to balance your time and GPA and social to graduate.
    You failed the ultimate test. You are leaving the school.
    <BLANKLINE>
    {'time': 185, 'GPA': 2.8, 'social': 50}
    """

    player["time"] -= 15
    if state is True:
        player["GPA"] = adjust_gpa(player["GPA"], 0.2)
        print(f"You have passed the exam. Congratulations!\n"
              f"You have earned 0.2 GPA points.\n"
              f"Now you have {player['GPA']:.2f} GPA and {player['time']} units of time left.\n")

    else:
        player["GPA"] = adjust_gpa(player["GPA"], - 0.2)
        print(f"You have failed the exam. You have lost 0.2 GPA points.\n"
              f"Remember you need to balance your time and GPA and social to graduate.\n"
              f"You failed the ultimate test. You are leaving the school.\n")
    return player


def study_session_event_adjustment(player):
    """
    Adjust the player's attributes for doing a study session, affecting time, GPA and social.

    :param player: a dictionary representing the player's state, including "time", "GPA", and "social"
    :precondition: player must be a dictionary with keys "time", "GPA" and "social" values as int, float, and int
                   respectively
    :precondition: social_limit must be a positive int
    :postcondition: reduce player's time by 8, increase GPA by 0.05 and reduce social score by 5
    :return: the updated player dictionary

    >>> player1 = {"time": 120, "GPA": 2.8, "social": 50, "location": 4}
    >>> study_session_event_adjustment(player1)
    You have completed a study session. Great Job!
    You have earned 1.00 GPA points and lost 5 units of social score and 10 units of time in the process.
    Remember you need to balance your time and GPA and social to graduate.
    Now you have 3.80 GPA, 45 social score and 110 units of timeleft.
    <BLANKLINE>
    {'time': 110, 'GPA': 3.8, 'social': 45, 'location': 5}

    >>> player2 = {"time": 150, "GPA": 3.6, "social": 30, "location": 4}
    >>> study_session_event_adjustment(player2)
    You have completed a study session. Great Job!
    You have earned 1.00 GPA points and lost 5 units of social score and 10 units of time in the process.
    Remember you need to balance your time and GPA and social to graduate.
    Now you have 4.00 GPA, 25 social score and 140 units of timeleft.
    <BLANKLINE>
    {'time': 140, 'GPA': 4.0, 'social': 25, 'location': 5}

    """
    player["time"] = adjust_time(player["time"], -10)
    player["GPA"] = adjust_gpa(player["GPA"], 1)
    player["social"] = adjust_social(player["social"], -5)
    player["location"] += 1
    print(f"You have completed a study session. Great Job!\n"
          f"You have earned 1.00 GPA points and lost 5 units of social score and 10 units of time in the process.\n"
          f"Remember you need to balance your time and GPA and social to graduate.\n"
          f"Now you have {player['GPA']:.2f} GPA, {player['social']} social score and {player['time']} units of time"
          f"left.\n")
    return player


def social_event_adjustment(player):
    """
    Adjust the player's attributes for going to a social event, affecting time, GPA and social.

    :param player: a dictionary representing the player's state, including "time" and "GPA"
    :precondition: player must be a dictionary with keys "time", "GPA" and "social" values as int, float, and int
                   respectively
    :precondition: social_limit must be a positive int
    :postcondition: reduce player's time by 10, GPA by 0.08 and increase social score by 10
    :return: the updated player dictionary

    >>> social_event_adjustment({"time": 150, "GPA": 3.6, "social": 30, "location": 6})
    You have attended a social event. You made good connections at the event Great Job!
    You have lost 0.08 GPA points and earned 10 units of social score in the process.
    Remember you need to balance your time and GPA and social to graduate.
    Now you have 3.52 GPA, 40 social score and 140 units of timeleft.
    <BLANKLINE>
    {'time': 140, 'GPA': 3.52, 'social': 40, 'location': 7}

    >>> social_event_adjustment({"time": 90, "GPA": 2.0, "social": 60, "location": 6})
    You have attended a social event. You made good connections at the event Great Job!
    You have lost 0.08 GPA points and earned 10 units of social score in the process.
    Remember you need to balance your time and GPA and social to graduate.
    Now you have 1.92 GPA, 70 social score and 80 units of timeleft.
    <BLANKLINE>
    {'time': 80, 'GPA': 1.92, 'social': 70, 'location': 7}

    """
    player["time"] = adjust_time(player["time"], -10)
    player["GPA"] = adjust_gpa(player["GPA"], -0.08)
    player["social"] = adjust_social(player["social"], 10)
    player["location"] += 1
    print(f"You have attended a social event. You made good connections at the event Great Job!\n"
          f"You have lost 0.08 GPA points and earned 10 units of social score in the process.\n"
          f"Remember you need to balance your time and GPA and social to graduate.\n"
          f"Now you have {player['GPA']:.2f} GPA, {player['social']} social score and {player['time']} units of time"
          f"left.\n")
    return player


def sick_event_adjustment(player):
    """
    Adjust the player's attributes for being sick, affecting time, GPA and social.

    :param player: a dictionary representing the player's state, including "time" and "GPA"
    :precondition: player must be a dictionary with keys "time", "GPA" and "social" values as int, float, and int
                   respectively
    :precondition: social_limit must be a positive int
    :postcondition: reduce player's time by a random amount in range [1, 10], GPA by 0.2 and social score by 15
    :return: the updated player dictionary and value of time key
    """
    time_lost = random.randint(1, 10)
    player["time"] = adjust_time(player["time"], -time_lost)  # Random time reduction between 1 and 10 (severeness)
    player["GPA"] = adjust_gpa(player["GPA"], -0.2)
    player["social"] = adjust_social(player["social"], -15)
    return [player, time_lost]


def volunteering_event_adjustment(player):
    """
    Adjust the player's attributes for volunteering, affecting time, GPA and social.

    :param player: a dictionary representing the player's state, including "time" and "GPA"
    :precondition: player must be a dictionary with keys "time", "GPA" and "social" values as int, float, and int
                   respectively
    :precondition: social_limit must be a positive int
    :postcondition: reduce player's time by 20, GPA by 0.05 and increase social score by 15
    :return: the updated player dictionary

    >>> volunteering_event_adjustment({"time": 200, "GPA": 2.5, "social": 10}, 80)
    You have done volunteering for the Day Care Center. You had a very great time.
    You have earned 0.05 GPA points and 30 units of social score in the process.
    Now you have 2.55 points, 40 social score and
    Remember you need to balance your time, GPA and social to graduate.
    {'time': 180, 'GPA': 2.55, 'social': 40}

    >>> volunteering_event_adjustment({"time": 180, "GPA": 3.95, "social": 5}, 80)
    You have done volunteering for the Day Care Center. You had a very great time.
    You have earned 0.05 GPA points and 30 units of social score in the process.
    Now you have 4.00 points, 35 social score and
    Remember you need to balance your time, GPA and social to graduate.
    {'time': 160, 'GPA': 4.0, 'social': 35}
    """
    player["time"] = adjust_time(player["time"], -20)
    player["GPA"] = adjust_gpa(player["GPA"], 0.05)
    player["social"] = adjust_social(player["social"], 30)
    print_gradually(f"You have done volunteering for the Day Care Center. You had a very great time.\n"
                    f"You have earned 0.05 GPA points and 30 units of social score in the process.\n"
                    f"Now you have {player['GPA']:.2f} points, {player['social']} social score and\n"
                    f"Remember you need to balance your time, GPA and social to graduate.")
    return player


def test_run_adjustments():
    """
    Test the functions in this module.
    """
    # Initialize a player dictionary
    user = {"time": 100, "GPA": 1.8, "social": 50, "location": 1}

    # Example cases to see functions are working properly or not
    user = assignment_event_adjustment(user)
    print(user)
    user = study_session_event_adjustment(user)
    print(user)
    user1 = sick_event_adjustment(user)
    print(user)
    user = social_event_adjustment(user)
    print(user)
    user = volunteering_event_adjustment(user)
    print(user)

    user = exam_event_adjustment(user, True)  # Player passes the exam
    print(user)
    print(user1)


if __name__ == "__main__":
    test_run_adjustments()

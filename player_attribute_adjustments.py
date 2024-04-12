import random
import narrative


def adjust_gpa(gpa, change):
    """
    Adjust player's GPA based on the given change, ensuring it is in range [0.0, 4.0].

    :param gpa: current GPA of the player
    :param change: amount to adjust the GPA by
    :precondition: gpa must be a float within the range 0.0 to 4.0, inclusive
    :precondition: change must be a float
    :postcondition: calculate the GPA correctly to 2 decimal places in range [0.0, 4.0] according to the change
    :return: adjusted GPA, rounded to 2 decimal places

    >>> adjust_gpa(3.95, 0.1)
    4.0
    >>> adjust_gpa(2.5, -0.3)
    2.2

    """
    updated_gpa = gpa + change
    if updated_gpa > 4.0:
        return 4.0
    elif updated_gpa < 0:
        return 0
    else:
        return updated_gpa


def adjust_social(social, change, limit):
    """
    Adjust a player's social score based on the given change, ensuring it stays within 0 to limit.

    :param social: current social score of the player
    :param change: amount to adjust the social score by
    :param limit: the max social value allowed
    :precondition: social must be an integer within the range 0 to limit
    :precondition: change must be an integer that can be positive or negative
    :postcondition: calculate social score correctly, ensuring it stays within the range 0 to limit, inclusive
    :return: the adjusted social score as an integer

    >>> adjust_social(95, 10, 95)
    95
    >>> adjust_social(5, -10, 100)
    0
    >>> adjust_social(50, -20, 100)
    30
    """
    updated_social = social + change
    if updated_social > limit:
        return limit
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
    {'time': 95, 'GPA': 3.6, 'social': 50}

    >>> assignment_event_adjustment({"time": 50, "GPA": 3.9, "social": 50})
    {'time': 45, 'GPA': 4.0, 'social': 50}
    """
    player["time"] = adjust_time(player["time"], -5)
    player["GPA"] = adjust_gpa(player["GPA"], 0.1)
    print(f"You have completed an assignment, Great Job!\n"
          f"You have earned 0.1 GPA points and lost 10 units of time in the process.\n"
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
    {'time': 185, 'GPA': 3.2, 'social': 50}

    >>> exam_event_adjustment({"time": 200, "GPA": 3.0, "social": 50}, False)
    {'time': 185, 'GPA': 2.8, 'social': 50}
    """

    player["time"] -= 15
    if state is True:
        player["GPA"] = adjust_gpa(player["GPA"], 0.2)
        print(f"You have passed the exam. Congratulations!\n"
              f"You have earned 0.2 GPA points.\n"
              f"Now you have {player['GPA']} GPA points and {player['time']} units of time left.\n")

    else:
        player["GPA"] = adjust_gpa(player["GPA"], - 0.2)
        print(f"You have failed the exam. You have lost 0.2 GPA points.\n"
              f"Remember you need to balance your time and GPA and social to graduate.\n"
              f"You failed the ultimate test. You are leaving the school.\n")

    return player


def study_session_event_adjustment(player, social_limit):
    """
    Adjust the player's attributes for doing a study session, affecting time, GPA and social.

    :param player: a dictionary representing the player's state, including "time", "GPA", and "social"
    :param social_limit: maximum social status allowed
    :precondition: player must be a dictionary with keys "time", "GPA" and "social" values as int, float, and int
                   respectively
    :precondition: social_limit must be a positive int
    :postcondition: reduce player's time by 8, increase GPA by 0.05 and reduce social score by 5
    :return: the updated player dictionary

    >>> study_session_event_adjustment({"time": 120, "GPA": 2.8, "social": 50}, 80)
    {'time': 112, 'GPA': 2.85, 'social': 45}

    >>> study_session_event_adjustment({"time": 80, "GPA": 3.95, "social": 10}, 80)
    {'time': 72, 'GPA': 4.0, 'social': 5}
    """
    player["time"] = adjust_time(player["time"], -15)
    player["GPA"] = adjust_gpa(player["GPA"], 0.05)
    player["social"] = adjust_social(player["social"], -5, social_limit)
    player["location"] += 1
    print(f"You have completed a study session. Great Job! ")
    print(f"You have earned 0.05 GPA points and lost 5 units of social score in the process. ")
    print(f"Remember you need to balance your time and GPA and social to graduate. ")
    print(f"Now you have {player['GPA']:.2f} GPA, {player['social']} social score and {player['time']} units of time"
          f"left.")
    return player


def social_event_adjustment(player, social_limit):
    """
    Adjust the player's attributes for going to a social event, affecting time, GPA and social.

    :param player: a dictionary representing the player's state, including "time" and "GPA"
    :param social_limit: max social status allowed
    :precondition: player must be a dictionary with keys "time", "GPA" and "social" values as int, float, and int
                   respectively
    :precondition: social_limit must be a positive int
    :postcondition: reduce player's time by 10, GPA by 0.08 and increase social score by 10
    :return: the updated player dictionary

    >>> social_event_adjustment({"time": 150, "GPA": 3.6, "social": 30}, 80)
    {'time': 140, 'GPA': 3.52, 'social': 40}

    >>> social_event_adjustment({"time": 90, "GPA": 2.0, "social": 60}, 80)
    {'time': 80, 'GPA': 1.92, 'social': 70}

    """
    player["time"] = adjust_time(player["time"], -10)
    player["GPA"] = adjust_gpa(player["GPA"], -0.08)
    player["social"] = adjust_social(player["social"], 10, social_limit)
    player["location"] += 1
    print(f"You have attended a social event. You made good connections at the event Great Job! "
          f"You have lost 0.08 GPA points and earned 10 units of social score in the process. "
          f"Remember you need to balance your time and GPA and social to graduate. "
          f"Now you have {player['GPA']} GPA points, {player['social']} social score and {player['time']} units of time"
          f"left.")
    return player


def sick_event_adjustment(player, social_limit):
    """
    Adjust the player's attributes for being sick, affecting time, GPA and social.

    :param player: a dictionary representing the player's state, including "time" and "GPA"
    :param social_limit: max social status allowed
    :precondition: player must be a dictionary with keys "time", "GPA" and "social" values as int, float, and int
                   respectively
    :precondition: social_limit must be a positive int
    :postcondition: reduce player's time by a random amount in range [1, 10], GPA by 0.2 and social score by 15
    :return: the updated player dictionary and value of time key
    """
    time_lost = random.randint(1, 10)
    player["time"] = adjust_time(player["time"], -time_lost)  # Random time reduction between 1 and 10 (severeness)
    player["GPA"] = adjust_gpa(player["GPA"], -0.2)
    player["social"] = adjust_social(player["social"], -15, social_limit)
    return [player, time_lost]


def volunteering_event_adjustment(player, social_limit):
    """
    Adjust the player's attributes for volunteering, affecting time, GPA and social.

    :param player: a dictionary representing the player's state, including "time" and "GPA"
    :param social_limit: max social status allowed
    :precondition: player must be a dictionary with keys "time", "GPA" and "social" values as int, float, and int
                   respectively
    :precondition: social_limit must be a positive int
    :postcondition: reduce player's time by 20, GPA by 0.05 and increase social score by 15
    :return: the updated player dictionary

    >>> volunteering_event_adjustment({"time": 200, "GPA": 2.5, "social": 10}, 80)
    You have done volunteering for the Day Care Center. You had a very great time.
    {'time': 180, 'GPA': 2.55, 'social': 25}

    >>> volunteering_event_adjustment({"time": 180, "GPA": 3.95, "social": 5}, 80)
    You have done volunteering for the Day Care Center. You had a very great time.
    {'time': 160, 'GPA': 4.0, 'social': 20}
    """
    player["time"] = adjust_time(player["time"], -20)
    player["GPA"] = adjust_gpa(player["GPA"], 0.05)
    player["social"] = adjust_social(player["social"], 30, social_limit)
    narrative.print_gradually(f"You have done volunteering for the Day Care Center. You had a very great time.\n"
                              f"You have earned 0.05 GPA points and 30 units of social score in the process.\n"
                              f"Now you have {player['GPA']} GPA points, {player['social']} social score and\n"
                              f"Remember you need to balance your time, GPA and social to graduate.")
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
        player["time"] = adjust_time(player["time"], -20)
        player["GPA"] = 2.8  # GPA is set to 2.8 for next year if player passes the recovery exam
        return player


def vacation_event_adjustment(player, vac_length):
    """
    Adjust the player's attributes based on the outcome of a vacation, affecting time.
    :param player: a dictionary representing the player's state, including "time" and "GPA"
    :param vac_length: total vacacation length units
    :precondition: player must be a dictionary that has a key "time" with its value int
    :postcondition: increase the player's time according to the vac_length
    :return: updated player dictionary
    """
    player["time"] += vac_length
    return player


def test_run_adjustments():
    # Initialize a player dictionary
    user = {"time": 100, "GPA": 1.8, "social": 50}
    social_limit_user = 80

    # Example cases to see functions are working properly or not
    user = assignment_event_adjustment(user)
    print(user)
    user = study_session_event_adjustment(user, social_limit_user)
    print(user)
    user = sick_event_adjustment(user, social_limit_user)
    print(user)
    user = social_event_adjustment(user, social_limit_user)
    print(user)
    user = volunteering_event_adjustment(user, social_limit_user)
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

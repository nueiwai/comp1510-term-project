import random
import itertools
import mini_games
import character
import player_attribute_adjustments

"""
This module contains functions that trigger events and games in the game.
functions:
    - distribute_sick_events_each_term(base_frequency=1, extra_frequency=2, grid_start=1, grid_end=19)
    - sick_event(player, time_lost)
    - distribute_volunteering_events_each_term(location_triggers_sick, grid_start=1, grid_end=19)
    - quiz_questions()
    - trigger_quiz(player, term, shift_limit=10, shift_grid=0, number_upperbound=100, base_upperbound=3, 
    roman_upbound=100)
    - player_choice_for_event_participation(event_name)
    - trigger_study_session(player, player_choice_study_session)
    - trigger_assignment(player, player_choice)
    - process_player_daily_events(player, term)
    
"""


def distribute_sick_events_each_term(base_frequency=1, extra_frequency=2, grid_start=1, grid_end=19):
    """
    Distribute sick events each term.

    :param base_frequency: an integer that represents the base frequency of sick events
    :param extra_frequency: an integer that represents the extra frequency of sick events
    :param grid_start: an integer that represents the start of the grid
    :param grid_end: an integer that represents the end of the grid
    :precondition: base_frequency must be a positive integer
    :precondition: extra_frequency must be a positive integer
    :precondition: grid_start must be a positive integer
    :precondition: grid_end must be a positive integer
    :postcondition: distribute sick events each term
    :return: a list of integers that represents the locations that trigger sick events

    """
    locations_triggers_sick = []
    for _ in range(base_frequency):
        event_position = random.randint(grid_start, grid_end)
        locations_triggers_sick.append(event_position)

    extra_events = random.randint(0, extra_frequency)
    for _ in range(extra_events):
        event_position = random.randint(1, grid_end)
        locations_triggers_sick.append(event_position)

    return locations_triggers_sick


def sick_event(player, time_lost):
    """
    Trigger a sick event based on the player's health condition.

    :param player: a dictionary that stores the character's attributes
    :param time_lost: an integer that represents the time lost due to sickness
    :precondition: player must be a dictionary with keys "time", "GPA", "social", and "location"
    :precondition: time_lost must be a positive integer
    :postcondition: trigger a sick event based on the player's health condition
    :postcondition: return a dictionary that stores the character's attributes
    :return: a dictionary that stores the character's attributes

    >>> test_player = {'time': 100, 'GPA': 3.5, 'social': 50, 'location': 1}
    >>> sick_event(test_player, 3)
    You had a minor sickness. You lost 3 units of time.You slept for three days to feel better...
    Now you have 3.50 GPA points, 50 social score and 97 units of time left.
    {'time': 97, 'GPA': 3.5, 'social': 50, 'location': 4}
    """
    text = (f"You slept for three days to feel better...\n"
            f"Now you have {player['GPA']:.2f} GPA points, {player['social']} social score and {player['time']} units "
            f"of time left.\n")
    if time_lost > 7:
        player["location"] += 3
        print(f"You had a very severe sickness. You lost {time_lost} units of time.\n" + text)
    elif time_lost > 4:
        player["location"] += 3
        print(f"You had a severe sickness. You lost {time_lost} units of time.\n" + text)
    elif time_lost > 2:
        player["location"] += 3
        print(f"You had a mild sickness. You lost {time_lost} units of time.\n" + text)
    else:
        player["location"] += 3
        print(f"You had a minor sickness. You lost {time_lost} units of time.\n" + text)
    return player


def distribute_volunteering_events_each_term(location_triggers_sick, grid_start=1, grid_end=19):
    """
    Distribute volunteering events each term.

    :param location_triggers_sick: a list of integers that represents the locations that trigger sick events
    :param grid_start: an integer that represents the start of the grid
    :param grid_end: an integer that represents the end of the grid
    :precondition: location_triggers_sick must be a list of integers
    :precondition: grid_start must be a positive integer
    :precondition: grid_end must be a positive integer
    :postcondition: distribute volunteering events each term
    :return: a list of integers that represents the locations that trigger volunteering events

    """
    locations_without_sick = [_ for _ in range(grid_start, grid_end + 1)]
    for _ in location_triggers_sick:
        if _ in locations_without_sick:
            locations_without_sick.remove(_)

    locations_trigger_volunteering = random.choices(locations_without_sick, k=5)
    return locations_trigger_volunteering


def quiz_questions():
    subset_questions = ["C", "B", "R", "R", "B", "C"]
    question_cycle = itertools.cycle(subset_questions)

    questions_list = []
    for grid_no, question in enumerate(question_cycle, 1):
        questions_list.append((grid_no, question))
        if grid_no == 100:
            break
    return questions_list


def trigger_quiz(player, term, shift_limit=10, shift_grid=0, number_upperbound=100, base_upperbound=3,
                 roman_upbound=100):
    """
    Trigger a quiz event based on the player's location.

    :param player: a dictionary that stores the character's attributes
    :param term: an integer that represents the current term
    :param shift_limit: an integer that represents the limit of shift in Caesar Cipher game
    :param shift_grid: an integer that represents the shift in the grid
    :param number_upperbound: an integer that represents the upperbound for the number in base conversion game
    :param base_upperbound: an integer that represents the upperbound for the base in base conversion game
    :param roman_upbound: an integer that represents the upperbound for the Roman numeral in Roman numeral conversion
                          game
    :precondition: player must be a dictionary with keys "time", "GPA", "social", and "location"
    :precondition: term must be an integer
    :precondition: shift_limit must be a positive integer
    :precondition: shift_grid must be a positive integer
    :precondition: number_upperbound must be a positive integer
    :precondition: base_upperbound must be a positive integer
    :precondition: roman_upbound must be a positive integer
    :postcondition: trigger a quiz event based on the player's location
    :return: a dictionary that stores the character's attributes

    """
    assigned_questions = quiz_questions()
    for location, question in assigned_questions:
        if player["location"] + shift_grid == location:
            if question == "B":
                mini_games.play_base_conversion_game(player, number_upperbound, base_upperbound)
            elif question == "C":
                mini_games.play_caesar_cipher_game(player, term, shift_limit)
            elif question == "R":
                mini_games.play_roman_numeral_conversion_game(player, roman_upbound)
    return player


def player_choice_for_event_participation(event_name):
    """
    Ask the player if they want to participate in an event.

    :param event_name: a string that represents the name of the event
    :precondition: event_name must be a string
    :postcondition: ask the player if they want to participate in an event
    :postcondition: return True if the player chooses to participate in the event, False otherwise
    :return: a boolean that represents the player's choice for event participation

    """
    while True:
        try:
            player_choice = input(f"Do you want to do {event_name}? (y/n)")
            if player_choice.upper() == "Y":
                return True
            elif player_choice.upper() == "N":
                return False
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter letters 'y' or 'n'.")
            continue


def trigger_study_session(player, player_choice_study_session):
    if player_choice_study_session:
        player_attribute_adjustments.study_session_event_adjustment(player, 100)
    else:
        print("You chose not to study. Remember, every decision counts!")
        print(f"You have {player['GPA']:.2f} GPA, {player['social']} social score and {player['time']} units of time\n")
    return player


def trigger_assignment(player, player_choice):
    """
    Trigger an assignment event based on the player's choice.

    :param player: a dictionary that stores the character's attributes
    :param player_choice: a boolean that represents the player's choice for assignment participation
    :precondition: player must be a dictionary with keys "time", "GPA", "social", and "location"
    :precondition: player_choice must be a boolean
    :postcondition: trigger an assignment event based on the player's choice
    :postcondition: return a dictionary that stores the character's attributes
    :return: a dictionary that stores the character's attributes

    """
    if player_choice:
        player_attribute_adjustments.assignment_event_adjustment(player)
    else:
        print("You chose not to do the assignment. Remember, every decision counts!")
        print(f"You have {player['GPA']:.2f} GPA, {player['social']} social score and {player['time']} units of time\n")
    return player


def process_player_daily_events(player, term):
    """
    Process the player's daily events.

    :param player: a dictionary that stores the character's attributes
    :param term: an integer that represents the current term
    :precondition: player must be a dictionary with keys "time", "GPA", "social", and "location"
    :precondition: term must be a positive integer in range [1, 4]
    :postcondition: process the player's daily events
    :return: a dictionary that stores the character's attributes

        """
    # Trigger the player's choice for assignment participation
    player_choice_assignment = player_choice_for_event_participation("assignment")
    player = trigger_assignment(player, player_choice_assignment)

    # Trigger the player's choice for study session participation
    player_choice_study_session = player_choice_for_event_participation("study_session")
    player = trigger_study_session(player, player_choice_study_session)

    # Trigger a quiz event
    player = trigger_quiz(player, term)

    if not (player_choice_assignment and player_choice_study_session):
        player = character.update_player_location(player, True)
        return player, True
    else:
        player = character.update_player_location(player, False)
        return player, False


if __name__ == "__main__":
    """
    Test the function trigger_quiz().
    """
    game_player = {"time": 200, "GPA": 2.5, "social": 10, "location": 1}
    game_term = 1
    trigger_quiz(game_player, game_term)

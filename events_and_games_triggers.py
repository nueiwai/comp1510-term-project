import random
import itertools
import mini_games
import player_attribute_adjustments


def distribute_sick_events_each_term(base_frequency=1, extra_frequency=2, grid_start=1, grid_end=19):
    """

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


def distribute_volunteering_events_each_term(location_triggers_sick, grid_start=1, grid_end=19):
    """
    >>> distribute_volunteering_events_each_term([1, 6], 1, 25)
    [2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    """
    locations_without_sick = [_ for _ in range(grid_start, grid_end + 1)]
    for _ in location_triggers_sick:
        if _ in locations_without_sick:
            locations_without_sick.remove(_)

    locations_trigger_volunteering = random.choices(locations_without_sick, k=5)
    return locations_trigger_volunteering


def quiz_questions():
    full_questions_list = []
    questions = itertools.cycle(["C", "B", "R", "R", "B", "C"])
    for _ in range(25):
        full_questions_list.append(next(questions))

    different_questions = list(enumerate(full_questions_list, 1))
    print(different_questions)
    return different_questions


def trigger_quiz(player, term, shift_limit=10, shift_grid=0, number_upperbound=100, base_upperbound=3,
                 roman_upbound=100):
    """

    :param player:
    :param term:
    :param shift_limit:
    :param shift_grid:
    :param number_upperbound:
    :param base_upperbound:
    :param roman_upbound:
    :return:


    """
    assigned_questions = [(1, 'C'), (2, 'B'), (3, 'R'), (4, 'R'), (5, 'B'), (6, 'C'), (7, 'C'), (8, 'B'), (9, 'R'),
                          (10, 'R'), (11, 'B'), (12, 'C'), (13, 'C'), (14, 'B'), (15, 'R'), (16, 'R'), (17, 'B'),
                          (18, 'C'), (19, 'C'), (20, 'B'), (21, 'R'), (22, 'R'), (23, 'B'), (24, 'C'), (25, 'C')]
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
    player_choice = input(f"Do you want to do {event_name}? (y/n)")
    if player_choice.upper() == "Y":
        return True
    else:
        return False


def trigger_study_session(player, player_choice_study_session):
    if player_choice_study_session:
        player_attribute_adjustments.study_session_event_adjustment(player, 100)
    else:
        print("You chose not to study. Remember, every decision counts!")
        print(f"You have {player['GPA']} GPA, {player['social']} social score and {player['time']} units of time\n")
    return player


def trigger_assignment(player, player_choice):
    if player_choice:
        player_attribute_adjustments.assignment_event_adjustment(player)
    else:
        print("You chose not to do the assignment. Remember, every decision counts!")
        print(f"You have {player['GPA']} GPA, {player['social']} social score and {player['time']} units of time\n")
    return player


def sick_event(player, time_lost):
    text = (f"You slept for three days to feel better...\n"
            f"Now you have {player['GPA']} GPA points, {player['social']} social score and {player['time']} units of "
            f"time left.\n")
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


if __name__ == "__main__":
    game_player = {"time": 200, "GPA": 2.5, "social": 10, "location": 1}
    game_term = 1
    trigger_quiz(game_player, game_term)

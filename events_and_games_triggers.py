import random
import itertools
import mini_games
import character
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


def sick_event(player, time_lost):
    text = (f"You slept for three days to feel better...\n"
            f"Now you have {player['GPA']:.2f} GPA points, {player['social']} social score and {player['time']} units of "
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

    :param player:
    :param term:
    :param shift_limit:
    :param shift_grid:
    :param number_upperbound:
    :param base_upperbound:
    :param roman_upbound:
    :return:


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
    if player_choice:
        player_attribute_adjustments.assignment_event_adjustment(player)
    else:
        print("You chose not to do the assignment. Remember, every decision counts!")
        print(f"You have {player['GPA']:.2f} GPA, {player['social']} social score and {player['time']} units of time\n")
    return player


def process_player_daily_events(player, term):
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
    game_player = {"time": 200, "GPA": 2.5, "social": 10, "location": 1}
    game_term = 1
    trigger_quiz(game_player, game_term)

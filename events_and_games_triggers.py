import random
import itertools
import mini_games
import player_attribute_adjustments

def distribute_sick_events_each_term(base_frequency=1, extra_frequency=2):
    """

    """
    grid_coverage = 25
    locations_triggers_sick = []
    for _ in range(base_frequency):
        event_position = random.randint(1, grid_coverage)
        locations_triggers_sick.append(event_position)

    extra_events = random.randint(0, extra_frequency)
    for _ in range(extra_events):
        event_position = random.randint(1, grid_coverage)
        locations_triggers_sick.append(event_position)

    return locations_triggers_sick


def distribute_volunteering_events_each_term(location_triggers_sick, grid_start=1, grid_end=25):
    """

    """
    locations_without_sick = [_ for _ in range(grid_start, grid_end + 1)]
    for _ in location_triggers_sick:
        if _ in locations_without_sick:
            locations_without_sick.remove(_)
    locations_trigger_volunteering = random.choices(locations_without_sick, k=2)
    return locations_trigger_volunteering


def quiz_questions():
    full_questions_list =[]
    questions = ["C", "B", "R", "R", "B", "C"]
    for _ in range(25):
        full_questions_list.append(next(itertools.cycle(questions)))

    different_questions = list(enumerate(full_questions_list, 1))
    return different_questions


def trigger_quiz(player, term, shift_limit=10, shift_grid=0, number_upperbound=100, base_upperbound=3,
                 roman_upbound=100):
    assigned_questions = quiz_questions()
    for location, question in assigned_questions:
        if player["location"] + shift_grid == location:
            if question == "B":
                mini_games.play_base_conversion_game(player["GPA"], number_upperbound, base_upperbound)
            elif question == "C":
                mini_games.play_caesar_cipher_game(player["GPA"], term, shift_limit)
            elif question == "R":
                mini_games.play_roman_numeral_conversion_game(player["GPA"], roman_upbound)


def player_choice_for_event_participation(event_name):
    player_choice = input(f"Do you want to do {event_name}? (y/n)")
    if player_choice.upper() == "Y":
        return True
    else:
        return False


def trigger_assignment(player, player_choice):
    if player_choice:
        player_attribute_adjustments.assignment_event_adjustment(player)
    else:
        print("You chose not to do the assignment. Remember, every decision counts!")


def sick_event(player, time_lost):
    if time_lost > 7:
        player["location"] += 3
        print(f"You had a very severe sickness. You lost {time_lost} units of time."
              f"You slept for three days to feel better...")
    elif time_lost > 4:
        print(f"You had a severe sickness. You lost {time_lost} units of time."
              f"You slept for three days to feel better...")
    elif time_lost > 2:
        print(f"You had a mild sickness. You lost {time_lost} units of time."
              f"You slept for three days to feel better...")
    else:
        print(f"You had a minor sickness. You lost {time_lost} units of time."
              f"You slept for three days to feel better...")

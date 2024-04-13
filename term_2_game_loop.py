import map_components
import events_and_games_triggers
import player_attribute_adjustments
import character
import narrative
import exam
from term_3_game_loop import term_3_game_loop


def term_2_game_loop(player, co_op_evaluation_point):
    sick_positions = events_and_games_triggers.distribute_sick_events_each_term(base_frequency=1, extra_frequency=0,
                                                                                grid_start=26, grid_end=44)
    volunteering_positions = events_and_games_triggers.distribute_volunteering_events_each_term(sick_positions,
                                                                                                grid_start=26,
                                                                                                grid_end=44)
    social_event_positions = [28, 33, 38, 43, 48]

    player = character.make_character_each_term_start(player)
    game_map = map_components.generate_term_map()
    term = 2

    while player["location"] < 75 and player["time"] > 5 and 2.8 <= player["GPA"] <= 4.0:
        narrative.print_map_repeatedly(player, game_map)

        if player["location"] in sick_positions:
            time_lost = player_attribute_adjustments.sick_event_adjustment(player)
            player = events_and_games_triggers.sick_event(player, time_lost[1])
            narrative.print_map_repeatedly(player, game_map)

        if player["location"] in volunteering_positions:
            player = player_attribute_adjustments.volunteering_event_adjustment(player)

        if player["location"] in social_event_positions:
            player = player_attribute_adjustments.social_event_adjustment(player)
            narrative.print_map_repeatedly(player, game_map)

        (player, slept) = events_and_games_triggers.process_player_daily_events(player, term, shift_limit=10,
                                                                                number_upperbound=80,
                                                                                base_upperbound=3, roman_upbound=100)
        if not slept:
            continue

    if player["location"] == 75:
        exam_state = exam.exam(term)
        player_attribute_adjustments.exam_event_adjustment(player, exam_state)
        if not exam_state:
            narrative.drop_out()
        else:
            print("you passed the exam")
            narrative.bonus_part(co_op_evaluation_point)
            player["location"] += 1  # add 1 grid to reach grid 51
            term_3_game_loop(player)

    elif player["time"] < 5:
        narrative.print_gradually("You have running out of time to complete the term. So we are checking your status "
                                  "whether you meet the requirements to graduate now.")
        narrative.waiting(2)
        if player["GPA"] >= 2.8:
            narrative.print_gradually("You have met the GPA requirement to graduate this term. Checking social status")
            narrative.waiting(2)
            if player["social"] > 90:
                narrative.print_gradually("You have met the social requirement to graduate this term. Congratulations! "
                                          "You have graduated this term. Isn't that great? You don't need to take the "
                                          "exam.!!!!!\n ")
                term_3_game_loop(player)
            else:
                narrative.print_gradually("You didn't meet the social requirement to graduate this term. You have to "
                                          "drop out sorry.")

        else:
            narrative.print_gradually("You didn't meet the GPA requirement to graduate this term. You have to drop out "
                                      "sorry.")

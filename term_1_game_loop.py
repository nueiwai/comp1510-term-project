from narrative import welcome_message
import map_components
import events_and_games_triggers
import character
import player_attribute_adjustments
import narrative
import exam
from term_2_game_loop import term_2_game_loop


def term_1_game_loop():

    welcome_message()

    sick_positions = events_and_games_triggers.distribute_sick_events_each_term(base_frequency=1, extra_frequency=0)
    volunteering_positions = events_and_games_triggers.distribute_volunteering_events_each_term(sick_positions)
    social_event_positions = [3, 8, 13, 18, 23]

    player = character.make_character()
    game_map = map_components.generate_term_map()
    term = 1

    while player["location"] < 25 and player["time"] > 5 and 2.8 <= player["GPA"] <= 4.0:
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

        (player, slept) = events_and_games_triggers.process_player_daily_events(player, term)
        if not slept:
            continue

    if player["location"] == 25:
        exam_state = exam.exam(term)
        player_attribute_adjustments.exam_event_adjustment(player, exam_state)
        if not exam_state:
            narrative.drop_out()
        else:
            print("you passed the exam")
            player["location"] += 1  # add 1 grid to reach grid 26
            co_op_evaluation_point = player  # store term 1 gpa for co-op evaluation
            term_2_game_loop(player, co_op_evaluation_point)

    elif player["time"] < 5 or player["time"] == 0:
        narrative.print_gradually("You have running out of time to complete the term. So we are checking your status "
                                  "whether you meet the requirements to graduate now.")
        narrative.waiting(2)
        if player["GPA"] >= 2.8:
            narrative.print_gradually("You have met the GPA requirement to graduate this term. Checking social status")
            narrative.waiting(2)
            if player["social"] > 70:
                narrative.print_gradually("You have met the social requirement to graduate this term. Congratulations! "
                                          "You have graduated this term. Isn't that great? You don't need to take the "
                                          "exam.!!!!!\n")
                player["location"] = 26  # assign grid 26 from anywhere in term 1
                co_op_evaluation_point = player  # store term 1 gpa for co-op evaluation
                term_2_game_loop(player, co_op_evaluation_point)
            else:
                narrative.print_gradually("You didn't meet the social requirement to graduate this term. You have to "
                                          "drop out sorry.")

        else:
            narrative.print_gradually("You didn't meet the GPA requirement to graduate this term. You have to drop out "
                                      "sorry.")


if __name__ == "__main__":
    term_1_game_loop()

from narrative import welcome_message
import map_components
import events_and_games_triggers
import player_attribute_adjustments
import character
import narrative
import exam
# import term_2_game_loop


def term_1_game_loop():

    welcome_message()

    sick_positions = events_and_games_triggers.distribute_sick_events_each_term(base_frequency=1, extra_frequency=0)
    volunteering_positions = events_and_games_triggers.distribute_volunteering_events_each_term(sick_positions)

    player = character.make_character()
    game_map = map_components.generate_term_map()
    term = 1
    social_limit = 100

    while player["location"] < 25 and player["time"] > 5 and 2.8 <= player["GPA"] < 4.0:
        map_components.print_game_map(player)
        map_components.describe_current_location(game_map, player)

        if player["location"] in sick_positions:
            time_lost = player_attribute_adjustments.sick_event_adjustment(player, social_limit)
            player = events_and_games_triggers.sick_event(player, time_lost[1])
            map_components.print_game_map(player)
            map_components.describe_current_location(game_map, player)

        if player["location"] in volunteering_positions:
            player = player_attribute_adjustments.volunteering_event_adjustment(player, social_limit)

        social_event_positions =[3, 8, 13, 18, 23]
        if player["location"] in social_event_positions:
            player = player_attribute_adjustments.social_event_adjustment(player, social_limit)
            map_components.print_game_map(player)
            map_components.describe_current_location(game_map, player)

        player_choice_assignment = events_and_games_triggers.player_choice_for_event_participation("assignment")
        player = events_and_games_triggers.trigger_assignment(player, player_choice_assignment)

        player_choice_study_session = events_and_games_triggers.player_choice_for_event_participation("study_session")
        player = events_and_games_triggers.trigger_study_session(player, player_choice_study_session)

        player = events_and_games_triggers.trigger_quiz(player, term)

        if (not player_choice_assignment and player_choice_study_session) or (not player_choice_study_session and
                                                                              player_choice_assignment):
            player = character.update_player_location(player, True)
        else:
            player = character.update_player_location(player, False)
            continue

    if player["location"] == 25:
        exam_state = exam.exam(term)
        player_attribute_adjustments.exam_event_adjustment(player, exam_state)
        if not exam_state:
            pass
        else:
            print("you passed the exam")
            # term_2_game_loop()
    if player["time"] < 10:
        if player["GPA"] >= 2.8:
            narrative.print_gradually("You have met the GPA requirement to graduate this term. Checking social status")
            if player["social"] > 70:
                narrative.print_gradually("You have met the social requirement to graduate this term. Congratulations! "
                                          "You have graduated this term.")
            else:
                narrative.print_gradually("You didn't meet the social requirement to graduate this term. You have to "
                                          "drop out sorry.")

        else:
            narrative.print_gradually("You didn't meet the GPA requirement to graduate this term. You have to drop out "
                                      "sorry.")
    elif player["time"] == 0:
        narrative.print_gradually("You have run out of time units. We will check your GPA for your eligibility to the"
                                  "next term.")
        if player["GPA"] >= 2.8:
            narrative.print_gradually("You have met the GPA requirement to graduate this term. Checking social status")
        else:
            narrative.print_gradually("You didn't meet the GPA requirement to graduate this term. You have to drop out "
                                      "sorry.")


if __name__ == "__main__":
    term_1_game_loop()

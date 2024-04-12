import map_components
import events_and_games_triggers
import player_attribute_adjustments
import character
import narrative
import exam
import term_4_game_loop


def term_3_game_loop(player):

    sick_positions = events_and_games_triggers.distribute_sick_events_each_term(base_frequency=1, extra_frequency=0)
    volunteering_positions = events_and_games_triggers.distribute_volunteering_events_each_term(sick_positions)
    social_event_positions = [33, 38, 43, 48, 53]

    player = character.make_character_each_term_start(player)
    game_map = map_components.generate_term_map()
    term = 3
    social_limit = 110

    while player["location"] < 75 and player["time"] > 5 and 2.8 <= player["GPA"] < 4.0:
        narrative.print_map_repeatedly(player, game_map)

        if player["location"] in sick_positions:
            time_lost = player_attribute_adjustments.sick_event_adjustment(player, social_limit)
            player = events_and_games_triggers.sick_event(player, time_lost[1])
            narrative.print_map_repeatedly(player, game_map)

        if player["location"] in volunteering_positions:
            player = player_attribute_adjustments.volunteering_event_adjustment(player, social_limit)

        if player["location"] in social_event_positions:
            player = player_attribute_adjustments.social_event_adjustment(player, social_limit)
            narrative.print_map_repeatedly(player, game_map)

        (player, slept) = events_and_games_triggers.process_player_daily_events(player, term)
        if not slept:
            continue

    if player["location"] == 75:
        exam_state = exam.exam(term)
        player_attribute_adjustments.exam_event_adjustment(player, exam_state)
        if not exam_state:
            narrative.drop_out()

        else:
            print("you passed the exam")
            player["location"] += 1  # add 1 grid to reach grid 76
            term_4_game_loop.term_4_game_loop(player)
    elif player["time"] < 10:
        if player["GPA"] >= 2.8:
            narrative.print_gradually("You have met the GPA requirement to graduate this term. Checking social status")
            if player["social"] > 110:
                narrative.print_gradually("You have met the social requirement to graduate this term. Congratulations! "
                                          "You have graduated this term.")
                term_4_game_loop.term_4_game_loop(player)
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
            if player["social"] > 110:
                narrative.print_gradually("You have met the social requirement to graduate this term. Congratulations! "
                                          "You have graduated this term.")
                term_4_game_loop.term_4_game_loop(player)
        else:
            narrative.print_gradually("You didn't meet the GPA requirement to graduate this term. You have to drop out "
                                      "sorry.")


if __name__ == "__main__":
    term_3_game_loop({'time': 150, 'GPA': 3.5, 'social': 70, 'location': 51})
import map_components
import events_and_games_triggers
import player_attribute_adjustments
import character
import narrative
import exam
import post_graduation


def term_4_game_loop(player):
    sick_positions = events_and_games_triggers.distribute_sick_events_each_term(base_frequency=1, extra_frequency=0,
                                                                                grid_start=76, grid_end=94)
    volunteering_positions = events_and_games_triggers.distribute_volunteering_events_each_term(sick_positions,
                                                                                                grid_start=76,
                                                                                                grid_end=94)
    social_event_positions = [78, 83, 88, 93, 98]

    player = character.make_character_each_term_start(player)
    game_map = map_components.generate_term_map()
    term = 4

    while player["location"] < 100 and player["time"] > 5 and 2.8 <= player["GPA"] <= 4.0:
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

        (player, slept) = events_and_games_triggers.process_player_daily_events(player, term, shift_limit=20,
                                                                                number_upperbound=120,
                                                                                base_upperbound=5, roman_upbound=200)
        if not slept:
            continue

    if player["location"] == 100:
        exam_state = exam.exam(term)
        player_attribute_adjustments.exam_event_adjustment(player, exam_state)
        if not exam_state:
            narrative.drop_out()
        else:
            narrative.print_gradually(f"Hooray!!! you passed the exam You graduated from CST nowwww. Congratulations!!!"
                                      f"\nYou are now a graduate. You can now proceed to the post-graduation phase.\n"
                                      f"Please wait for the next phase to start.")
            narrative.waiting(3)
            post_graduation.job_interview()

    elif player["time"] < 5:
        narrative.print_gradually("You have running out of time to complete the term. So we are checking your status "
                                  "whether you meet the requirements to graduate now.")
        narrative.waiting(2)
        if player["GPA"] >= 2.8:
            narrative.print_gradually("You have met the GPA requirement to graduate this term. Checking social status")
            narrative.waiting(2)
            if player["social"] > 110:
                narrative.print_gradually("You have met the social requirement to graduate this term. Congratulations! "
                                          "You have graduated this term. Isn't that great? You don't need to take the "
                                          "exam.!!!!!\nYou can now proceed to the post-graduation phase.\n")
                narrative.waiting(3)
                post_graduation.job_interview()
            else:
                narrative.print_gradually("You didn't meet the social requirement to graduate this term. You have to "
                                          "drop out sorry.")

        else:
            narrative.print_gradually("You didn't meet the GPA requirement to graduate this term. You have to drop out "
                                      "sorry.")


if __name__ == "__main__":
    term_4_game_loop({'time': 180, 'GPA': 3.5, 'social': 80, 'location': 76})

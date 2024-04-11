from narrative import welcome_message
import map_components
import events_and_games_triggers
import player_attribute_adjustments
import character
import narrative


def term_1_game_loop():

    welcome_message()

    sick_positions = events_and_games_triggers.distribute_sick_events_each_term(base_frequency=1, extra_frequency=0)
    volunteering_positions = events_and_games_triggers.distribute_volunteering_events_each_term(sick_positions)

    player = character.make_character()
    game_map = map_components.generate_term_map()
    term = 1
    social_limit = 100
    slept_yesterday = False

    while player["location"] < 26 and player["time"] > 0 and player["GPA"] < 4.0:
        map_components.print_game_map(player)
        map_components.describe_current_location(game_map, player)

        if player["location"] in sick_positions:
            time_lost = player_attribute_adjustments.sick_event_adjustment(player, social_limit)
            events_and_games_triggers.sick_event(player, time_lost)

        if player["location"] in volunteering_positions:
            player_attribute_adjustments.volunteering_event_adjustment(player, social_limit)

        player_choice_assignment = events_and_games_triggers.player_choice_for_event_participation("assignment")
        events_and_games_triggers.trigger_assignment(player, player_choice_assignment)

        events_and_games_triggers.trigger_quiz(player, term)

        sleep_char = character.update_player_location(player, slept_yesterday)
        slept_yesterday = sleep_char[0]
        player = sleep_char[1]

    if player["location"] == 26:
        # Exam loop
    if player["time"] < 5:
       if player["GPA"] >= 2.8:
          narrative.print_gradually("You have met the GPA requirement to graduate this term. Checking social status...")
          if player["social"]
          narrative.waiting(3)



if __name__ == "__main__":
    term_1_game_loop()

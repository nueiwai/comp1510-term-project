from unittest import TestCase
from unittest.mock import patch

import character


class TestUpdatePlayerLocation(TestCase):

    @patch('builtins.input', side_effect=['Y'])
    def test_update_player_location_have_not_slept_location_updates_with_sleep_attempt(self, mock_input):
        slept_yesterday = False
        test_player = {"time": 50, "GPA": 3.5, "social": 80, "location": 24}
        expected = 25
        player_result, slept_result = character.update_player_location(test_player, slept_yesterday)
        actual = player_result["location"]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['N'])
    def test_update_player_location_have_not_slept_location_unchanged_without_sleep_attempt(self, mock_input):
        slept_yesterday = False
        test_player = {"time": 50, "GPA": 3.5, "social": 80, "location": 24}
        expected = 24
        player_result, slept_result = character.update_player_location(test_player, slept_yesterday)
        actual = player_result["location"]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Y'])
    def test_update_player_location_have_slept_location_unchanged_with_sleep_attempt(self, mock_input):
        slept_yesterday = True
        test_player = {"time": 50, "GPA": 3.5, "social": 80, "location": 24}
        expected = 24
        player_result, slept_result = character.update_player_location(test_player, slept_yesterday)
        actual = player_result["location"]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['N'])
    def test_update_player_location_have_slept_location_unchanged_without_sleep_attempt(self, mock_input):
        slept_yesterday = True
        test_player = {"time": 50, "GPA": 3.5, "social": 80, "location": 24}
        expected = 24
        player_result, slept_result = character.update_player_location(test_player, slept_yesterday)
        actual = player_result["location"]
        self.assertEqual(expected, actual)

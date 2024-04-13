from unittest import TestCase
from unittest.mock import patch
from character import update_player_location


class TestUpdatePlayerLocation(TestCase):

    @patch('builtins.input', side_effect=['Y'])
    def test_update_player_location_accomplished_location_skips_one(self, _):
        player = {"time": 50, "GPA": 3.5, "social": 80, "location": 24}
        expected_location = 25
        result = update_player_location(player, True)
        self.assertEqual(expected_location, result['location'])

    @patch('builtins.input', side_effect=['Y'])
    def test_update_player_location_accomplished_location_skips_two(self, _):
        player = {"time": 50, "GPA": 3.5, "social": 80, "location": 23}
        expected_location = 25
        result = update_player_location(player, True)
        self.assertEqual(expected_location, result['location'])

    @patch('builtins.input', side_effect=['N'])
    def test_update_player_location_accomplished_no_sleep(self, _):
        player = {"time": 50, "GPA": 3.5, "social": 80, "location": 24}
        expected_location = 24
        result = update_player_location(player, True)
        self.assertEqual(expected_location, result['location'])

    def test_update_player_location_not_accomplished(self):
        player = {"time": 50, "GPA": 3.5, "social": 80, "location": 24}
        expected_location = 24
        result = update_player_location(player, False)
        self.assertEqual(expected_location, result['location'])

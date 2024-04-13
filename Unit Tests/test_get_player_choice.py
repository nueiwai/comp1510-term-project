from unittest import TestCase
from unittest.mock import patch

from exam import get_player_choice


class TestGetPlayerChoice(TestCase):

    @patch('builtins.input', side_effect=['1', '2', 'e'])
    def test_get_player_choice_valid_input(self, mock_input):
        self.assertEqual(get_player_choice(["snippet 1", "snippet 2", "snippet 3"]), ['snippet 1', 'snippet 2'])

    @patch('builtins.input', side_effect=['5', 'e'])
    def test_get_player_choice_invalid_input(self, mock_input):
        self.assertEqual(get_player_choice(["snippet 1", "snippet 2", "snippet 3"]), [])

    @patch('builtins.input', side_effect=['5', '10', 'e'])
    def test_get_player_choice_more_than_one_invalid_input(self, mock_input):
        self.assertEqual(get_player_choice(["snippet 1", "snippet 2", "snippet 3"]), [])

    @patch('builtins.input', side_effect=['e'])
    def test_get_player_choice_execute_snippets_without_selection(self, mock_input):
        self.assertEqual(get_player_choice(["snippet 1", "snippet 2", "snippet 3"]), [])

    @patch('builtins.input', side_effect=['1', 'y', '2', 'e'])
    def test_get_player_choice_mix_order_of_valid_and_invalid_input(self, mock_input):
        self.assertEqual(get_player_choice(["snippet 1", "snippet 2", "snippet 3"]), ['snippet 1', 'snippet 2'])

from unittest import TestCase
from unittest.mock import patch
from player_attribute_adjustments import sick_event_adjustment


class TestSickEventAdjustments(TestCase):
    @patch('random.randint', return_value=1)
    def test_sick_event_adjustment_time_loss_1(self, _):
        player = {'time': 50, 'GPA': 3.5, 'social': 50}
        expected_player = {'time': 49, 'GPA': 3.3, 'social': 40}
        actual = sick_event_adjustment(player)
        expected = [expected_player, 1]
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=2)
    def test_sick_event_adjustment_time_loss_2(self, _):
        player = {'time': 50, 'GPA': 3.5, 'social': 50}
        expected_player = {'time': 48, 'GPA': 3.3, 'social': 40}
        actual = sick_event_adjustment(player)
        expected = [expected_player, 2]
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)
    def test_sick_event_adjustment_time_loss_3(self, _):
        player = {'time': 50, 'GPA': 3.5, 'social': 50}
        expected_player = {'time': 47, 'GPA': 3.3, 'social': 40}
        actual = sick_event_adjustment(player)
        expected = [expected_player, 3]
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=4)
    def test_sick_event_adjustment_time_loss_4(self, _):
        player = {'time': 50, 'GPA': 3.5, 'social': 50}
        expected_player = {'time': 46, 'GPA': 3.3, 'social': 40}
        actual = sick_event_adjustment(player)
        expected = [expected_player, 4]
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=5)
    def test_sick_event_adjustment_time_loss_5(self, _):
        player = {'time': 50, 'GPA': 3.5, 'social': 50}
        expected_player = {'time': 45, 'GPA': 3.3, 'social': 40}
        actual = sick_event_adjustment(player)
        expected = [expected_player, 5]
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=6)
    def test_sick_event_adjustment_time_loss_6(self, _):
        player = {'time': 50, 'GPA': 3.5, 'social': 50}
        expected_player = {'time': 44, 'GPA': 3.3, 'social': 40}
        actual = sick_event_adjustment(player)
        expected = [expected_player, 6]
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=7)
    def test_sick_event_adjustment_time_loss_7(self, _):
        player = {'time': 50, 'GPA': 3.5, 'social': 50}
        expected_player = {'time': 43, 'GPA': 3.3, 'social': 40}
        actual = sick_event_adjustment(player)
        expected = [expected_player, 7]
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=8)
    def test_sick_event_adjustment_time_loss_8(self, _):
        player = {'time': 50, 'GPA': 3.5, 'social': 50}
        expected_player = {'time': 42, 'GPA': 3.3, 'social': 40}
        actual = sick_event_adjustment(player)
        expected = [expected_player, 8]
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=9)
    def test_sick_event_adjustment_time_loss_9(self, _):
        player = {'time': 50, 'GPA': 3.5, 'social': 50}
        expected_player = {'time': 41, 'GPA': 3.3, 'social': 40}
        actual = sick_event_adjustment(player)
        expected = [expected_player, 9]
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=10)
    def test_sick_event_adjustment_time_loss_10(self, _):
        player = {'time': 50, 'GPA': 3.5, 'social': 50}
        expected_player = {'time': 40, 'GPA': 3.3, 'social': 40}
        actual = sick_event_adjustment(player)
        expected = [expected_player, 10]
        self.assertEqual(actual, expected)

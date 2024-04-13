from unittest import TestCase
from player_attribute_adjustments import social_event_adjustment


class TestSocialEventAdjustment(TestCase):
    def test_social_event_adjustment_normal_value(self):
        player = {"time": 150, "GPA": 3.6, "social": 30, "location": 6}
        expected = {"time": 140, "GPA": 3.52, "social": 40, "location": 7}
        actual = social_event_adjustment(player)
        self.assertEqual(actual, expected)

    def test_social_event_adjustment_time_already_at_minimum(self):
        player = {"time": 5, "GPA": 3.5, "social": 50, "location": 3}
        expected = {"time": 0, "GPA": 3.42, "social": 60, "location": 4}
        actual = social_event_adjustment(player)
        self.assertEqual(actual, expected)

    def test_social_event_adjustment_org_large_social_increase(self):
        player = {"time": 90, "GPA": 2.0, "social": 90, "location": 6}
        expected = {"time": 80, "GPA": 1.92, "social": 100, "location": 7}
        actual = social_event_adjustment(player)
        self.assertEqual(actual, expected)

    def test_social_event_adjustment_both_time_and_gpa_at_low(self):
        player = {"time": 10, "GPA": 0.1, "social": 0, "location": 6}
        expected = {"time": 0, "GPA": 0.02, "social": 10, "location": 7}
        actual = social_event_adjustment(player)
        self.assertEqual(actual, expected)

from unittest import TestCase
from player_attribute_adjustments import study_session_event_adjustment


class TestStudySessionEventAdjustment(TestCase):
    def test_study_session_event_adjustment_normal_conditions(self):
        player = {"time": 120, "GPA": 2.8, "social": 50, "location": 4}
        expected = {"time": 110, "GPA": 3.8, "social": 45, "location": 5}
        actual = study_session_event_adjustment(player)
        self.assertEqual(actual, expected)

    def test_study_session_event_adjustment_time_already_at_minimum(self):
        player = {"time": 0, "GPA": 2.8, "social": 50, "location": 4}
        expected = {"time": 0, "GPA": 3.8, "social": 45, "location": 5}
        actual = study_session_event_adjustment(player)
        self.assertEqual(actual, expected)

    def test_study_session_event_adjustment_social_already_at_minimum(self):
        player = {"time": 120, "GPA": 2.8, "social": 0, "location": 4}
        expected = {"time": 110, "GPA": 3.8, "social": 0, "location": 5}
        actual = study_session_event_adjustment(player)
        self.assertEqual(actual, expected)

    def test_study_session_event_adjustment_both_time_and_social_at_minimum(self):
        player = {"time": 0, "GPA": 2.8, "social": 0, "location": 4}
        expected = {"time": 0, "GPA": 3.8, "social": 0, "location": 5}
        actual = study_session_event_adjustment(player)
        self.assertEqual(actual, expected)

    def test_study_session_event_adjustment_minimum_social_limit(self):
        player = {"time": 120, "GPA": 2.8, "social": 5, "location": 4}
        expected = {"time": 110, "GPA": 3.8, "social": 0, "location": 5}
        actual = study_session_event_adjustment(player)
        self.assertEqual(actual, expected)

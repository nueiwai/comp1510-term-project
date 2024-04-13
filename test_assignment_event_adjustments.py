from unittest import TestCase
from player_attribute_adjustments import assignment_event_adjustment


class TestAssignmentEventAdjustment(TestCase):
    def test_assignment_event_time_and_gpa_adjustment(self):
        player = {"time": 100, "GPA": 3.5, "social": 50, "location": 3}
        expected = {"time": 95, "GPA": 3.55, "social": 50, "location": 3}
        result = assignment_event_adjustment(player)
        self.assertEqual(result, expected)
        self.assertEqual(result["location"], player["location"])

    def test_assignment_event_low_time(self):
        player = {"time": 2, "GPA": 3.5, "social": 50, "location": 3}
        expected = {"time": 0, "GPA": 3.55, "social": 50, "location": 3}
        result = assignment_event_adjustment(player)
        self.assertEqual(result, expected)

    def test_assignment_event_high_gpa(self):
        player = {"time": 100, "GPA": 3.98, "social": 50, "location": 3}
        expected = {"time": 95, "GPA": 4.0, "social": 50, "location": 3}
        result = assignment_event_adjustment(player)
        self.assertEqual(result, expected)

    def test_assignment_event_negative_gpa_change(self):
        player = {"time": 100, "GPA": 1.0, "social": 50, "location": 3}
        expected = {"time": 95, "GPA": 1.05, "social": 50, "location": 3}
        result = assignment_event_adjustment(player)
        self.assertEqual(result, expected)

    def test_assignment_event_minimum_gpa(self):
        player = {"time": 100, "GPA": 0.0, "social": 50, "location": 3}
        expected = {"time": 95, "GPA": 0.05, "social": 50, "location": 3}
        result = assignment_event_adjustment(player)
        self.assertEqual(result, expected)

    def test_assignment_event_time_already_at_minimum(self):
        player = {"time": 0, "GPA": 3.5, "social": 50, "location": 3}
        expected = {"time": 0, "GPA": 3.55, "social": 50, "location": 3}
        result = assignment_event_adjustment(player)
        self.assertEqual(result, expected)

    def test_assignment_event_gpa_already_at_maximum(self):
        player = {"time": 100, "GPA": 4.0, "social": 50, "location": 3}
        expected = {"time": 95, "GPA": 4.0, "social": 50, "location": 3}
        result = assignment_event_adjustment(player)
        self.assertEqual(result, expected)

    def test_assignment_event_no_time_for_assignment(self):
        player = {"time": 4, "GPA": 3.5, "social": 50, "location": 3}
        expected = {"time": 0, "GPA": 3.55, "social": 50, "location": 3}
        result = assignment_event_adjustment(player)
        self.assertEqual(result, expected)

# THis file doesn't run when I put into package

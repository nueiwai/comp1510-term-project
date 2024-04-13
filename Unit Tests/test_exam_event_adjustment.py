from unittest import TestCase
from player_attribute_adjustments import exam_event_adjustment


class TestExamEventAdjustment(TestCase):
    def test_exam_pass_gpa_increase(self):
        player = {"time": 200, "GPA": 3.0, "social": 50}
        state = True
        expected = {"time": 185, "GPA": 3.2, "social": 50}
        result = exam_event_adjustment(player, state)
        self.assertEqual(result, expected)

    def test_exam_fail_gpa_decrease(self):
        player = {"time": 200, "GPA": 3.0, "social": 50}
        state = False
        expected = {"time": 185, "GPA": 2.8, "social": 50}
        result = exam_event_adjustment(player, state)
        self.assertEqual(result, expected)

    def test_exam_pass_gpa_at_max(self):
        player = {"time": 200, "GPA": 4.0, "social": 50}
        state = True
        expected = {"time": 185, "GPA": 4.0, "social": 50}
        result = exam_event_adjustment(player, state)
        self.assertEqual(result, expected)

    def test_exam_fail_gpa_at_min(self):
        player = {"time": 200, "GPA": 0.0, "social": 50}
        state = False
        expected = {"time": 185, "GPA": 0.0, "social": 50}
        result = exam_event_adjustment(player, state)
        self.assertEqual(result, expected)

    def test_exam_pass_time_decrease(self):
        player = {"time": 20, "GPA": 3.0, "social": 50}
        state = True
        expected = {"time": 5, "GPA": 3.2, "social": 50}
        result = exam_event_adjustment(player, state)
        self.assertEqual(result, expected)

    def test_exam_fail_time_decrease(self):
        player = {"time": 20, "GPA": 3.0, "social": 50}
        state = False
        expected = {"time": 5, "GPA": 2.8, "social": 50}
        result = exam_event_adjustment(player, state)
        self.assertEqual(result, expected)

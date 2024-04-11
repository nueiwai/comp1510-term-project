from unittest import TestCase
from player_attribute_adjustments import adjust_gpa


class TestAdjustGPA(TestCase):
    def test_adjust_gpa_increase_to_max_gpa(self):
        expected = 4.0
        actual = adjust_gpa(3.95, 0.1)
        self.assertEqual(actual, expected)

    def test_adjust_gpa_decrease_within_range(self):
        expected = 2.2
        actual = adjust_gpa(2.5, -0.3)
        self.assertEqual(actual, expected)

    def test_adjust_gpa_increase_within_range(self):
        expected = 3.75
        actual = adjust_gpa(3.0, 0.75)
        self.assertEqual(actual, expected)

    def test_adjust_gpa_no_change(self):
        expected = 3.0
        actual = adjust_gpa(3.0, 0.0)
        self.assertEqual(actual, expected)

    def test_adjust_gpa_initial_max(self):
        expected = 4.0
        actual = adjust_gpa(4.0, 1.0)
        self.assertEqual(actual, expected)

    def test_adjust_gpa_initial_min(self):
        expected = 0.0
        actual = adjust_gpa(1.0, -1.0)
        self.assertEqual(actual, expected)

    def test_adjust_gpa_increase_beyond_max_gpa(self):
        expected = 4.0
        actual = adjust_gpa(3.9, 0.2)
        self.assertEqual(actual, expected)

    def test_adjust_gpa_decrease_below_min_gpa(self):
        expected = 0.0
        actual = adjust_gpa(0.5, -0.6)
        self.assertEqual(actual, expected)

from unittest import TestCase
from player_attribute_adjustments import adjust_time


class Test(TestCase):
    def test_adjust_time_decrease_below_minimum(self):
        expected = 0
        actual = adjust_time(5, -10)
        self.assertEqual(actual, expected)

    def test_adjust_time_increase(self):
        expected = 19
        actual = adjust_time(14, 5)
        self.assertEqual(actual, expected)

    def test_adjust_time_decrease_to_zero(self):
        expected = 0
        actual = adjust_time(1, -5)
        self.assertEqual(actual, expected)

    def test_adjust_time_increase_from_zero(self):
        expected = 5
        actual = adjust_time(0, 5)
        self.assertEqual(actual, expected)

    def test_adjust_time_no_change(self):
        expected = 8
        actual = adjust_time(8, 0)
        self.assertEqual(actual, expected)

    def test_adjust_time_decrease_within_range(self):
        expected = 4
        actual = adjust_time(9, -5)
        self.assertEqual(actual, expected)

    def test_adjust_time_initial_min(self):
        expected = 0
        actual = adjust_time(0, -1)
        self.assertEqual(actual, expected)

    def test_adjust_time_increase_large(self):
        expected = 100
        actual = adjust_time(50, 50)
        self.assertEqual(actual, expected)

    def test_adjust_time_decrease_large_to_zero(self):
        expected = 0
        actual = adjust_time(50, -100)
        self.assertEqual(actual, expected)

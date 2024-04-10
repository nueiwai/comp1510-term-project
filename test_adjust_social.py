from unittest import TestCase
from player_attribute_adjustments import adjust_social


class TestAdjustSocial(TestCase):
    def test_adjust_social_increase_within_range_limit_100(self):
        expected = 70
        actual = adjust_social(50, 20, 100)
        self.assertEqual(expected, actual)

    def test_adjust_social_decrease_within_range_limit_100(self):
        expected = 30
        actual = adjust_social(50, -20, 100)
        self.assertEqual(expected, actual)

    def test_adjust_social_decrease_beyond_min_social_limit_100(self):
        expected = 0
        actual = adjust_social(5, -10, 100)
        self.assertEqual(expected, actual)

    def test_adjust_social_increase_beyond_max_social_limit_100(self):
        expected = 100
        actual = adjust_social(95, 10, 100)
        self.assertEqual(expected, actual)

    def test_adjust_social_exact_to_0_limit_100(self):
        expected = 0
        actual = adjust_social(10, -10, 100)
        self.assertEqual(expected, actual)

    def test_adjust_social_exact_to_100_limit_100(self):
        expected = 100
        actual = adjust_social(90, 10, 100)
        self.assertEqual(expected, actual)

    def test_adjust_social_no_change_limit_100(self):
        expected = 50
        actual = adjust_social(50, 0, 100)
        self.assertEqual(expected, actual)

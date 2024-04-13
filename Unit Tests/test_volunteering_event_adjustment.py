from unittest import TestCase
from player_attribute_adjustments import volunteering_event_adjustment


class TestVolunteeringEventAdjustment(TestCase):
    def test_volunteering_event_adjustment_standard(self):
        player = {'time': 200, 'GPA': 2.5, 'social': 10}
        expected = {'time': 180, 'GPA': 2.55, 'social': 40}
        actual = volunteering_event_adjustment(player)
        self.assertEqual(actual, expected)

    def test_volunteering_event_adjustment_near_gpa_cap(self):
        player = {'time': 180, 'GPA': 3.95, 'social': 5}
        expected = {'time': 160, 'GPA': 4.0, 'social': 35}
        actual = volunteering_event_adjustment(player)
        self.assertEqual(actual, expected)

    def test_volunteering_event_adjustment_low_resources(self):
        player = {'time': 25, 'GPA': 1.0, 'social': 5}
        expected = {'time': 5, 'GPA': 1.05, 'social': 35}
        actual = volunteering_event_adjustment(player)
        self.assertEqual(actual, expected)

    def test_volunteering_event_adjustment_time_boundary(self):
        player = {'time': 20, 'GPA': 2.0, 'social': 10}
        expected = {'time': 0, 'GPA': 2.05, 'social': 40}
        actual = volunteering_event_adjustment(player)
        self.assertEqual(actual, expected)

    def test_volunteering_event_adjustment_negative_time(self):
        player = {'time': 10, 'GPA': 3.0, 'social': 20}
        expected = {'time': 0, 'GPA': 3.05, 'social': 50}
        actual = volunteering_event_adjustment(player)
        self.assertEqual(actual, expected)

    def test_volunteering_event_adjustment_high_social_increase(self):
        player = {'time': 100, 'GPA': 2.2, 'social': 980}
        expected = {'time': 80, 'GPA': 2.25, 'social': 1010}
        actual = volunteering_event_adjustment(player)
        self.assertEqual(actual, expected)

    def test_volunteering_event_adjustment_all_0_values(self):
        player = {'time': 0, 'GPA': 0.0, 'social': 0}
        expected = {'time': 0, 'GPA': 0.05, 'social': 30}
        actual = volunteering_event_adjustment(player)
        self.assertEqual(actual, expected)

    def test_volunteering_event_adjustment_maximum_gpa(self):
        player = {'time': 50, 'GPA': 3.99, 'social': 25}
        expected = {'time': 30, 'GPA': 4.0, 'social': 55}
        actual = volunteering_event_adjustment(player)
        self.assertEqual(actual, expected)

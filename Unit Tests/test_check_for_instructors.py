from unittest import TestCase
from unittest.mock import patch

import character


class TestCheckForInstructors(TestCase):
    @patch('random.random', return_value=0.2)
    def test_check_for_instructors_just_under_point_two_five(self, mock_random):
        instructor_encountered = character.check_for_instructors()
        self.assertEqual(instructor_encountered, True)

    @patch('random.random', return_value=0.3)
    def test_check_for_instructors_just_above_point_two_five(self, mock_random):
        instructor_encountered = character.check_for_instructors()
        self.assertEqual(instructor_encountered, False)

    @patch('random.random', return_value=0.25)
    def test_check_for_instructors_exactly_at_point_two_five(self, mock_random):
        instructor_encountered = character.check_for_instructors()
        self.assertEqual(instructor_encountered, True)

    @patch('random.random', return_value=0.5)
    def test_check_for_instructors_somewhere_in_the_middle(self, mock_random):
        instructor_encountered = character.check_for_instructors()
        self.assertEqual(instructor_encountered, False)

    @patch('random.random', return_value=0.9999)
    def test_check_for_instructors_just_under_upper_bound(self, mock_random):
        instructor_encountered = character.check_for_instructors()
        self.assertEqual(instructor_encountered, False)

    @patch('random.random', return_value=1)
    def test_check_for_instructors_exactly_at_upper_bound(self, mock_random):
        instructor_encountered = character.check_for_instructors()
        self.assertEqual(instructor_encountered, False)

    @patch('random.random', return_value=0.0001)
    def test_check_for_instructors_just_above_lower_bound(self, mock_random):
        instructor_encountered = character.check_for_instructors()
        self.assertEqual(instructor_encountered, True)

    @patch('random.random', return_value=0.0)
    def test_check_for_instructors_exactly_at_lower_bound(self, mock_random):
        instructor_encountered = character.check_for_instructors()
        self.assertEqual(instructor_encountered, True)

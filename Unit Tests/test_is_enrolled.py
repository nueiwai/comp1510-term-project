from unittest import TestCase

import character


class TestIsEnrolled(TestCase):
    def test_is_enrolled_student_is_enrolled(self):
        test_character = {'time': 50, 'GPA': 3.5, 'social': 50, 'location': 26}
        result = character.is_enrolled(test_character)
        self.assertEqual(result, True)

    def test_is_enrolled_student_is_not_enrolled(self):
        test_character = {'time': 50, 'GPA': 1.0, 'social': 50, 'location': 26}
        result = character.is_enrolled(test_character)
        self.assertEqual(result, False)

    def test_is_enrolled_student_is_enrolled_at_different_location(self):
        test_character = {'time': 50, 'GPA': 3.5, 'social': 50, 'location': 51}
        result = character.is_enrolled(test_character)
        self.assertEqual(result, True)

    def test_is_enrolled_student_is_not_enrolled_at_different_location(self):
        test_character = {'time': 50, 'GPA': 1.0, 'social': 50, 'location': 51}
        result = character.is_enrolled(test_character)
        self.assertEqual(result, False)

    def test_is_enrolled_student_is_enrolled_at_end_location(self):
        test_character = {'time': 50, 'GPA': 3.5, 'social': 50, 'location': 100}
        result = character.is_enrolled(test_character)
        self.assertEqual(result, True)

    def test_is_enrolled_student_is_not_enrolled_at_end_location(self):
        test_character = {'time': 50, 'GPA': 1.0, 'social': 50, 'location': 100}
        result = character.is_enrolled(test_character)
        self.assertEqual(result, False)

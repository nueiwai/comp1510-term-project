from unittest import TestCase

import character


class TestMakeCharacterEachTermStart(TestCase):

    def test_make_character_each_term_start_term_two_start(self):
        test_character = {'time': 50, 'GPA': 3.8, 'social': 50, 'location': 26}
        expected_result = {'time': 120, 'GPA': 3.5, 'social': 60, 'location': 26}
        result = character.make_character_each_term_start(test_character)
        self.assertEqual(result, expected_result)

    def test_make_character_each_term_start_term_three_start(self):
        test_character = {'time': 50, 'GPA': 3.8, 'social': 50, 'location': 51}
        expected_result = {'time': 150, 'GPA': 3.5, 'social': 70, 'location': 51}
        result = character.make_character_each_term_start(test_character)
        self.assertEqual(result, expected_result)

    def test_make_character_each_term_start_term_four_start(self):
        test_character = {'time': 50, 'GPA': 3.8, 'social': 50, 'location': 76}
        expected_result = {'time': 180, 'GPA': 3.5, 'social': 80, 'location': 76}
        result = character.make_character_each_term_start(test_character)
        self.assertEqual(result, expected_result)

    def test_make_character_each_term_start_middle_of_term(self):
        test_character = {'time': 50, 'GPA': 3.8, 'social': 50, 'location': 40}
        expected_result = {'time': 50, 'GPA': 3.8, 'social': 50, 'location': 40}
        result = character.make_character_each_term_start(test_character)
        self.assertEqual(result, expected_result)

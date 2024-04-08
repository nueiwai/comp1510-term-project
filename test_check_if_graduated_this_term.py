from unittest import TestCase

import character


class TestCheckIfGraduatedThisTerm(TestCase):
    def test_check_if_graduated_this_term_graduated_term(self):
        test_character = {'time': 50, 'GPA': 3.5, 'social': 50, 'location': 26}
        term_graduated = character.check_if_graduated_this_term(test_character)
        self.assertEqual(term_graduated, True)

    def test_check_if_graduated_this_term_did_not_graduate_term(self):
        test_character = {'time': 50, 'GPA': 1.0, 'social': 50, 'location': 26}
        term_graduated = character.check_if_graduated_this_term(test_character)
        self.assertEqual(term_graduated, False)

    def test_check_if_graduated_this_term_graduated_term_with_maximum_gpa(self):
        test_character = {'time': 50, 'GPA': 4.0, 'social': 50, 'location': 26}
        term_graduated = character.check_if_graduated_this_term(test_character)
        self.assertEqual(term_graduated, True)

    def test_check_if_graduated_this_term_did_not_graduate_term_with_minimum_gpa(self):
        test_character = {'time': 50, 'GPA': 0.0, 'social': 50, 'location': 26}
        term_graduated = character.check_if_graduated_this_term(test_character)
        self.assertEqual(term_graduated, False)

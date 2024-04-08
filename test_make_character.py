from unittest import TestCase

import character


class TestMakeCharacter(TestCase):
    def test_make_character_time_attribute_exist_and_is_one_hundred(self):
        test_character = character.make_character()
        self.assertEqual(test_character.get('time', -1), 100)

    def test_make_character_gpa_attribute_exist_and_is_three_point_five(self):
        test_character = character.make_character()
        self.assertEqual(test_character.get('GPA', -1), 3.5)

    def test_make_character_social_attribute_exist_and_is_fifty(self):
        test_character = character.make_character()
        self.assertEqual(test_character.get('social', -1), 50)

    def test_make_character_location_attribute_exist_and_is_one(self):
        test_character = character.make_character()
        self.assertEqual(test_character.get('location', -1), 1)

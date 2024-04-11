from unittest import TestCase
from mini_games import roman_numeral_converter


class TestRomanNumeralConverter(TestCase):
    def test_roman_numeral_converter_min(self):
        expected = "I"
        actual = roman_numeral_converter(1)
        self.assertEqual(expected, actual)

    def test_roman_numeral_converter_max(self):
        expected = "MMMMM"
        actual = roman_numeral_converter(5000)
        self.assertEqual(expected, actual)

    def test_roman_numeral_converter_4(self):
        expected = "IV"
        actual = roman_numeral_converter(4)
        self.assertEqual(expected, actual)

    def test_roman_numeral_converter_9(self):
        expected = "IX"
        actual = roman_numeral_converter(9)
        self.assertEqual(expected, actual)

    def test_roman_numeral_converter_40(self):
        expected = "XL"
        actual = roman_numeral_converter(40)
        self.assertEqual(expected, actual)

    def test_roman_numeral_converter_90(self):
        expected = "XC"
        actual = roman_numeral_converter(90)
        self.assertEqual(expected, actual)

    def test_roman_numeral_converter_400(self):
        expected = "CD"
        actual = roman_numeral_converter(400)
        self.assertEqual(expected, actual)

    def test_roman_numeral_converter_900(self):
        expected = "CM"
        actual = roman_numeral_converter(900)
        self.assertEqual(expected, actual)

    def test_roman_numeral_converter_3999(self):
        expected = "MMMCMXCIX"
        actual = roman_numeral_converter(3999)
        self.assertEqual(expected, actual)

    def test_roman_numeral_converter_2421(self):
        expected = "MMCDXXI"
        actual = roman_numeral_converter(2421)
        self.assertEqual(expected, actual)

    def test_roman_numeral_converter_1023(self):
        expected = "MXXIII"
        actual = roman_numeral_converter(1023)
        self.assertEqual(expected, actual)

    def test_roman_numeral_converter_580(self):
        expected = "DLXXX"
        actual = roman_numeral_converter(580)
        self.assertEqual(expected, actual)

    def test_roman_numeral_converter_123(self):
        expected = "CXXIII"
        actual = roman_numeral_converter(123)
        self.assertEqual(expected, actual)

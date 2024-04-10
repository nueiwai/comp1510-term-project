from unittest import TestCase
from mini_games import decimal_to_base


class TestDecimalToBase(TestCase):
    def test_decimal_1_to_base_2(self):
        expected = "1"
        actual = decimal_to_base(1, 2)
        self.assertEqual(expected, actual)

    def test_decimal_1_to_base_5(self):
        expected = "1"
        actual = decimal_to_base(1, 5)
        self.assertEqual(expected, actual)

    def test_decimal_1_to_base_9(self):
        expected = "1"
        actual = decimal_to_base(1, 9)
        self.assertEqual(expected, actual)

    def test_decimal_10000_to_base_2(self):
        expected = "10011100010000"
        actual = decimal_to_base(10000, 2)
        self.assertEqual(expected, actual)

    def test_decimal_10000_to_base_5(self):
        expected = "310000"
        actual = decimal_to_base(10000, 5)
        self.assertEqual(expected, actual)

    def test_decimal_10000_to_base_9(self):
        expected = "14641"
        actual = decimal_to_base(10000, 9)
        self.assertEqual(expected, actual)

    def test_decimal_77_to_base_2(self):
        expected = "1001101"
        actual = decimal_to_base(77, 2)
        self.assertEqual(expected, actual)

    def test_decimal_77_to_base_3(self):
        expected = "2212"
        actual = decimal_to_base(77, 3)
        self.assertEqual(expected, actual)

    def test_decimal_77_to_base_4(self):
        expected = "1031"
        actual = decimal_to_base(77, 4)
        self.assertEqual(expected, actual)

    def test_decimal_77_to_base_5(self):
        expected = "302"
        actual = decimal_to_base(77, 5)
        self.assertEqual(expected, actual)

    def test_decimal_77_to_base_6(self):
        expected = "205"
        actual = decimal_to_base(77, 6)
        self.assertEqual(expected, actual)

    def test_decimal_77_to_base_7(self):
        expected = "140"
        actual = decimal_to_base(77, 7)
        self.assertEqual(expected, actual)

    def test_decimal_77_to_base_8(self):
        expected = "115"
        actual = decimal_to_base(77, 8)
        self.assertEqual(expected, actual)

    def test_decimal_77_to_base_9(self):
        expected = "85"
        actual = decimal_to_base(77, 9)
        self.assertEqual(expected, actual)

    def test_decimal_zero_to_base_2(self):
        expected = "0"
        actual = decimal_to_base(0, 2)
        self.assertEqual(expected, actual)

    def test_decimal_zero_to_base_5(self):
        expected = "0"
        actual = decimal_to_base(0, 5)
        self.assertEqual(expected, actual)

    def test_decimal_zero_to_base_9(self):
        expected = "0"
        actual = decimal_to_base(0, 9)
        self.assertEqual(expected, actual)

from unittest import TestCase
from rn_to_ints import roman_nums


class TestRomanNumeralsToInts(TestCase):
    def test_roman_nums(self):
        self.assertEqual(roman_nums('IV'), 4)
        self.assertEqual(roman_nums('XIX'), 19)
        self.assertEqual(roman_nums('MMCM'), 2900)

    def test_empty_string(self):
        self.assertEqual(roman_nums(''), 0)

    def test_not_roman_numeral(self):
        self.assertEqual(roman_nums('2'), '')
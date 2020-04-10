from unittest import TestCase

from pyquiz.leetcode.RomanToInteger import RomanToInteger


class TestRomanToInteger(TestCase):
    alg = RomanToInteger()

    def test_one_to_10(self):
        self.assertEqual(1, self.alg.roman_to_int('I'))
        self.assertEqual(2, self.alg.roman_to_int('II'))
        self.assertEqual(3, self.alg.roman_to_int('III'))
        self.assertEqual(4, self.alg.roman_to_int('IV'))
        self.assertEqual(5, self.alg.roman_to_int('V'))
        self.assertEqual(6, self.alg.roman_to_int('VI'))
        self.assertEqual(7, self.alg.roman_to_int('VII'))
        self.assertEqual(8, self.alg.roman_to_int('VIII'))
        self.assertEqual(9, self.alg.roman_to_int('IX'))
        self.assertEqual(10, self.alg.roman_to_int('X'))

    def test_complex(self):
        self.assertEqual(409, self.alg.roman_to_int('XICD')) # 10 -1 -100 + 500
        self.assertEqual(390, self.alg.roman_to_int('XCD'))


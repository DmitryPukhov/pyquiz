from unittest import TestCase

from pyquiz.leetcode.FactorialTrailingZeroes import FactorialTrailingZeroes


class TestFactorialTrailingZeroes(TestCase):
    alg = FactorialTrailingZeroes()

    def test_trailing_zeroes(self):

        self.assertEqual(1, self.alg.trailingZeroes(5))
        self.assertEqual(1, self.alg.trailingZeroes(6))
        self.assertEqual(2, self.alg.trailingZeroes(10))
        self.assertEqual(2, self.alg.trailingZeroes(14))
        self.assertEqual(3, self.alg.trailingZeroes(15))

    def test_trailing_zeroes__negative_val(self):
        self.assertEqual(0, self.alg.trailingZeroes(-1))
        self.assertEqual(-1, self.alg.trailingZeroes(-5))
        self.assertEqual(-1, self.alg.trailingZeroes(-6))

    def test_trailing_zeroes__zero(self):
        self.assertEqual(0, self.alg.trailingZeroes(0))
        self.assertEqual(0, self.alg.trailingZeroes(1))
        self.assertEqual(0, self.alg.trailingZeroes(4))

from unittest import TestCase

from pyquiz.leetcode.SelfDividingNumbers import SelfDividingNumbers


class TestSelfDividingNumbers(TestCase):
    alg = SelfDividingNumbers()

    def test_self_dividing_numbers(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22], self.alg.selfDividingNumbers(1, 22))
        self.assertEqual([1], self.alg.selfDividingNumbers(1, 1))
        self.assertEqual([12], self.alg.selfDividingNumbers(12, 14))
        self.assertEqual([15], self.alg.selfDividingNumbers(14, 15))
        self.assertEqual([], self.alg.selfDividingNumbers(3, 2))

    def test_is_self_div(self):
        self.assertTrue(self.alg.is_self_div(135))
        self.assertFalse(self.alg.is_self_div(14))

from unittest import TestCase

from pyquiz.leetcode.Maximum69Number import Maxumum69Number


class TestMaxumum69Number(TestCase):
    alg = Maxumum69Number()

    def test_maximum_69_number(self):
        self.assertEqual(9969, self.alg.maximum_69_number(9669))
        self.assertEqual(9, self.alg.maximum_69_number(9))
        self.assertEqual(9, self.alg.maximum_69_number(6))
        self.assertEqual(999, self.alg.maximum_69_number(999))
        self.assertEqual(9, self.alg.maximum_69_number(6))
        self.assertEqual(96, self.alg.maximum_69_number(66))

    def test_digit_of(self):
        self.assertEqual(3, self.alg.digit_of(123, 1))
        self.assertEqual(2, self.alg.digit_of(123, 2))
        self.assertEqual(1, self.alg.digit_of(123, 3))
        self.assertEqual(0, self.alg.digit_of(123, 4))

    def test_with_digit(self):
        self.assertEqual(124, self.alg.with_digit(123, 4, 1))
        self.assertEqual(143, self.alg.with_digit(123, 4, 2))
        self.assertEqual(423, self.alg.with_digit(423, 4, 3))

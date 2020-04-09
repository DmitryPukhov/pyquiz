from unittest import TestCase

from test.leetcode.SqrtX import SqrtX


class TestSqrtX(TestCase):
    def test_my_sqrt__presize_val(self):
        alg = SqrtX()
        self.assertEqual(2, alg.mySqrt(4))
        self.assertEqual(4, alg.mySqrt(16))

    def test_my_sqrt__result_with_decimal_part(self):
        alg = SqrtX()
        self.assertEqual(2, alg.mySqrt(8))
        self.assertEqual(3, alg.mySqrt(9))
        self.assertEqual(3, alg.mySqrt(10))
        self.assertEqual(3, alg.mySqrt(11))
        self.assertEqual(3, alg.mySqrt(12))
        self.assertEqual(3, alg.mySqrt(13))
        self.assertEqual(3, alg.mySqrt(14))
        self.assertEqual(3, alg.mySqrt(15))

    def test_my_sqrt__corner_cases(self):
        alg = SqrtX()
        self.assertEqual(0, alg.mySqrt(0))
        self.assertEqual(1, alg.mySqrt(1))
        self.assertEqual(1, alg.mySqrt(2))
        self.assertEqual(1, alg.mySqrt(3))

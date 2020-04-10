from unittest import TestCase

from pyquiz.leetcode.SingleNumber import SingleNumber


class TestSingleNumber(TestCase):
    alg = SingleNumber()

    def test_solve(self):
        self.assertEqual(1, self.alg.solve([2, 2, 1]))

    def test_solve__with_even_arr__should_return_0(self):
        self.assertEqual(0, self.alg.solve([1,1]))

    # def test_solve__with_neg(self):
    #     self.assertEqual(-2, self.alg.solve([-1,-1, -2]))

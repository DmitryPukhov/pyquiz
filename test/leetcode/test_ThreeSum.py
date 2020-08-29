from unittest import TestCase

from pyquiz.leetcode.ThreeSum import ThreeSum


class TestThreeSum(TestCase):
    def test_three_sum_empty(self):
        res = ThreeSum().threeSum([])
        self.assertEqual([],res)

    def test_three_sum(self):
        res = ThreeSum().threeSum([-1, 0, 1, 2, -1, 4])
        self.assertEqual([
            [-1, -1, 2],
            [-1, 0, 1]
        ], res)

    def test_three_sum_2(self):
        res = ThreeSum().threeSum([-1, -1, 0, 1, 1, 2, -1, 4, 5, -5])
        self.assertEqual([
            [-5, 0, 5],
            [-5, 1, 4],
            [-1, -1, 2],
            [-1, 0, 1]
        ], res)

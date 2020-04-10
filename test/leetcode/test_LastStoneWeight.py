from unittest import TestCase
from pyquiz.leetcode.LastStoneWeight import LastStoneWeight


class TestLastStoneWeight(TestCase):

    def test_solution(self):
        alg = LastStoneWeight()
        self.assertEqual(1, alg.solve([2, 7, 4, 1, 8, 1]))

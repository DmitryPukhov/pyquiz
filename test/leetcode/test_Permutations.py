from unittest import TestCase

from pyquiz.leetcode.Permutations import Permutations


class TestPermutations(TestCase):
    def test_permute(self):
        res = Permutations().permute([1, 2, 3])
        self.assertEqual([
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ], res)

    def test_permite_1(self):
        self.assertEqual([[1]], Permutations().permute([1]))

    def test_permite_empty(self):
        self.assertEqual([], Permutations().permute([]))

    def test_permite_none(self):
        self.assertEqual([], Permutations().permute([]))

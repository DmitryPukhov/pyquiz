from unittest import TestCase
from pyquiz.leetcode.MinMoves import Solution


class TestSolution(TestCase):
    def test_min_moves_example1(self):
        """
        Example:
        Input:
        [1,2,3]

        Output:  3
        1,2,3 -> 2,3,3 -> 3,4,3 -> 4,4,4
        """
        self.assertEqual(3, Solution().minMoves([1, 2, 3]))

    def test_min_moves_12(self):
        self.assertEqual(1, Solution().minMoves([1, 2]))

    def test_min_moves_1(self):
        self.assertEqual(0, Solution().minMoves([1]))

    def test_min_moves_1_2147483647(self):
        out = Solution().minMoves([1, 2147483647])

    def test_min_moves_1_0_1(self):
        self.assertEqual(2, Solution().minMoves([1, 0, 1]))

    def test_min_moves_1_2_neg2(self):
        self.assertEqual(5, Solution().minMoves([1, 2, -1]))

    def test_min_moves_1_neg1(self):
        self.assertEqual(2, Solution().minMoves([1, -1]))
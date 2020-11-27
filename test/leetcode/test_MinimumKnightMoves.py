from unittest import TestCase
from pyquiz.leetcode.MinimumKnightMoves import MinimumKnightMoves


class TestMinKnightMoves(TestCase):
    def test_min_knight_moves_example1(self):
        """
        Example 1:
        Input: x = 2, y = 1
        Output: 1
        Explanation: [0, 0] → [2, 1]
        """
        res = MinimumKnightMoves().minKnightMoves(2, 1)
        self.assertEqual(1, res)

    def test_min_knight_moves_example2(self):
        """
        Example 2:
        Input: x = 5, y = 5
        Output: 4
        Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]`
        """
        res = MinimumKnightMoves().minKnightMoves(5, 5)
        self.assertEqual(4, res)

    def test_min_knight_moves_0_0(self):
        res = MinimumKnightMoves().minKnightMoves(0, 0)
        self.assertEqual(0, res)

    def test_min_knight_moves_2_1(self):
        res = MinimumKnightMoves().minKnightMoves(2, 1)
        self.assertEqual(1, res)

    def test_min_knight_moves_2_neg1(self):
        res = MinimumKnightMoves().minKnightMoves(2, -1)
        self.assertEqual(1, res)

    def test_min_knight_moves_neg2_1(self):
        res = MinimumKnightMoves().minKnightMoves(-2, 1)
        self.assertEqual(1, res)

    def test_min_knight_moves_neg2_neg1(self):
        res = MinimumKnightMoves().minKnightMoves(-2, -1)
        self.assertEqual(1, res)

    def test_min_knight_moves_neg1_neg2(self):
        res = MinimumKnightMoves().minKnightMoves(2, -1)
        self.assertEqual(1, res)

    def test_min_knight_moves_1_2(self):
        res = MinimumKnightMoves().minKnightMoves(1, 2)
        self.assertEqual(1, res)

    def test_min_knight_moves_1_3(self):
        res = MinimumKnightMoves().minKnightMoves(1, 3)
        self.assertEqual(2, res)

    def test_min_knight_moves_neg1_3(self):
        res = MinimumKnightMoves().minKnightMoves(-1, 3)
        self.assertEqual(2, res)

    def test_min_knight_moves_1_neg3(self):
        res = MinimumKnightMoves().minKnightMoves(1, -3)
        self.assertEqual(2, res)

    def test_min_knight_moves_150_150(self):
        res = MinimumKnightMoves().minKnightMoves(150, 150)
        self.assertEqual(100, res)

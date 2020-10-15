from unittest import TestCase

from pyquiz.leetcode.MaximalSquare import MaximalSquare


class TestMaximalSquare(TestCase):
    def test_maximal_square_example1(self):
        """
        Example:
        Input:
        1 0 1 0 0
        1 0 1 1 1
        1 1 1 1 1
        1 0 0 1 0

        Output: 4
        """
        matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                  ["1", "0", "0", "1", "0"]]
        self.assertEqual(4, MaximalSquare().maximalSquare(matrix))

    def test_maximal_square__00_00(self):
        matrix = [["0", "0"],
                  ["0", "0"]]
        self.assertEqual(0, MaximalSquare().maximalSquare(matrix))

    def test_maximal_square_11_11(self):
        matrix = [["1", "1"],
                  ["1", "1"]]
        self.assertEqual(4, MaximalSquare().maximalSquare(matrix))

    def test_maximal_square_00_01(self):
        matrix = [["0", "0"],
                  ["0", "1"]]
        self.assertEqual(1, MaximalSquare().maximalSquare(matrix))

    def test_maximal_square_10_00(self):
        matrix = [["1", "0"],
                  ["0", "0"]]
        self.assertEqual(1, MaximalSquare().maximalSquare(matrix))

    def test_maximal_square_0(self):
        matrix = [["0"]]
        self.assertEqual(0, MaximalSquare().maximalSquare(matrix))

    def test_maximal_square_1(self):
        matrix = [["1"]]
        self.assertEqual(1, MaximalSquare().maximalSquare(matrix))

    def test_maximal_square__11_00(self):
        matrix = [["1", "1"], ["0", "0"]]
        self.assertEqual(1, MaximalSquare().maximalSquare(matrix))

    def test_maximal_square__10_01(self):
        matrix = [["1", "0"], ["0", "1"]]
        self.assertEqual(1, MaximalSquare().maximalSquare(matrix))

    def test_maximal_square__0_1(self):
        matrix = [["0"], ["1"]]
        self.assertEqual(1, MaximalSquare().maximalSquare(matrix))

    def test_maximal_square__1_0(self):
        matrix = [["1"], ["0"]]
        self.assertEqual(1, MaximalSquare().maximalSquare(matrix))

    def test_maximal_square__badcase(self):
        matrix = [["1", "0", "1", "0"],
                  ["1", "0", "1", "1"],
                  ["1", "0", "1", "1"],
                  ["1", "1", "1", "1"]]
        self.assertEqual(4, MaximalSquare().maximalSquare(matrix))

from typing import List
from unittest import TestCase
from pyquiz.leetcode.LeftmostColumnWithAtLeastAOne import LeftmostColumnWithAtLeastAOne


class TestLeftmostColumnWithAtLeastAOne(TestCase):
    class BinaryMatrix(object):
        """
        Binary matrix implementation for test. Uses given list as a matrix
        """

        def __init__(self, m: List[List[int]]):
            self._m = m
            self._width = len(m[0]) if m and m[0] else 0
            self._height = len(m)

        def get(self, row: int, col: int) -> int:
            return self._m[row][col]

        def dimensions(self) -> List[int]:
            return [self._height, self._width]

    def test_left_most_column_with_one_example1(self):
        """
        Example 1:
        Input: mat = [[0,0],[1,1]]
        Output: 0
        """
        m = self.BinaryMatrix([[0, 0], [1, 1]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(res, 0)

    def test_left_most_column_with_one_example2(self):
        """
        Example 2:
        Input: mat = [[0,0],[0,1]]
        Output: 1
        """
        m = self.BinaryMatrix([[0, 0], [0, 1]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(res, 1)

    def test_left_most_column_with_one_example3(self):
        """
        Example 3:
        Input: mat = [[0,0],[0,0]]
        Output: -1
        """
        m = self.BinaryMatrix([[0, 0], [0, 0]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(res, -1)

    def test_left_most_column_with_one_example4(self):
        """
        Example 4:
        Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
        Output: 1
        """
        m = self.BinaryMatrix([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(1, res)

    def test_left_most_column_with_one_0011_0000_0001(self):
        m = self.BinaryMatrix([[0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 1]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(2, res)

    def test_left_most_column_with_one_0(self):
        m = self.BinaryMatrix([[0]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(-1, res)

    def test_left_most_column_with_one_1(self):
        m = self.BinaryMatrix([[1]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(0, res)

    def test_left_most_column_with_one_0_0(self):
        m = self.BinaryMatrix([[0], [0]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(-1, res)

    def test_left_most_column_with_one_1_1(self):
        m = self.BinaryMatrix([[1], [1]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(0, res)

    def test_left_most_column_with_one_00(self):
        m = self.BinaryMatrix([[0, 0]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(-1, res)

    def test_left_most_column_with_one_11(self):
        m = self.BinaryMatrix([[1, 1]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(0, res)

    def test_left_most_column_with_one_001(self):
        m = self.BinaryMatrix([[0, 0, 1]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(2, res)

    def test_left_most_column_with_one_011(self):
        m = self.BinaryMatrix([[0, 1, 1]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(1, res)

    def test_left_most_column_with_one_1010(self):
        m = self.BinaryMatrix([[1, 1, 1]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(0, res)

    def test_left_most_column_with_one_001_011(self):
        m = self.BinaryMatrix([[0, 0, 1], [0, 1, 1]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(1, res)

    def test_left_most_column_with_one_001_111_011(self):
        m = self.BinaryMatrix([[0, 0, 1], [1, 1, 1], [0, 1, 1]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(0, res)

    def test_left_most_column_with_one_111_001_011(self):
        m = self.BinaryMatrix([[1, 1, 1],[0, 0, 1],  [0, 1, 1]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(0, res)

    def test_left_most_column_with_one_001_011_111(self):
        m = self.BinaryMatrix([[0, 0, 1],  [0, 1, 1],[1, 1, 1]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(0, res)

    def test_left_most_column_with_one_001_011_001(self):
        m = self.BinaryMatrix([[0, 0, 1],  [0, 1, 1],[0, 0, 1]])
        res = LeftmostColumnWithAtLeastAOne().leftMostColumnWithOne(m)
        self.assertEqual(1, res)

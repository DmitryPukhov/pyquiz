from unittest import TestCase

from pyquiz.leetcode.MaximalRectangle import MaximalRectangle


class TestMaximalRectangle(TestCase):
    def test_maximal_rectangle_example1(self):
        """
        Example 1:
        Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        Output: 6
        Explanation: The maximal rectangle is shown in the above picture.
        """
        matrix = [["1", "0", "1", "0", "0"],
                  ["1", "0", "1", "1", "1"],
                  ["1", "1", "1", "1", "1"],
                  ["1", "0", "0", "1", "0"]]
        out = MaximalRectangle().maximalRectangle(matrix)
        self.assertEqual(6, out)

    def test_maximal_rectangle_example2(self):
        """
        Example 2:
        Input: matrix = []
        Output: 0
        """
        out = MaximalRectangle().maximalRectangle([])
        self.assertEqual(0, out)

    def test_maximal_rectangle_example3(self):
        """
        Example 3:
        Input: matrix = [["0"]]
        Output: 0
        """
        matrix = [["0"]]
        out = MaximalRectangle().maximalRectangle(matrix)
        self.assertEqual(0, out)

    def test_maximal_rectangle_example4(self):
        """
        Example 4:
        Input: matrix = [["1"]]
        Output: 1
        """
        matrix = [["1"]]
        out = MaximalRectangle().maximalRectangle(matrix)
        self.assertEqual(1, out)

    def test_maximal_rectangle_example5(self):
        """
        Example 5:
        Input: matrix = [["0","0"]]
        Output: 0
        """
        matrix = [["0", "0"]]
        out = MaximalRectangle().maximalRectangle(matrix)
        self.assertEqual(0, out)

    def test_maximal_rectangle_example011_111(self):
        matrix = [["0", "0","1"],["1","1","1"]]
        out = MaximalRectangle().maximalRectangle(matrix)
        self.assertEqual(3, out)

    def test_maximal_rectangle_example100_111(self):
        matrix = [["1", "0","0"],["1","1","1"]]
        out = MaximalRectangle().maximalRectangle(matrix)
        self.assertEqual(3, out)

    def test_maximal_rectangle_01(self):
        matrix = [["0", "1"]]
        out = MaximalRectangle().maximalRectangle(matrix)
        self.assertEqual(1, out)

    def test_maximal_rectangle_10(self):
        matrix = [["1", "0"]]
        out = MaximalRectangle().maximalRectangle(matrix)
        self.assertEqual(1, out)

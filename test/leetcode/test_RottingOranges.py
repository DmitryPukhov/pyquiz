from unittest import TestCase

from pyquiz.leetcode.RottingOranges import RottingOranges


class TestRottingOranges(TestCase):
    def test_oranges_rotting__example1(self):
        """
        Example 1:
        Input: [[2,1,1],[1,1,0],[0,1,1]]
        Output: 4
        """
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        output = 4
        self.assertEqual(output, RottingOranges().orangesRotting(grid))

    def test_oranges_rotting__example2(self):
        """
        Example 2:
        Input: [[2,1,1],[0,1,1],[1,0,1]]
        Output: -1
        Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
        """
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        output = -1
        self.assertEqual(output, RottingOranges().orangesRotting(grid))

    def test_oranges_rotting__example3(self):
        """
        Example 3:
        Input: [[0,2]]
        Output: 0
        Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
        :return:
        """
        grid = [[0, 2]]
        output = 0
        self.assertEqual(output, RottingOranges().orangesRotting(grid))

    def test_oranges_rotting__02_20(self):
        grid = [[0, 2],
                [2, 0]]
        output = 0
        self.assertEqual(output, RottingOranges().orangesRotting(grid))

    def test_oranges_rotting__20_02(self):
        grid = [[2, 0],
                [0, 2]]
        output = 0
        self.assertEqual(output, RottingOranges().orangesRotting(grid))

    def test_oranges_rotting__02_20(self):
        grid = [[0, 2],
                [2, 0]]
        output = 0
        self.assertEqual(output, RottingOranges().orangesRotting(grid))

    def test_oranges_rotting__10_01(self):
        grid = [[1, 0],
                [0, 1]]
        output = -1
        self.assertEqual(output, RottingOranges().orangesRotting(grid))

    def test_oranges_rotting__211_101_111(self):
        grid = [[2, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
                ]
        output = 4
        self.assertEqual(output, RottingOranges().orangesRotting(grid))

    def test_oranges_rotting__1(self):
        grid = [[1]]
        output = -1
        self.assertEqual(output, RottingOranges().orangesRotting(grid))

    def test_oranges_rotting__2(self):
        grid = [[2]]
        output = 0
        self.assertEqual(output, RottingOranges().orangesRotting(grid))

    def test_oranges_rotting__0(self):
        grid = [[0]]
        output = 0
        self.assertEqual(output, RottingOranges().orangesRotting(grid))

    def test_oranges_rotting__S(self):
        grid = [[2,1,1],
                [0,0,1],
                [1,1,1],
                [1,0,0],
                [1,1,1]]
        output = 10
        self.assertEqual(output, RottingOranges().orangesRotting(grid))

    def test_oranges_rotting__22_11_00_20(self):
        grid = [[2,2],
                [1,1],
                [0,0],
                [2,0]]
        output = 1
        self.assertEqual(output, RottingOranges().orangesRotting(grid))

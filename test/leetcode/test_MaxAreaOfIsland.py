from unittest import TestCase

from pyquiz.leetcode.MaxAreaOfIsland import MaxAreaOfIsland


class TestMaxAreaOfIsland(TestCase):
    def test_max_area_of_island__example1(self):
        """
        Example 1:
        [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
        """
        grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
        res = MaxAreaOfIsland().maxAreaOfIsland(grid)
        self.assertEqual(6, res)

    def test_max_area_of_island__example2(self):
        """
        Example 2:
        [[0,0,0,0,0,0,0,0]]
        Given the above grid, return 0.
        """
        grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
        res = MaxAreaOfIsland().maxAreaOfIsland(grid)
        self.assertEqual(0, res)

    def test_max_area_of_island__1(self):
        grid = [[1]]
        res = MaxAreaOfIsland().maxAreaOfIsland(grid)
        self.assertEqual(1, res)

    def test_max_area_of_island__0(self):
        grid = [[0]]
        res = MaxAreaOfIsland().maxAreaOfIsland(grid)
        self.assertEqual(0, res)

    def test_max_area_of_island__01(self):
        grid = [[0, 1]]
        res = MaxAreaOfIsland().maxAreaOfIsland(grid)
        self.assertEqual(1, res)

    def test_max_area_of_island__01_10(self):
        grid = [[0, 1], [1, 0]]
        res = MaxAreaOfIsland().maxAreaOfIsland(grid)
        self.assertEqual(1, res)

    def test_max_area_of_island__10_01(self):
        grid = [[1, 0], [0, 1]]
        res = MaxAreaOfIsland().maxAreaOfIsland(grid)
        self.assertEqual(1, res)

    def test_max_area_of_island__11_11(self):
        grid = [[1, 1], [1, 1]]
        res = MaxAreaOfIsland().maxAreaOfIsland(grid)
        self.assertEqual(4, res)

    def test_max_area_of_island__11_10(self):
        grid = [[1, 1], [1, 0]]
        res = MaxAreaOfIsland().maxAreaOfIsland(grid)
        self.assertEqual(3, res)

    def test_max_area_of_island__10_10(self):
        grid = [[1, 0], [1, 0]]
        res = MaxAreaOfIsland().maxAreaOfIsland(grid)
        self.assertEqual(2, res)

    def test_max_area_of_island__0_1_1_0_1(self):
        grid = [[0], [1], [1], [0], [1]]
        res = MaxAreaOfIsland().maxAreaOfIsland(grid)
        self.assertEqual(2, res)

from unittest import TestCase
from pyquiz.leetcode.TrappingRainWater2 import Solution


class TestSolution(TestCase):

    def test_trap2d__big_and_small_hole_10202(self):
        """
        00101
        10101
        11111
        """
        self.assertEqual([0, 1, 0, 2, 0], Solution().trap_2d(height=[1, 0, 2, 0, 2]))

    def test_trap2d_1(self):
        self.assertEqual([0], Solution().trap_2d([1]))

    def test_trap2d_101(self):
        self.assertEqual([0, 1, 0], Solution().trap_2d([1, 0, 1]))

    def test_trap2d_1210121(self):
        self.assertEqual([0, 0, 1, 2, 1, 0, 0], Solution().trap_2d([1, 2, 1, 0, 1, 2, 1]))

    def test_trap__example2d1(self):
        """
        Example 1 from 2d:
        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
        In this case, 6 units of rain water (blue section) are being trapped.
        """
        self.assertEqual(6,
                         Solution().trapRainWater(heightMap=[[2] * 12, [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], [2] * 12]))

    def test_trap__example2d_2(self):
        """
        Example 2d 2:
        Input: height = [4,2,0,3,2,5]
        Output: 9
        """
        self.assertEqual(9, Solution().trapRainWater(heightMap=[[5] * 6, [4, 2, 0, 3, 2, 5], [5] * 6]))

    def test_trap__singlehole1011(self):
        """
        1011
        """
        self.assertEqual(1, Solution().trapRainWater(heightMap=[[1] * 4, [1, 0, 1, 1], [1] * 4]))

    def test_trap__singlehole101(self):
        """
        101
        """
        self.assertEqual(1, Solution().trapRainWater(heightMap=[[1] * 3, [1, 0, 1], [1] * 3]))

    def test_trap__singlehole201(self):
        """
        1
        101
        """
        self.assertEqual(1, Solution().trapRainWater(heightMap=[[1] * 3, [2, 0, 1], [1] * 3]))

    def test_trap__singlehole102(self):
        """
          1
        101
        """
        self.assertEqual(1, Solution().trapRainWater(heightMap=[[1] * 3, [1, 0, 2], [1] * 3]))

    def test_trap__doublehole10101(self):
        """
        10101
        """
        self.assertEqual(2, Solution().trapRainWater(heightMap=[[1] * 5, [1, 0, 1, 0, 1], [1] * 5]))

    def test_trap__thole21012(self):
        """
        10001
        11011
        """
        self.assertEqual(4, Solution().trapRainWater(heightMap=[[2] * 5, [2, 1, 0, 1, 2], [2] * 5]))

    def test_trap__big_and_small_hole_10202(self):
        """
        22222
        10202
        22222
        """
        self.assertEqual(3, Solution().trapRainWater(heightMap=[[2] * 5, [1, 0, 2, 0, 2], [2] * 5]))

    def test_trap__thole1021012(self):
        """
        0010001
        1011011
        """
        self.assertEqual(5, Solution().trapRainWater(heightMap=[[2] * 7, [1, 0, 2, 1, 0, 1, 2], [2] * 7]))

    def test_trap__2121(self):
        """
        1 1
        1111
        """
        self.assertEqual(1, Solution().trapRainWater(heightMap=[[2] * 4, [2, 1, 2, 1], [2] * 4]))

    def test_trap__12121(self):
        """
         1 1
        11111
        """
        self.assertEqual(1, Solution().trapRainWater(heightMap=[[2] * 5, [1, 2, 1, 2, 1], [2] * 5]))

    def test_trap__example1test(self):
        """
        1 1
        11111
        """
        # self.assertEqual(1, Solution().trapRainWater(heightMap=[3,2,1,2,1]))
        # self.assertEqual(1, Solution().trapRainWater(heightMap=[3,1,2,1]))
        self.assertEqual(1, Solution().trapRainWater(heightMap=[[1] * 4, [2, 0, 1, 0], [1] * 4]))

    def test_trap_1(self):
        self.assertEqual(0, Solution().trapRainWater(heightMap=[[1]]))

    def test_trap_11(self):
        self.assertEqual(0, Solution().trapRainWater(heightMap=[[1, 1]]))

    def test_trap_111(self):
        self.assertEqual(0, Solution().trapRainWater(heightMap=[[1, 1, 1]]))

    def test_trap_121(self):
        self.assertEqual(0, Solution().trapRainWater(heightMap=[[1, 2, 1]]))

    def test_trap_empty(self):
        self.assertEqual(0, Solution().trapRainWater(heightMap=[[]]))

    def test_trap_none(self):
        self.assertEqual(0, Solution().trapRainWater(heightMap=None))

    def test_trap_example1(self):
        """
        Example 1:
        Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
        Output: 4
        Explanation: After the rain, water is trapped between the blocks.
        We have two small pounds 1 and 3 units trapped.
        The total volume of water trapped is 4."""
        self.assertEqual(4, Solution().trapRainWater(
            heightMap=[[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))

    def test_trap_example2(self):
        """
        Example 2:
        Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
        Output: 10
        """
        self.assertEqual(10, Solution().trapRainWater(
            heightMap=[[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))

    def test_trap_010_101_010(self):
        self.assertEqual(1, Solution().trapRainWater(
            heightMap=[[2, 1, 0], [1, 0, 1], [0, 1, 0]]))

    def test_trap_large(self):
        m = [list(range(200))] * 200
        self.assertIsNotNone(Solution().trapRainWater(heightMap=m))

    def test_err(self):
        m = [[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]
        self.assertEqual(14, Solution().trapRainWater(heightMap=m))

    def test_trap_bad(self):
        self.assertEqual(0, Solution().trapRainWater(
            heightMap=[[1, 0, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]))

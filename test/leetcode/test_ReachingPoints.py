from unittest import TestCase, skip
from pyquiz.leetcode.ReachingPoints import Solution


class TestSolution(TestCase):
    def test_reaching_points__example1(self):
        """
        Input: sx = 1, sy = 1, tx = 3, ty = 5
        Output: True
        Explanation:
        One series of moves that transforms the starting point to the target is:
        (1, 1) -> (1, 2)
        (1, 2) -> (3, 2)
        (3, 2) -> (3, 5)
        """
        self.assertTrue(Solution().reachingPoints(sx=1, sy=1, tx=3, ty=5))

    def test_reaching_points__example2(self):
        """
        Input: sx = 1, sy = 1, tx = 2, ty = 2
        Output: False
        """
        self.assertFalse(Solution().reachingPoints(sx=1, sy=1, tx=2, ty=2))

    def test_reaching_points__example3(self):
        """
        Input: sx = 1, sy = 1, tx = 1, ty = 1
        Output: True
        """
        self.assertTrue(Solution().reachingPoints(sx=1, sy=1, tx=1, ty=1))


    def test_reaching_points__large(self):
        Solution().reachingPoints(1,1,1000000000,1000000000)

    def test_reaching_points__large_1(self):
        Solution().reachingPoints(1,1,1,1000000000)

    def test_reaching_points__2_2_4_2(self):
        self.assertTrue(Solution().reachingPoints(sx=2, sy=2, tx=4, ty=2))

    def test_reaching_points__2_2_2_4(self):
        self.assertTrue(Solution().reachingPoints(sx=2, sy=2, tx=4, ty=2))

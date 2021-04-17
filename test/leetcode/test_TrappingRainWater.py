from unittest import TestCase
from pyquiz.leetcode.TrappingRainWater import Solution


class TestSolution(TestCase):
    def test_trap__example1(self):
        """
        Example 1:
        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
        In this case, 6 units of rain water (blue section) are being trapped.
        """
        self.assertEqual(6, Solution().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    def test_trap__example2(self):
        """
        Example 2:
        Input: height = [4,2,0,3,2,5]
        Output: 9
        """
        self.assertEqual(9, Solution().trap(height=[4, 2, 0, 3, 2, 5]))

    def test_trap__singlehole1011(self):
        """
        1011
        """
        self.assertEqual(1, Solution().trap(height=[1, 0, 1,1]))

    def test_trap__singlehole101(self):
        """
        101
        """
        self.assertEqual(1, Solution().trap(height=[1, 0, 1]))

    def test_trap__singlehole201(self):
        """
        1
        101
        """
        self.assertEqual(1, Solution().trap(height=[2, 0, 1]))

    def test_trap__singlehole102(self):
        """
          1
        101
        """
        self.assertEqual(1, Solution().trap(height=[1, 0, 2]))

    def test_trap__doublehole10101(self):
        """
        10101
        """
        self.assertEqual(2, Solution().trap(height=[1, 0, 1, 0, 1]))

    def test_trap__thole21012(self):
        """
        10001
        11011
        """
        self.assertEqual(4, Solution().trap(height=[2, 1, 0, 1, 2]))

    def test_trap__thole1021012(self):
        """
        0010001
        1011011
        """
        self.assertEqual(5, Solution().trap(height=[1, 0, 2, 1, 0, 1, 2]))

    def test_trap__2121(self):
        """
        1 1
        1111
        """
        self.assertEqual(1, Solution().trap(height=[2, 1, 2,1]))

    def test_trap__12121(self):
        """
         1 1
        11111
        """
        self.assertEqual(1, Solution().trap(height=[1,2, 1, 2,1]))

    def test_trap__example1test(self):
        """
        1 1
        11111
        """
        #self.assertEqual(1, Solution().trap(height=[3,2,1,2,1]))
        #self.assertEqual(1, Solution().trap(height=[3,1,2,1]))
        self.assertEqual(1, Solution().trap(height=[2,0,1,0]))

    def test_trap_1(self):
        self.assertEqual(0, Solution().trap(height=[1]))

    def test_trap_11(self):
        self.assertEqual(0, Solution().trap(height=[1,1]))

    def test_trap_111(self):
        self.assertEqual(0, Solution().trap(height=[1,1,1]))

    def test_trap_121(self):
        self.assertEqual(0, Solution().trap(height=[1,2,1]))

    def test_trap_empty(self):
        self.assertEqual(0, Solution().trap(height=[]))

    def test_trap_none(self):
        self.assertEqual(0, Solution().trap(height=None))

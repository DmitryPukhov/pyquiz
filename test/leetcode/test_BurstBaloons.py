from unittest import TestCase
from pyquiz.leetcode.BurstBaloons import Solution


class TestSolution(TestCase):
    def test_max_coins__example1(self):
        """
        Example 1:

        Input: nums = [3,1,5,8]
        Output: 167
        Explanation:
        nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
        coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
        """
        self.assertEqual(167, Solution().maxCoins([3,1,5,8]))

    def test_max_coins__1_2_3__12(self):
        self.assertEqual(12, Solution().maxCoins([1,2,3]))

    def test_max_coins__example2(self):
        """
        Example 2:
        Input: nums = [1,5]
        Output: 10
        """
        self.assertEqual(10, Solution().maxCoins([1,5]))

    def test_max_coins__1__1(self):
        self.assertEqual(1, Solution().maxCoins([1]))

    def test_max_coins__1_2__4(self):
        self.assertEqual(4, Solution().maxCoins([1,2]))

    def test_max_coins__2_1__4(self):
        self.assertEqual(4, Solution().maxCoins([2,1]))

    def test_max_coins__112345__110(self):
        self.assertEqual(110, Solution().maxCoins([1,2,3,4,5]))

    def test_max_coins__2222(self):
        self.assertEqual(22, Solution().maxCoins([2,2,2,2]))

    def test_max_coins__many1(self):
        self.assertEqual(100, Solution().maxCoins([1]*100))

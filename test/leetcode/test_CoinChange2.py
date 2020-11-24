from unittest import TestCase

from pyquiz.leetcode.CoinChange2 import CoinChange2


class TestCoinChange2(TestCase):
    def test_change__example1(self):
        """
        Example 1:
        Input: amount = 5, coins = [1, 2, 5]
        Output: 4
        Explanation: there are four ways to make up the amount:
        5=5
        5=2+2+1
        5=2+1+1+1
        5=1+1+1+1+1
        """
        res = CoinChange2().change(amount=5, coins=[1, 2, 5])
        self.assertEqual(4, res)

    def test_change__example2(self):
        """
        Example 2:
        Input: amount = 3, coins = [2]
        Output: 0
        Explanation: the amount of 3 cannot be made up just with coins of 2.
        """
        res = CoinChange2().change(amount=3, coins=[2])
        self.assertEqual(0, res)

    def test_change__example__11(self):
        res = CoinChange2().change(amount=1, coins=[1,1])
        self.assertEqual(2, res)

    def test_change__big(self):
        coins = [1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10,1,2,5,6,7,8,9,10]
        res = CoinChange2().change(amount=5, coins=coins)
        self.assertEqual(26518714, res)

    def test_change__21_1(self):
        res = CoinChange2().change(amount=1, coins=[2,1])
        self.assertEqual(1, res)

    def test_change__empty_7(self):
        res = CoinChange2().change(amount=0, coins=[7])
        # Leetcode expects 1 for 0 amount
        self.assertEqual(1, res)

    def test_change__empty(self):
        res = CoinChange2().change(amount=0, coins=[])
        # Leetcode expects 1 for 0 amount
        self.assertEqual(1, res)

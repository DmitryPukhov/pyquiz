from unittest import TestCase

from pyquiz.leetcode.CoinChange import CoinChange


class TestCoinChange(TestCase):

    def test_coin_change__1_2_5_11(self):
        """
        Example 1:
        Input: coins = [1,2,5], amount = 11
        Output: 3
        Explanation: 11 = 5 + 5 + 1
        """
        self.assertEqual(3, CoinChange().coinchange_topdown([1, 2, 5], 11))
        self.assertEqual(3, CoinChange().coinchange_bottomup([1, 2, 5], 11))

    def test_coin_change__2_3(self):
        """
        Example 2:
        Input: coins = [2], amount = 3
        Output: -1
        """
        self.assertEqual(-1, CoinChange().coinchange_topdown([2], 3))
        self.assertEqual(-1, CoinChange().coinchange_bottomup([2], 3))

    def test_coin_change__1_0(self):
        """
        Example 3:
        Input: coins = [1], amount = 0
        Output: 0
        """
        self.assertEqual(0, CoinChange().coinchange_topdown([1], 0))
        self.assertEqual(0, CoinChange().coinchange_bottomup([1], 0))

    def test_coin_change__1_1(self):
        """
        Example 4:
        Input: coins = [1], amount = 1
        Output: 1
        """
        self.assertEqual(1, CoinChange().coinchange_topdown([1], 1))
        self.assertEqual(1, CoinChange().coinchange_bottomup([1], 1))

    def test_coin_change__1_2(self):
        """
        Example 5:
        Input: coins = [1], amount = 2
        Output: 2
        """
        self.assertEqual(2, CoinChange().coinchange_topdown([1], 2))
        self.assertEqual(2, CoinChange().coinchange_bottomup([1], 2))

    def test_coin_change__1_1_2(self):
        self.assertEqual(2, CoinChange().coinchange_topdown([1, 1], 2))
        self.assertEqual(2, CoinChange().coinchange_bottomup([1, 1], 2))

    def test_coin_change__5_2_8(self):
        self.assertEqual(4, CoinChange().coinchange_topdown([5, 2], 8))
        self.assertEqual(4, CoinChange().coinchange_bottomup([5, 2], 8))

    def test_coin_change__186_419_83_408(self):
        self.assertEqual(20, CoinChange().coinchange_topdown([186, 419, 83, 408], 6249))
        self.assertEqual(20, CoinChange().coinchange_bottomup([186, 419, 83, 408], 6249))

    def test_coin_change__long(self):
        self.assertEqual(83334, CoinChange().coinchange_bottomup([1,2,3,4,5,6,7,8,9,10,11,12], 999999))

    # def test_coin_change__maxintamount(self):
    #     self.assertEqual(178956971, CoinChange().coinChange([1,2,3,4,5,6,7,8,9,10,11,12], 2147483647))

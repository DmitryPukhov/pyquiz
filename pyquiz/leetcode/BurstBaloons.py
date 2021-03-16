from functools import lru_cache
from typing import List, Tuple


class Solution:
    """
    You are given n balloons, indexed from 0 to n - 1.
    Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
    If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
    If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

    Return the maximum coins you can collect by bursting the balloons wisely.

    Example 1:

    Input: nums = [3,1,5,8]
    Output: 167
    Explanation:
    nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
    coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

    Example 2:
    Input: nums = [1,5]
    Output: 10
    """

    def maxCoins(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            # Verbose version:
            #     out = 0
            #     for i in range(left + 1, right):
            #         currcoins = nums[i] * nums[left] * nums[right]
            #         leftcoins = dp(left, i)
            #         rightcoins = dp(i, right)
            #         out = max(out, currcoins + leftcoins + rightcoins)
            #     return out
            #

            # Base Case
            if left +1 == right:
                return 0
            # One liner
            return max([nums[i]*nums[left]*nums[right] + dp(left,i) + dp(i,right) for i in range(left+1,right)])
        nums = [1] + nums + [1]
        return dp(0, len(nums) - 1)

    def maxCoins_bruit_force(self, nums: List[int]) -> int:
        coins = 0
        for i in range(0, len(nums)):
            coins = max(coins, self.birst_bruit_force(i, tuple(nums)))
        return coins

    @lru_cache(None)
    def birst_bruit_force(self, i: int, tnums: Tuple[int]):
        """
        Bruite force recursive birst all possible graph
        """
        nums = list(tnums)
        if len(nums) == 1:
            return nums[0]
        prev = nums[i - 1] if i > 0 else 1
        next = nums[i + 1] if i < len(nums) - 1 else 1
        num = nums.pop(i)
        coins = num * prev * next + max([self.birst(i, tuple(nums)) for i in range(0, len(nums))])
        return coins

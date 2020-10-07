from typing import List


class CoinChange:
    """
    You are given coins of different denominations and a total amount of money amount.
    Write a function to compute the fewest number of coins that you need to make up that amount.
    If that amount of money cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.


    Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

    Example 2:
    Input: coins = [2], amount = 3
    Output: -1

    Example 3:
    Input: coins = [1], amount = 0
    Output: 0

    Example 4:
    Input: coins = [1], amount = 1
    Output: 1

    Example 5:
    Input: coins = [1], amount = 2
    Output: 2

    Constraints:
    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 231 - 1
    """
    def coinchange_bottomup(self, coins: List[int], amount: int) -> int:
        """
        Bottom up approach
        """
        dp = [0] + [amount] * amount
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - coin] + 1 for coin in coins + [0] if i >= coin])
        return dp[-1] if dp[-1] <= amount else -1


    def coinchange_topdown(self, coins: List[int], amount: int) -> int:
        """
        Top down approach
        """
        memo = [0] + [amount+1]*amount
        out = self._coinchange_topdown(coins, amount, memo)
        return out if out <= amount else -1

    def _coinchange_topdown(self, coins: List[int], amount: int, memo: List[int]) -> int:
        if amount == 0:
            return 0
        elif amount in coins:
            memo[amount] = 1
            return 1
        elif memo[amount]>amount:
            minprev=min([amount+1]+[self._coinchange_topdown(coins, amount-i, memo) for i in coins if i < amount])
            memo[amount]= min(memo[amount], minprev)+1

        return memo[amount]


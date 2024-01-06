# Created by Adarsh N B at 11/14/2023

# Description:
"""
You are given an integer array coins representing coins of different denominations and an integer amount representing
a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
any combination of the coins, return -1.

You may assume that you have an **infinite** number of each kind of coin
"""
from typing import List


class Solution:

    @staticmethod
    def coin_chainge(amount: int, coins: List[int]) -> int:

        dp = [amount+1 for _ in range(amount+1)]

        dp[0] = 0  # we don't need any coins to get 0 amount xD

        for a in range(1, amount+1):
            for c in coins:
                if c <= amount:
                    dp[a] = min(dp[a], 1 + dp[amount-c])

        return dp[amount] if dp[amount] != amount+1 else -1

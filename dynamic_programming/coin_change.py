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
                if c <= a:
                    # dp[a] is if you don't pick up the current coin
                    dp[a] = min(dp[a], 1 + dp[a-c])

        return dp[amount] if dp[amount] != amount+1 else -1

    def coin_change_recursive_memoized(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        ans = self.coin_change_recursive_memoized_helper(coins, amount, len(coins)-1, dp)
        if ans > amount:
            return -1
        return ans

    def coin_change_recursive_memoized_helper(self, coins: List[int], amount: int, ind: int, dp: List[List[int]]):
        if ind == 0:
            if amount % coins[0] == 0:
                return amount//coins[0]
            else:
                return amount+1  # assuming amount+1 is the max
        if dp[ind][amount] != -1:
            return dp[ind][amount]
        pick = amount+1
        if amount >= coins[ind]:
            # we are going to keep checking if we can use the same coin again, as the next line would pick up without
            pick = 1 + self.coin_change_recursive_memoized_helper(coins, amount-coins[ind], ind, dp)

        not_pick = self.coin_change_recursive_memoized_helper(coins, amount, ind-1, dp)

        dp[ind][amount] = min(pick, not_pick)
        return dp[ind][amount]

    @staticmethod
    def coin_change_tabulation(coins: List[int], amount: int) -> int:
        c = len(coins)
        dp = [[amount+1 for _ in range(amount + 1)] for _ in range(c)]
        for amt in range(amount+1):
            if amt % coins[0] == 0:
                dp[0][amt] = amt//coins[0]
        for coins_ind in range(1, c):
            for amt in range(amount+1):
                not_pick = dp[coins_ind-1][amt]
                pick = amount+1
                if coins[coins_ind] <= amt:
                    pick = 1 + dp[coins_ind][amt-coins[coins_ind]]
                dp[coins_ind][amt] = min(pick, not_pick)
        res = dp[c-1][amount]
        if res == amount+1:
            return -1
        return res

    @staticmethod
    def coin_change_tabulation_space_optimized(coins: List[int], amount: int) -> int:
        c = len(coins)
        prev = [amount+1 for _ in range(amount + 1)]
        for amt in range(amount+1):
            if amt % coins[0] == 0:
                prev[amt] = amt//coins[0]
        for coins_ind in range(1, c):
            curr = [amount + 1 for _ in range(amount + 1)]
            for amt in range(amount+1):
                not_pick = prev[amt]
                pick = amount+1
                if coins[coins_ind] <= amt:
                    pick = 1 + curr[amt-coins[coins_ind]]
                curr[amt] = min(pick, not_pick)
            prev = [k for k in curr]
        res = prev[amount]
        if res == amount+1:
            return -1
        return res


if __name__ == "__main__":
    coins_list = [[1, 2, 5], [1, 2, 3], [1], [2], [2, 5, 10, 1]]
    amount_list = [11, 7, 1, 0, 27]
    soln = Solution()
    for i in range(len(coins_list)):
        print("fully space optimized and tabular")
        print(soln.coin_chainge(amount_list[i], coins_list[i]))
        print("recursive memoized")
        print(soln.coin_change_recursive_memoized(coins_list[i], amount_list[i]))
        print("Tabulation")
        print(soln.coin_change_tabulation(coins_list[i], amount_list[i]))
        print("Tab space optimized")
        print(soln.coin_change_tabulation_space_optimized(coins_list[i], amount_list[i]))

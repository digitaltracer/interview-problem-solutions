# Created by Adarsh N B at 3/11/2024

# Description:
"""
This is similar to problem 2 with the limitation that the number of transactions is limited to 2.(2 buys, 2 sells)
With this limitation all the change we need to do is add one more variable that will keep track of the number of
transactions done.
Time complexity - O(n)
Space complexity - O(n)
"""
from typing import List


def max_profit_rec(prices: List[int], n: int) -> int:
    dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
    return max_profit_rec_helper(0, 1, 2, prices, n, dp)


def max_profit_rec_helper(ind: int, buy: int, cap: int, prices: List[int], n: int, dp: List[List[List[int]]]) -> int:
    if ind == n or cap == 0:
        return 0

    if dp[ind][buy][cap] != -1:
        return dp[ind][buy][cap]

    if buy:
        option_buy = -prices[ind] + max_profit_rec_helper(ind+1, 0, cap, prices, n, dp)
        option_not_buy = max_profit_rec_helper(ind+1, 1, cap, prices, n, dp)
        profit = max(option_buy, option_not_buy)
    else:
        option_sell = prices[ind] + max_profit_rec_helper(ind+1, 1, cap-1, prices, n, dp)
        option_not_sell = max_profit_rec_helper(ind+1, 0, cap, prices, n, dp)
        profit = max(option_sell, option_not_sell)

    dp[ind][buy][cap] = profit
    return dp[ind][buy][cap]


def max_profit_tabulation(prices: List[int], n: int) -> int:
    dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]

    # Since we have initialized the entire dp array to 0, we don't need to set base cases to 0

    for ind in range(n-1, -1, -1):
        for buy in range(2):
            for cap in range(1, 3):
                if buy:
                    option_buy = dp[ind + 1][0][cap] - prices[ind]
                    option_not_buy = dp[ind + 1][1][cap]
                    profit = max(option_buy, option_not_buy)
                else:
                    option_sell = prices[ind] + dp[ind + 1][1][cap-1]
                    option_not_sell = dp[ind + 1][0][cap]
                    profit = max(option_sell, option_not_sell)
                dp[ind][buy][cap] = profit
    return dp[0][1][2]


if __name__ == "__main__":
    cost = [3, 3, 5, 0, 0, 3, 1, 4]
    print(max_profit_rec(cost, len(cost)))
    print(max_profit_tabulation(cost, len(cost)))

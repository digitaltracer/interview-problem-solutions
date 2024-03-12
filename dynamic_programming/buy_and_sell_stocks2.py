# Created by Adarsh N B at 3/11/2024

# Description:
"""
It's the same as buy and sell stocks, but here you can buy and sell as many times you want on the condition that you
cannot buy stocks again without selling the previous bought stocks
Time complexity - 
Space complexity - 
"""
from typing import List


def maximum_profit(values: List[int], n: int) -> int:
    dp = [[-1, -1] for _ in range(n)]
    return maximum_profit_helper(0, 1, values, n, dp)


def maximum_profit_helper(ind: int, buy: int, values: List[int], n: int, dp: List[List[int]]) -> int:

    if ind == n:
        return 0

    if dp[ind][buy] != -1:
        return dp[ind][buy]

    if buy:
        option_buy = -values[ind] + maximum_profit_helper(ind+1, 0, values, n, dp)
        option_not_buy = maximum_profit_helper(ind+1, 1, values, n, dp)
        profit = max(option_buy, option_not_buy)
    else:
        option_sell = values[ind] + maximum_profit_helper(ind+1, 1, values, n, dp)
        option_not_sell = maximum_profit_helper(ind+1, 0, values, n, dp)
        profit = max(option_sell, option_not_sell)

    dp[ind][buy] = profit
    return dp[ind][buy]


def maximum_profit_tabular(values: List[int], n: int) -> int:
    dp = [[-1, -1] for _ in range(n+1)]

    dp[n][0] = dp[n][1] = 0

    for ind in range(n-1, -1, -1):
        for buy in range(2):
            if buy == 1:
                option_buy = -values[ind] + dp[ind + 1][0]
                option_not_buy = dp[ind + 1][1]
                profit = max(option_buy, option_not_buy)
            else:
                option_sell = values[ind] + dp[ind + 1][1]
                option_not_sell = dp[ind + 1][0]
                profit = max(option_sell, option_not_sell)
            dp[ind][buy] = profit

    return dp[0][1]


if __name__ == "__main__":
    n = 6
    vals = [7, 1, 5, 3, 6, 4]
    print(maximum_profit_tabular(vals, n))
    print(maximum_profit(vals, n))

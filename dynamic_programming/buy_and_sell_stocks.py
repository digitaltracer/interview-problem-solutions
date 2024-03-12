# Created by Adarsh N B at 3/11/2024

# Description:
"""
You are given a price array which consists of the prices of the stock at ith day. Return the maximum profit you
can earn with this array.
Time complexity - O(n)
Space complexity - O(1)
"""
from typing import List


def maximum_profit(price: List[int]) -> int:
    max_profit = 0
    min_cost = price[0]

    for i in range(1, len(price)):
        min_cost = min(min_cost, price[i])
        max_profit = max(max_profit, (price[i]-min_cost))

    return max_profit


if __name__ == "__main__":
    print(maximum_profit([7, 1, 5, 3, 6, 4]))

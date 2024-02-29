# Created by Adarsh N B at 1/4/2024

# Description:
"""
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value
in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with
N items respectively.
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that
sum of the weights of this subset is smaller than or equal to W.
You cannot break an item, either pick the complete item or don't pick it (0-1 property).
"""
from typing import List
from copy import deepcopy


def knapsack_recursion(val: List[int], wt: List[int], w: int) -> int:
    return knapsack_recursion_helper(val, wt, len(wt)-1, w)


def knapsack_recursion_helper(val: List[int], wt: List[int], ind: int, w: int) -> int:
    # varying arguments are ind and w
    # starting off with a base case
    if ind == 0:
        if w >= wt[0]:
            # assuming val contains only positive values
            return val[0]
        return 0

    pick = 0
    if w >= wt[ind]:
        pick = val[ind] + knapsack_recursion_helper(val, wt, ind-1, w-wt[ind])
    not_pick = knapsack_recursion_helper(val, wt, ind-1, w)

    return max(pick, not_pick)


def knapsack_recursion_memoized(val: List[int], wt: List[int], w: int) -> int:
    n = len(val)
    # since there are two varying arguments we will need 2d array dp[n-1][w+1]
    # as we go from 0....n-1 and 0....w
    d2 = [-1] * (w+1)
    dp = [deepcopy(d2) for _ in range(n)]
    return knapsack_recursion__memoized_helper(val, wt, n-1, w, dp)


def knapsack_recursion__memoized_helper(val: List[int], wt: List[int], ind: int, w: int, dp: List[List[int]]) -> int:
    # varying arguments are ind and w
    # starting off with a base case
    if ind == 0:
        if w >= wt[0]:
            # assuming val contains only positive values
            return val[0]
        return 0

    pick = 0
    if w >= wt[ind]:
        pick = val[ind] + knapsack_recursion_helper(val, wt, ind-1, w-wt[ind])
    not_pick = knapsack_recursion_helper(val, wt, ind-1, w)

    dp[ind][w] = max(pick, not_pick)
    return dp[ind][w]


def knapsack_tabulation(val: List[int], wt: List[int], w: int) -> int:
    # going to do it directly for space optimized.
    prev = [-1] * (w+1)

    # at index 0, if capacity of the bag is wt[0] or more, we will pick it and the value will be val[0]
    for cap in range(wt[0], w+1):
        prev[cap] = val[0]

    for ind in range(1, len(val)):
        curr = [-1] * (w+1)
        for cap in range(w):
            not_take = prev[cap]
            take = 0
            if wt[ind] <= cap:
                take = val[ind] + prev[cap - wt[ind]]
            curr[cap] = max(take, not_take)
        prev = [c for c in curr]

    return prev[w-1]


if __name__ == "__main__":
    values = [[1, 2, 3], [1, 2, 3]]
    weights = [[4, 5, 1], [4, 5, 6]]
    capacities = [4, 3]
    for i in range(len(values)):
        print(knapsack_recursion(values[i], weights[i], capacities[i]))
        print(knapsack_recursion_memoized(values[i], weights[i], capacities[i]))
        print(knapsack_tabulation(values[i], weights[i], capacities[i]))

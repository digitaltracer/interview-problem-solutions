# Created by Adarsh N B at 3/7/2024

# Description:
"""
This is the same as 0/1 knapsack, except the fact that there are unlimited supplies of the same items
Time complexity - 
Space complexity - 
"""
from typing import List


def unbounded_knapsack_rec(val: List[int], wt: List[int], w: int) -> int:
    return unbounded_knapsack_rec_helper(val, wt, len(wt)-1, w)


def unbounded_knapsack_rec_helper(val: List[int], wt: List[int], ind: int, current_capacity: int) -> int:

    if ind == 0:
        return val[0] * (current_capacity//wt[0])

    not_pick = 0 + unbounded_knapsack_rec_helper(val, wt, ind-1, current_capacity)

    # initialise pick to a very negative number
    pick = -1  # assuming val is a positive int list

    if current_capacity >= wt[ind]:
        pick = wt[ind] + unbounded_knapsack_rec_helper(val, wt, ind, current_capacity-wt[ind])

    return max(pick, not_pick)

# This will take x**n (exponential. not 2**n as we have more than 2 choices, pick, not pick, pick and stay in the same
# index) time complexity as every node has 2 options. So we will need to memoize to bring it down to n
# Since there are two variables in the recursion, we will be needing a 2D array to cache things.


def unbounded_knapsack_rec_memoized(val: List[int], wt: List[int], w: int) -> int:
    dp = [[-1 for _ in range(w+1)] for _ in range(len(wt))]
    return unbounded_knapsack_rec_helper_memoized(val, wt, len(wt)-1, w, dp)


def unbounded_knapsack_rec_helper_memoized(val: List[int], wt: List[int], ind: int, current_capacity: int,
                                           dp: List[List[int]]) -> int:
    # everything will be same as the above function, except we will be storing the result in the dp array
    if ind == 0:
        return val[0] * (current_capacity//wt[0])

    if dp[ind][current_capacity] != -1:
        return dp[ind][current_capacity]

    not_pick = 0 + unbounded_knapsack_rec_helper_memoized(val, wt, ind-1, current_capacity, dp)

    pick = -1

    if current_capacity >= wt[ind]:
        pick = wt[ind] + unbounded_knapsack_rec_helper_memoized(val, wt, ind, current_capacity, dp)

    dp[ind][current_capacity] = max(pick, not_pick)

    return dp[ind][current_capacity]

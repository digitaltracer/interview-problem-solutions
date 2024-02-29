# Created by Adarsh N B at 1/6/2024

# Description:
"""
There is a frog on the 1st step of an n stairs long staircase. The frog wants to reach nth stair.
height[i] is the height of (i+1)th stair. If frog jumps from ith to jth stair, the energy lost in the jump is given
by |height[i-1] - height[j-1]|.

If the frog is on ith staircase it can either jump to (i+1) or (i+2) stair. Your task is to find the minimum total
energy used by the frog to reach nth stair from 1st stair.

Time complexity - 
Space complexity - 
"""
from typing import List
from sys import maxsize


def frog_jump_rec(n: int, heights: List[int]) -> int:
    dp = [-1] * (n+1)
    return frog_jump_rec_helper(n-1, heights, dp)


def frog_jump_rec_helper(ind: int, heights: List[int], dp: List[int]) -> int:

    if ind == 0:
        return 0

    if dp[ind] != -1:
        return dp[ind]

    left = frog_jump_rec_helper(ind-1, heights, dp) + abs(heights[ind] - heights[ind-1])
    right = maxsize

    if ind > 0:
        right = frog_jump_rec_helper(ind-1, heights, dp) + abs(heights[ind] - heights[ind-2])

    dp[ind] = min(left, right)

    return dp[ind]


def frog_jump_tab(n: int, heights: List[int]) -> int:
    prev = 0
    first = 0
    curr = 0

    for i in range(len(heights)):
        pass

# Created by Adarsh N B at 1/17/2024

# Description:
"""
You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of
length n to minimize the absolute difference of the sums of the arrays.
To partition nums, put each element of nums into one of the two arrays.

Return the minimum possible absolute difference.

Time complexity - 
Space complexity - 
"""


"""
This is similar to subarray sum equals k, the difference here is, over there you will find out if the subsets
sum up to 0 to k, if we consider that as sum1 (possible set), total-sum1 would give the sum of remaining subset (s2)
With this if we calculate, |s1-s2| that would give the lowest difference.

"""
from typing import List


def min_difference_rec(nums: List[int]) -> int:
    pass


def min_difference_rec_helper(nums: List[int], ind: int, target: int) -> int:
    pass


def min_difference_tabular(nums: List[int]) -> int:
    ideal_sum = sum(nums)//2
    dp = [[False for _ in range(ideal_sum+1)] for _ in range(len(nums))]
    dp[0][0] = True
    if nums[0] <= ideal_sum:
        dp[0][nums[0]] = True
    for ind in range(1, len(nums)):
        for target in range(ideal_sum+1):
            pass

    return -1

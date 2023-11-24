# Created by Adarsh N B at 11/9/2023

# Description:
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.
"""
from typing import List


class Solution:

    @staticmethod
    def rob(nums: List[int]) -> int:
        profit1, profit2 = 0, 0
        # these two variables behave as a placeholders that precedes that nums array

        # [profit1, profit2, n, n+1, n+2, ....]

        for n in nums:
            temp = max(n + profit1, profit2)
            profit2 = profit1
            profit1 = profit2

        return profit2

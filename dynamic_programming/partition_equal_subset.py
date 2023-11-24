# Created by Adarsh N B at 11/15/2023

# Description:
"""
Given an integer array nums, return true if you can partition the array into two subsets
such that the sum of the elements in both subsets is equal or false otherwise.
LC: 416
"""
from typing import List


class Solution:

    @staticmethod
    def can_partition(nums: List[int]) -> bool:

        nums_sum = sum(nums)

        # If the sum is odd, then we cannot partition into two.
        if nums_sum % 2:
            return False

        target = nums_sum/2
        sums_set = {0}

        for i in range(len(nums)-1, -1, -1):
            current_set = set()
            for t in sums_set:
                if t + nums[i] == target:
                    return True
                current_set.add(t)
                current_set.add(t + nums[i])
            sums_set = current_set

        return target in sums_set

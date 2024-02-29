# Created by Adarsh N B at 1/17/2024

# Description:
"""
LC 416
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the
elements in both subsets is equal or false otherwise.

This is exactly similar as subarray_sum_equals_k as the logic is to get the total sum of the array and then divide
it by 2 and set the target as that (if the total sum is even)

Time complexity - 
Space complexity - 
"""
from typing import List


def can_partition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    print(target)

    prev = [False] * (target + 1)

    prev[0] = True
    if nums[0] <= target:
        prev[nums[0]] = True

    for ind in range(1, len(nums)):
        curr = [False] * (target + 1)
        curr[0] = True
        for targ in range(1, target + 1):
            not_take = prev[targ]
            take = False
            if targ >= nums[ind]:
                take = prev[targ - nums[ind]]
            curr[targ] = take or not_take
        prev = [i for i in curr]
    print(prev)
    return prev[target]


if __name__ == "__main__":
    print(can_partition(nums=[3, 3, 3, 4, 5]))

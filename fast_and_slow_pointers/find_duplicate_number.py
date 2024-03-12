# Created by Adarsh N B at 3/6/2024

# Description:
"""
Given an unsorted array of positive numbers, nums, such that the values lie in the range [1,n], inclusive, and that
there are n+1 numbers in the array, find and return the duplicate number present in nums.
There is only one repeated number in nums.
Time complexity - 
Space complexity - 
"""
from typing import List

"""
This problem is not intuitive at all. Unfortunately the only way I see it is to remember the logic.
"""


def find_duplicate(nums):
    fast = slow = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

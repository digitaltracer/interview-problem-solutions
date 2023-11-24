# Created by Adarsh N B at 11/16/2023

# Description:
"""
Given an array of integers nums, find all possible subsets of nums, including the empty set.
"""
from copy import deepcopy


def find_all_subsets(nums):
    # Replace this placeholder return statement with your code
    result = [[]]
    # nums = [1,2,3]
    for num in nums:
        tmp = deepcopy(result)
        for r in result:
            tmp_r = deepcopy(r)
            tmp_r.append(num)
            tmp.append(tmp_r)
        result = deepcopy(tmp)
    return result

# This solution can be made slightly better by converting to set and then converting the set to list instead of
# doing deepcopy at every step

# Created by Adarsh N B at 3/1/2024

# Description:
"""
LC 9
Given an array of integers `nums` that may contain duplicates, return all possible subsets (power set).
The solution set should not contain duplicate subsets. return solution in any order.
Time complexity - 
Space complexity - 
"""

from typing import List
from copy import deepcopy

"""
This can also be placed under backtracking as we remove the current step before proceeding to the next one 
"""


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans: List[List[int]] = []
    find_subsets(0, nums, [], ans)
    return ans


def find_subsets(ind: int, nums: List[int], cur_list: List[int], ans: List[List[int]]):
    ans.append(deepcopy(cur_list))

    for i in range(ind, len(nums)):
        if i != ind and nums[i] == nums[i-1]:
            continue

        cur_list.append(nums[i])
        find_subsets(i+1, nums, deepcopy(cur_list), ans)
        cur_list.pop()


if __name__ == "__main__":
    slist = [1, 2, 2, 3, 4, 2]
    print(subsets_with_dup(slist))

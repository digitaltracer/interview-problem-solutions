# Created by Adarsh N B at 1/16/2024

# Description:
"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

There can be many variants to the same problem
1. return true if possible
2. return total number of subarrays
3. return all the subarrays that match this criteria.

Time complexity - 
Space complexity - 
"""
from typing import List


def sub_array_sum_exists_rec(nums: List[int], k: int) -> bool:
    dp = [[-1 for _ in range(k + 1)] for _ in range(len(nums))]
    return sub_array_sum_exists_rec_helper(len(nums)-1, k, nums, dp)


def sub_array_sum_exists_rec_helper(ind: int, remaining_target: int, nums: List[int], dp: List[List[int]]) -> bool:

    if remaining_target == 0:
        return True

    if ind == 0:
        return nums[ind] == remaining_target

    if dp[ind][remaining_target] != -1:
        return dp[ind][remaining_target] == 1

    not_take = sub_array_sum_exists_rec_helper(ind-1, remaining_target, nums, dp)
    take = False
    if remaining_target >= nums[ind]:
        take = sub_array_sum_exists_rec_helper(ind-1, remaining_target-nums[ind], nums, dp)

    dp[ind][remaining_target] = take or not_take

    return dp[ind][remaining_target] == 1


def sub_array_sum_exists_tab(nums: List[int], k: int) -> bool:
    dp = [[-1 for _ in range(k + 1)] for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = True

    if nums[0] <= k:
        dp[0][nums[0]] = True

    for ind in range(len(nums)):
        for target in range(k+1):
            not_take = dp[ind - 1][target]
            take = False
            if target >= nums[ind]:
                take = dp[ind - 1][target - nums[ind]]
            if take == 1 or not_take == 1:
                dp[ind][target] = 1
            else:
                dp[ind][target] = 0
    return dp[len(nums)-1][k] == 1


def sub_array_sum_exists_tab_space_optimized(nums: List[int], k: int) -> bool:
    prev = [False] * (k + 1)

    prev[0] = True
    if nums[0] <= k:
        prev[nums[0]] = True

    for ind in range(1, len(nums)):
        curr = [False] * (k+1)
        curr[0] = True
        for target in range(1, k+1):
            not_take = prev[target]
            take = 0
            if target >= nums[ind]:
                take = prev[target - nums[ind]]
            curr[target] = take or not_take
        prev = [i for i in curr]

    return prev[k]


def sub_array_sum_k_count_tab(nums: List[int], k: int) -> int:
    prev = [0] * (k+1)

    prev[0] = 1
    if nums[0] <= k:
        prev[nums[0]] = prev[nums[0]] + 1

    for ind in range(1, len(nums)):
        curr = [0] * (k+1)
        for target in range(k+1):
            not_take = prev[target]
            take = 0
            if target >= nums[ind]:
                take = prev[target-nums[ind]]
            curr[target] = not_take + take
        prev = [i for i in curr]

    return prev[k]


if __name__ == "__main__":
    inp = [
        {"arr": [4, 3, 2, 1], "k": 5},
        {"arr": [2, 5, 1, 6, 7], "k": 4},
        {"arr": [0, 0, 1], "k": 1}
    ]
    for inp1 in inp:
        print(sub_array_sum_exists_rec(inp1["arr"], inp1["k"]))
        print(sub_array_sum_exists_tab(inp1["arr"], inp1["k"]))
        print(sub_array_sum_exists_tab_space_optimized(inp1["arr"], inp1["k"]))
        print(sub_array_sum_k_count_tab(inp1["arr"], inp1["k"]))

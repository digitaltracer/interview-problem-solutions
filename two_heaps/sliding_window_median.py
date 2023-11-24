# Created by Adarsh N B at 10/9/2023

# Description:
"""
Given an integer array, nums, and an integer, k, there is a sliding window of size k, which is moving from
the very left to the very right of the array. We can only see the k numbers in the window.
Each time the sliding window moves right by one position.
Given this scenario, return the median of each window

This solution is similar to that of the median of the data stream.
"""
from typing import List
from interview_problem_solutions.utils.max_heap import MaxHeap
from interview_problem_solutions.utils.min_heap import MinHeap


def median_sliding_window(nums: List[int], k: int) -> List[int]:
    max_half = MinHeap()  # this will be similar to the second half of the sorted list
    min_half = MaxHeap()  # this will be similar to the first half of the sorted list.
    medians = []

    window_last_position = k

    for i in range(k):
        min_half.insert(nums[i])

    for i in range(k//2):
        max_half.insert(min_half.pop())

    if k & 1:  # means k is odd
        medians.append(min_half.get_max())
    else:
        medians.append((min_half.get_max() + max_half.get_min())/2)

    # variable to store which heap has more elements
    balance = 0
    
    return medians

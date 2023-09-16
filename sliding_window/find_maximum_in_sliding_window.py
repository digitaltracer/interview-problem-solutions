# Created by Adarsh N B at 9/12/2023

# Description:
"""
Given an integer list `nums`, find the maximum values in all the contiguous sub-arrays (windows) of size `w`.
"""
from typing import List
from collections import deque


def cleanup(i, current_window, nums):
    try:
        while current_window and nums[i] >= nums[current_window[-1]]:
            current_window.pop()
    except BaseException as e:
        print(nums)
        print(current_window)
        print(i)
        print(e)


# function to find the maximum in all possible windows
def find_max_sliding_window(nums: List[int], w: int) -> List[int]:

    # lets address the boundary issues:
    # for empty array
    if len(nums) == 0:
        return []

    # if window size is greater than input size, adjust it to the length of list
    if w > len(nums):
        w = len(nums)

    output_list = []
    current_window = deque()

    # adding the first window to the current window
    for i in range(w):
        cleanup(i, current_window, nums)
        current_window.append(i)

    output_list.append(nums[current_window[0]])

    for i in range(w, len(nums)):
        cleanup(i, current_window, nums)

        if current_window and current_window[0] <= (i-w):
            print("Popping left")
            current_window.popleft()

        current_window.append(i)

        output_list.append(nums[current_window[0]])

    return output_list


if __name__ == "__main__":
    window_sizes = [3, 3, 3, 3, 2, 4, 3, 2, 3, 18]
    nums_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [1, 5, 8, 10, 10, 10, 12, 14, 15, 19, 19, 19, 17, 14, 13, 12, 12, 12, 14, 18, 22, 26, 26, 26, 28, 29, 30],
        [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67],
        [4, 5, 6, 1, 2, 3],
        [9, 5, 3, 1, 6, 3],
        [2, 4, 6, 8, 10, 12, 14, 16],
        [-1, -1, -2, -4, -6, -7],
        [4, 4, 4, 4, 4, 4]
    ]
    for i in range(len(nums_list)):
        print(f"{i + 1}.\tInput array:\t{nums_list[i]}")
        print(f"\tWindow size:\t{window_sizes[i]}")
        output = find_max_sliding_window(nums_list[i], window_sizes[i])
        print(f"\n\tMaximum in each sliding window:\t{output}")
        print("-"*100)

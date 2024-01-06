# Created by Adarsh N B at 12/16/2023

# Description:
"""
Given an array of integers, arr, and an integer, k, return the k most frequent elements.

Time complexity -
Space complexity - 
"""
from typing import List
from heapq import heappop, heappush


def top_k_frequent_elements(arr: List[int], k: int) -> List[int]:
    frequency_map = {}
    for num in arr:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    top_k_elements = []  # this will be used as min heap

    for num, frequency in frequency_map.items():
        heappush(top_k_elements, (frequency, num))

        if len(top_k_elements) > k:
            heappop(top_k_elements)

    top_elements = [i for _, i in top_k_elements]

    return top_elements


if __name__ == "__main__":
    inp = [1, 2, 3, 1, 2, 1, 1, 2, 4, 5]
    print(top_k_frequent_elements(inp, 1))

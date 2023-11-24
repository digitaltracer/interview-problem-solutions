# Created by Adarsh N B at 11/24/2023

# Description:
"""
Given a sorted list of non-overlapping intervals and a new interval, your task is to insert the new interval into the
correct position while ensuring that the resulting list of intervals remains sorted and non-overlapping.
Each interval is a pair of non-negative numbers, the first being the start time and the second being
the end time of the interval.
"""
from typing import List


def insert_interval(existing_intervals: List[List[int]], new_interval: List[List[int]]) -> List[List[int]]:
    if not existing_intervals:
        return new_interval

    if not new_interval:
        return existing_intervals

    new_interval_index = 0
    existing_interval_index = 0
    result = []

    while existing_intervals[existing_interval_index][0] < new_interval[0][0]:
        result.append(existing_intervals[existing_interval_index])
        existing_interval_index += 1

    for i in range(existing_interval_index, len(existing_intervals)):
        pass

    return result

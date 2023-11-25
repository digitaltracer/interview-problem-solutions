# Created by Adarsh N B at 11/24/2023

# Description:
"""
Given a sorted list of non-overlapping intervals and a new interval, your task is to insert the new interval into the
correct position while ensuring that the resulting list of intervals remains sorted and non-overlapping.
Each interval is a pair of non-negative numbers, the first being the start time and the second being
the end time of the interval.

Time complexity - O(n)
Space complexity - O(1)
"""
from typing import List


def insert_interval(existing_intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    if not existing_intervals:
        return [new_interval]

    if not new_interval:
        return existing_intervals

    existing_interval_index = 0
    result = []

    while existing_intervals[existing_interval_index][0] < new_interval[0]:
        result.append(existing_intervals[existing_interval_index])
        existing_interval_index += 1

    if not result or result[-1][1] < new_interval[0]:
        result.append(new_interval)

    else:
        result[-1][-1] = max(new_interval[-1], result[-1][-1])

    while existing_interval_index < len(existing_intervals):
        if result[-1][-1] > existing_intervals[existing_interval_index][0]:
            result[-1][-1] = max(result[-1][-1], existing_intervals[existing_interval_index][1])
        else:
            result.append(existing_intervals[existing_interval_index])
        existing_interval_index += 1

    return result


def main():
    new_interval = [[5, 7], [8, 9], [10, 12], [1, 3], [1, 10]]
    existing_intervals = [
        [[1, 2], [3, 5], [6, 8]],
        [[1, 3], [5, 7], [10, 12]],
        [[8, 10], [12, 15]],
        [[5, 7], [8, 9]],
        [[3, 5]]
    ]

    for i in range(len(new_interval)):
        print(i + 1, ".\tExiting intervals: ", existing_intervals[i], sep="")
        print("\tNew interval: ", new_interval[i], sep="")
        output = insert_interval(existing_intervals[i], new_interval[i])
        print("\tUpdated intervals: ", output, sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()

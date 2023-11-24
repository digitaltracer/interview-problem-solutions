# Created by Adarsh N B at 11/23/2023

# Description:
"""
We are given an array of *closed intervals* where each interval has a start time and an end time. The input array is
sorted with respect to the start times of each interval.
Your task is to merge the overlapping intervals and return a new output array consisting of only the
non-overlapping intervals.
"""
from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:

    result = []

    if not intervals:
        return result

    result.append(intervals[0])

    for i in range(1, len(intervals)):
        cur_interval = intervals[i]

        if cur_interval[0] <= result[-1][-1]:
            end_interval = max(cur_interval[-1], result[-1][-1])
            result[-1][-1] = end_interval
        else:
            result.append(cur_interval)

    return result


def main():
    all_intervals = [
        [[1, 5], [3, 7], [4, 6]],
        [[1, 5], [4, 6], [6, 8], [11, 15]],
        [[3, 7], [6, 8], [10, 12], [11, 15]],
        [[1, 5]],
        [[1, 9], [3, 8], [4, 4]],
        [[1, 2], [3, 4], [8, 8]],
        [[1, 5], [1, 3]],
        [[1, 5], [6, 9]],
        [[0, 0], [1, 18], [1, 3]]
    ]

    for i in range(len(all_intervals)):
        print(i + 1, ". Intervals to merge: ", all_intervals[i], sep="")
        result = merge_intervals(all_intervals[i])
        print("   Merged intervals:\t", result)
        print("-" * 100)


if __name__ == '__main__':
    main()

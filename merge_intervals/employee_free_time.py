# Created by Adarsh N B at 11/26/2023

# Description:
"""
You’re given a list containing the schedules of multiple employees. Each person’s schedule is a list of non-overlapping
intervals in sorted order. An interval is specified with the start and end time, both being positive integers.
Your task is to find the list of finite intervals representing the free time for all the employees.

Time complexity - O(nlogk) where k is the number of employees
"""
import heapq
from typing import List


class Interval:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Solution:

    @staticmethod
    def employee_free_time(schedule: List[List[Interval]]) -> List[Interval]:
        heap = []

        for person_index in range(len(schedule)):
            heap.append((schedule[person_index][0].start, i, 0))

        heapq.heapify(heap)

        result = []
        previous = schedule[heap[0][1]][heap[0][2]].start

        while heap:
            _, person_index, interval_index = heapq.heappop(heap)
            interval = schedule[person_index][interval_index]

            if interval.start > previous:
                result.append(Interval(previous, interval.start))

            previous = max(previous, interval.end)

            if interval_index + 1 < len(schedule[person_index]):
                heapq.heappush(heap, (schedule[person_index][interval_index + 1].start, person_index,
                                      interval_index + 1))

        return result

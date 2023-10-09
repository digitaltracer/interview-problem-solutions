# Created by Adarsh N B at 9/25/2023

# Description:
"""
Custom implementation of min heap using heapq
"""

from heapq import heappush, heappop


class MinHeap:
    def __init__(self):
        self.min_heap_list = []

    def insert(self, x):
        heappush(self.min_heap_list, x)

    def get_min(self):
        return self.min_heap_list[0]

    def pop(self):
        return heappop(self.min_heap_list)

    def __len__(self):
        return len(self.min_heap_list)

    def __str__(self):
        out = "["
        for i in self.min_heap_list:
            out += str(i) + ", "
        out = out[:-2] + "]"
        return out

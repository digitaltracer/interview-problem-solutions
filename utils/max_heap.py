# Created by Adarsh N B at 9/25/2023

# Description:
"""
Since python only supports min heap, adding this to support max heap to avoid duplication
"""
from heapq import *


class MaxHeap:

    def __int__(self):
        self.max_heap_list = []

    def insert(self, value):
        heappush(self.max_heap_list, -value)

    def get_max(self):
        return -self.max_heap_list[0]

    def __len__(self):
        return len(self.max_heap_list)

    def __str__(self):
        out = "["
        for i in self.max_heap_list:
            out += str(i) + ", "
        out = out[:-2] + "]"
        return out

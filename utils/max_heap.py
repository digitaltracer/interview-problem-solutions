# Created by Adarsh N B at 9/25/2023

# Description:
"""
Since python only supports min heap, adding this to support max heap to avoid duplication
"""
from heapq import heappush, heappop


class MaxHeap:

    def __init__(self):
        self.max_heap_list = []

    def insert(self, value):
        heappush(self.max_heap_list, -value)

    def get_max(self):
        return -self.max_heap_list[0]

    def pop(self):
        return -heappop(self.max_heap_list)

    def __len__(self):
        return len(self.max_heap_list)

    def __str__(self):
        out = "["
        for i in self.max_heap_list:
            out += str(i) + ", "
        out = out[:-2] + "]"
        return out


if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5]
    max_heap = MaxHeap()
    for i in sample_list:
        max_heap.insert(i)

    print(max_heap.get_max())

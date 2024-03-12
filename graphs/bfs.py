# Created by Adarsh N B at 3/6/2024

# Description:
"""

Time complexity - O(n) + O(2E)  (total number of degrees is equal to twice the number of edges)
Space complexity - O(n)
"""
from typing import List
from queue import Queue


def breadth_first_traversal(size: int, adjacency_list: List[List[int]]) -> List[int]:

    visited_nodes = set()
    # assuming the start node is given as 1
    visited_nodes.add(1)
    q = Queue()
    q.put(1)
    bfs = [1]

    while not q.empty():
        node = q.get()

        adjacent_nodes = adjacency_list[node]
        for an in adjacent_nodes:
            if an not in visited_nodes:
                q.put(an)
                visited_nodes.add(an)
                bfs.append(an)

    return bfs

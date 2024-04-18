# Created by Adarsh N B at 4/10/2024

# Description:
"""
LC 547
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b and
city b is connected directly with city c, then city a is indirectly connected with city c

A province is a group of directly or indirectly connected cities and no other cities outside the group.

You are given a `n x n` matrix `is_connected` where `is_connected[i][j] = 1` if the ith city and jth city are
directly connected and `isConnected[i][j] = 0` otherwise.
Return the total number of provinces
Time complexity - O(n**2)
Space complexity - O(n)
"""
from typing import List
from queue import Queue

"""
The logic here is to loop through entire nodes (from 0 to n-1) and start dfs traversal from each of the nodes
**if** that node is already not traversed from the previous traversals. This 
"""


def find_circle_num(is_connected: List[List[int]]) -> int:
    number_of_nodes = len(is_connected)
    visited_array = [False] * number_of_nodes

    number_of_provinces = 0

    for node in range(number_of_nodes):
        if visited_array[node] is False:
            number_of_provinces += 1
            dfs(is_connected, node, visited_array)
    return number_of_provinces


def dfs(is_connected: List[List[int]], node: int, visited_array: List[int]) -> None:
    visited_array[node] = True
    for neighbor in range(len(is_connected)):
        if is_connected[node][neighbor] and visited_array[neighbor] is False:
            visited_array[neighbor] = True
            dfs(is_connected, neighbor, visited_array)


def find_circle_num_bfs(is_connected: List[List[int]]) -> int:
    number_of_nodes = len(is_connected)
    visited_array = [False] * number_of_nodes
    number_of_provinces = 0

    for node in range(number_of_nodes):
        if visited_array[node] is False:
            number_of_provinces += 1
            # start bfs
            q = Queue()
            q.put(node)
            visited_array[node] = True
            while not q.empty():
                cur_node = q.get()
                for nb in range(number_of_nodes):
                    if is_connected[cur_node][nb] and visited_array[nb] is False:
                        visited_array[nb] = True
                        q.put(nb)
    return number_of_provinces


if __name__ == "__main__":
    connected_graphs = [[[1, 1, 0], [1, 1, 0], [0, 0, 1]],
                        [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                        [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]]
    for cg in connected_graphs[2:]:
        print(find_circle_num(cg))
        print(find_circle_num_bfs(cg))

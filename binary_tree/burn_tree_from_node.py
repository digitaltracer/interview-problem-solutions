# Created by Adarsh N B at 2/27/2024

# Description:
"""
Given a node/node value, return the maximum time taken to burn the entire tree starting from that node.
Time complexity - 
Space complexity - 
"""
from queue import Queue
from interview_problem_solutions.utils.tree import Node


def map_parents(root: Node, mapping: dict, node_value: int) -> Node:
    q = Queue()
    req_node = None
    q.put(root)

    while not q.empty():
        q_size = q.qsize()
        for _ in range(q_size):
            cur_node = q.get()

            if cur_node.left:
                q.put(cur_node.left)
                mapping[cur_node.left] = cur_node

            if cur_node.right:
                q.put(cur_node.right)
                mapping[cur_node.right] = cur_node

            if cur_node.data == node_value:
                req_node = cur_node

    return req_node


def find_max_distance(target: Node, parent_mapping: dict) -> int:
    distance = 0
    visited = set()
    q = Queue()
    q.put(target)

    while not q.empty():
        q_size = q.qsize()
        cur_node = q.get()
        burnt_flag = 0
        for _ in range(q_size):
            if cur_node.left and cur_node.left not in visited:
                q.put(cur_node.left)
                visited.add(cur_node.left)
                burnt_flag = 1
            if cur_node.right and cur_node.right not in visited:
                q.put(cur_node.right)
                visited.add(cur_node.right)
                burnt_flag = 1
            if parent_mapping.get(cur_node) and parent_mapping[cur_node] not in visited:
                q.put(cur_node.get(cur_node))
                visited.add(parent_mapping[cur_node])
                burnt_flag = 1

        if burnt_flag:
            distance += 1

    return distance


def solution(root: Node, target: int) -> int:
    parents_mapping = {}
    target_node = map_parents(root, parents_mapping, target)
    return find_max_distance(target_node, parents_mapping)

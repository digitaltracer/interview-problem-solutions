# Created by Adarsh N B at 2/26/2024

# Description:
"""
Given a node, print all the nodes that are a distance k from this node
Time complexity - 
Space complexity - 
"""
from typing import List
from queue import Queue
from interview_problem_solutions.utils.tree import Node


def map_nodes_to_parents(root: Node, mapping: dict):
    q = Queue()

    q.put(root)

    while not q.empty():
        q_size = q.qsize()

        for _ in range(q_size):
            cur_node = q.get()

            if cur_node.left:
                mapping[cur_node.left] = cur_node
                q.put(cur_node.left)

            if cur_node.right:
                mapping[cur_node.right] = cur_node
                q.put(cur_node.right)


def distance_k(root: Node, target: Node, k: int) -> List[int]:
    res = []
    q = Queue()
    q.put(target)

    cur_level = 0
    while cur_level != k:
        pass
    return res

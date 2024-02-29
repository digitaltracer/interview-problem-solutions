# Created by Adarsh N B at 2/14/2024

# Description:
"""
"""
from queue import Queue
from typing import List


class Node:

    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


def level_order_traversal(node: Node):
    ans = []
    if node is None:
        return ans
    queue = Queue()
    queue.put(node)

    queue.qsize()

    while queue.not_empty:
        cur_level_elements = []
        for i in range(queue.qsize()):
            el: Node = queue.get()
            cur_level_elements.append(el.data)

            if el.left:
                queue.put(el.left)
            if el.right:
                queue.put(el.right)
        ans.append(cur_level_elements)

    return ans


def pre_order_recursion(node: Node):

    print(node.data)
    if node.left:
        pre_order_recursion(node.left)
    if node.right:
        pre_order_recursion(node.right)


def in_order_recursion():
    pass

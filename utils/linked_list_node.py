# Created by Adarsh N B at 9/6/2023

# Description:
"""
Template for linked list node
"""


class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

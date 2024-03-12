# Created by Adarsh N B at 3/6/2024

# Description:
"""
Check whether a linked list contains a cycle. If a cycle exists, return TRUE. Otherwise, return FALSE.
The cycle means that at least one node can be reached again by traversing the next pointer.
Time complexity - O(n)
Space complexity - O(1)
"""
from interview_problem_solutions.utils.linked_list import LinkedListNode, LinkedList


def detect_cycle(head: LinkedListNode) -> bool:

    slow_pointer: LinkedListNode = head
    fast_pointer: LinkedListNode = head.next

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            return True

    return False

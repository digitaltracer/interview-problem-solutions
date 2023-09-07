# Created by Adarsh N B at 9/7/2023

# Description:
"""
Reverse a linked list using O(1) memory
"""
from interview_problem_solutions.utils.linked_list import LinkedList
from interview_problem_solutions.utils.linked_list_node import LinkedListNode
from interview_problem_solutions.utils.print_linked_list import print_list_with_forward_arrow


def reverse_linked_list(linked_list: LinkedList) -> LinkedList:
    # print_list_with_forward_arrow(linked_list.head)
    curr: LinkedListNode = linked_list.head
    prev = None
    nxt = None

    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt

    linked_list.head = prev

    return linked_list


if __name__ == "__main__":
    lists = (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1],
        [10],
        [1, 2],
    )

    for i in lists:
        linkd_list = LinkedList()
        linkd_list.create_linked_list(i)
        print_list_with_forward_arrow(reverse_linked_list(linkd_list).head)
        print()

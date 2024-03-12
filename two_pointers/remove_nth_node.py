# Created by Adarsh N B at 9/6/2023

# Description:
"""
Given a singly linked list, remove the nth node from the end of the list and return its head.

If n is more than the length of the list, throw an error.

Time complexity: O(n)
Space complexity: O(1)
"""

from interview_problem_solutions.utils.linked_list import LinkedList
from interview_problem_solutions.utils.linked_list_node import LinkedListNode
from interview_problem_solutions.utils.print_linked_list import print_list_with_forward_arrow

"""
1. Two pointers, right and left, are set at the head node.
2. Move the right pointer n steps forward.
3. If right reaches NULL, return head's next node.
4. Move both right and left pointers forward till right reaches the last node.
5. Relink the left node to the node at left's next to the next node.
6. Return head.
"""


def remove_nth_last_node(linked_list: LinkedList, n) -> LinkedList:

    if linked_list.size < n-1:
        raise IndexError(f"Provided number is higher than the length of linked list.")

    head: LinkedListNode = linked_list.head
    left = head
    right = head

    # move n steps for the right pointers
    for _ in range(n):
        right = right.next

    if not right:
        return head.next

    # move both left and right pointers
    while right.next is not None:
        left = left.next
        right = right.next

    left.next = left.next.next
    return linked_list


if __name__ == "__main__":
    lists = [[23, 89, 10, 5, 67, 39, 70, 28], [34, 53, 6, 95, 38, 28, 17, 63, 16, 76],
             [288, 224, 275, 390, 4, 383, 330, 60, 193],
             [1, 2, 3, 4, 5, 6, 7, 8, 9], [69, 8, 49, 106, 116, 112, 104, 129, 39, 14, 27, 12]]
    n = [4, 1, 6, 8, 11]
    for index, llist in enumerate(lists):
        linked_list = LinkedList()
        linked_list.create_linked_list(llist)
        remove_nth_last_node(linked_list, n[index])
        print_list_with_forward_arrow(linked_list.head)
        print("\n")

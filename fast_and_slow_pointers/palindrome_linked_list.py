# Created by Adarsh N B at 3/6/2024

# Description:
"""
Given the head of a linked list, your task is to check whether the linked list is a palindrome or not.
Return TRUE if the linked list is a palindrome; otherwise, return FALSE.

Time complexity - O(n)
Space complexity - O(1)
"""

from interview_problem_solutions.utils.linked_list import LinkedList, LinkedListNode
from interview_problem_solutions.utils.print_linked_list import print_list_with_forward_arrow


def reverse_linked_list(head: LinkedListNode) -> LinkedListNode:
    curr = head
    prev = nxt = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt

    return prev


def palindrome(head: LinkedListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    rev = reverse_linked_list(slow)

    print("\t")
    print_list_with_forward_arrow(head)

    return compare_two_halves(head, rev)


def compare_two_halves(first_half: LinkedListNode, second_half: LinkedListNode) -> bool:
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False

        else:
            first_half = first_half.next
            second_half = second_half.next
    return True


if __name__ == "__main__":
    inp = (
                [2, 4, 6, 4, 2],
                [0, 3, 5, 5, 0],
                [9, 7, 4, 4, 7, 9],
                [5, 4, 7, 9, 4, 5],
                [5, 9, 8, 3, 8, 9, 5],
            )
    j = 1

    for i in range(len(inp)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(inp[i])
        print(j, ".\tLinked List:", end=" ", sep="")
        print_list_with_forward_arrow(input_linked_list.head)
        head = input_linked_list.head
        print("\n\tIs it a palindrome?", "Yes" if palindrome(head) else "No")
        j += 1
        print("-"*100, "\n")

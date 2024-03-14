# Created by Adarsh N B at 3/6/2024

# Description:
"""
An input array, nums containing non-zero integers, is given, where the value at each index represents the number of
places to skip forward (if the value is positive) or backward (if the value is negative). When skipping forward or
backward, wrap around if you reach either end of the array. For this reason, we are calling it a circular array.
Determine if this circular array has a cycle. A cycle is a sequence of indices in the circular array characterized by the following:

The same set of indices is repeated when the sequence is traversed in accordance with the aforementioned rules.
The length of the sequence is at least two.
The loop must be in a single direction, forward or backward.
Time complexity - O(n**2)
Space complexity - O(1)
"""
from typing import List
"""
If the values at the array indexes of the slow and fast pointers have different signs, i.e., one pointer is pointing 
to a positive value, and the other is pointing to a negative value, the loop cannot exist
"""


# This function only proves negative. which doesn't mean that if it returns false, it is a cycle
# Here direction is being represented by boolean. True means ahead(positive value)
def is_not_cycle(nums: List[int], curr_index: int, prev_direction: bool) -> bool:
    curr_direction = nums[curr_index] >= 0

    if curr_direction != prev_direction or nums[curr_index] % len(nums) == 0:
        return True

    return False


def next_step(curr_value: int, curr_index: int, size: int) -> int:
    next_index = (curr_index + curr_value) % size

    if next_index < 0:
        next_index += size
    return next_index


def circular_array_loop(nums: List[int]) -> bool:

    size = len(nums)

    for i in range(size):
        fast = slow = i
        direction = nums[i] > 0

        while True:
            slow = next_step(nums[slow], slow, size)

            if is_not_cycle(nums, slow, direction):
                break

            fast = next_step(nums[fast], fast, size)

            if is_not_cycle(nums, fast, direction):
                break

            fast = next_step(nums[fast], fast, size)

            if is_not_cycle(nums, fast, direction):
                break

            if fast == slow:
                return True

    return False


if __name__ == "__main__":
    print(circular_array_loop([3, 1, 3]))

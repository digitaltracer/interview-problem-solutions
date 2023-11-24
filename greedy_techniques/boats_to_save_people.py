# Created by Adarsh N B at 11/21/2023

# Description:
"""
We are given an array, people, where people[i] is the weight of the i th person, and an infinite number of boats,
 where each boat can carry a maximum weight, limit. Each boat carries, at most, two people at the same time.
This is provided that the sum of the weight of these people is under or equal to the weight limit.

Time complexity - O(n logn) -- ( O(nlogn) + O(n) => O(nlogn) ) since sorting takes O(nlogn)
Space complexity -
"""
from typing import List


def boats_to_save_people(nums: List[int], limit: int) -> int:
    nums.sort()

    # The assumption is that the limit is lesser or equal to the heaviest member in the nums

    boats = 0

    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer <= right_pointer:
        if nums[left_pointer] + right_pointer <= limit:
            left_pointer += 1

        # if heaviest + lightest member cannot, then just board the heaviest member
        right_pointer -= 1

        boats += 1

    return boats


def main():
    people = [[1, 2], [3, 2, 2, 1], [3, 5, 3, 4], [
        5, 5, 5, 5], [1, 2, 3, 4], [1, 2, 3], [3, 4, 5]]
    limit = [3, 3, 5, 5, 5, 3, 5]
    for i in range(len(people)):
        print(i + 1, "\tWeights = ", people[i], sep="")
        print("\tWeight Limit = ", limit[i], sep="")
        print("\tThe minimum number of boats required to save people are ",
              boats_to_save_people(people[i], limit[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()

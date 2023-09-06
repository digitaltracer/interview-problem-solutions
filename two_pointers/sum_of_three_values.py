# Created by Adarsh N B at 9/6/2023

# Description:
"""
Given a list/array and a target number,
 say whether by adding 3 different elements of the list can we achieve the target given.

 We are going to solve using the 2 pointers approach.
"""


def sum_of_three_numbers(numbers: list[int], target: int) -> bool:
    # two pointers will work only on sorted list
    numbers.sort()
    length_of_list = len(numbers)
    for i in range(0, len(numbers)-2):
        low = i+1
        high = length_of_list - 1

        while low < high:
            triplet_sum = numbers[i] + numbers[low] + numbers[high]

            if triplet_sum == target:
                print(f"{numbers[i]} + {numbers[low]} + {numbers[high]}")
                return True

            if triplet_sum < target:
                low += 1

            else:
                high -= 1
    return False


if __name__ == "__main__":
    nums_lists = [[3, 7, 1, 2, 8, 4, 5],
                  [-1, 2, 1, -4, 5, -3],
                  [2, 3, 4, 1, 7, 9],
                  [1, -1, 0],
                  [2, 4, 2, 7, 6, 3, 1]]

    targets = [10, 7, 20, -1, 8]

    for index, numbers in enumerate(nums_lists):
        print(f"Input - {numbers}  -- Target - {targets[index]}")
        print(f"Result - {sum_of_three_numbers(numbers, targets[index])}")

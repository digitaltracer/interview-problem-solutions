# Created by Adarsh N B at 3/5/2024

# Description:
"""
Given an array `colors`, which contains a combination of the following three elements:

- 0 (representing red)
- 1 (representing white)
- 2 (representing blue)

Sort the array in place so that the elements of the same color are adjacent, with the colors in the order of red, white, and blue.

The function should only return the modified `colors` array (in place sorting)

Time complexity - O(n)
Space complexity - O(1)
"""
from typing import List


def sort_colors(colors: List[int]) -> List[int]:

    # first step is to initiate the pointers
    white = red = 0
    blue = len(colors) - 1

    while white <= blue:
        # let's check all the 3 possible options
        if colors[white] == 0:
            if colors[red] != 0:
                colors[white], colors[red] = colors[red], colors[white]

            # now that both are sorted, increment both the pointers
            white += 1
            red += 1

        elif colors[white] == 1:
            # that is what is expected of the white pointer. just move on to the next index
            white += 1

        else:
            if colors[blue] != 2:
                colors[blue], colors[white] = colors[white], colors[blue]

            # we don't care about what the blue pointer value holds. So, just decreasing the blue counter after
            # making sure the blue pointer is pointing to blue value, decreasing the pointer
            blue -= 1

    return colors


if __name__ == "__main__":
    inputs = [[0, 1, 0], [1, 1, 0, 2], [2, 1, 1, 0, 0], [2, 2, 2, 0, 1, 0], [2, 1, 1, 0, 1, 0, 2]]

    for i in range(len(inputs)):
        print(i + 1, ".\tcolors:", inputs[i].copy(),
              "\n\n\tThe sorted array is:", sort_colors(inputs[i]))
        print("-" * 100)

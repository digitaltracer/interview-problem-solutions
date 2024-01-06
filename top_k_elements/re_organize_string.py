# Created by Adarsh N B at 12/11/2023

# Description:
"""
Given a string, `string`, rearrange it so that any two adjacent characters are not the same. If such a reorganization of the
characters is possible, output any possible valid arrangement. Otherwise, return an empty string.

Time complexity - O(nlogc)  . where c is number of distinct characters in the string
Space complexity - O(1) . Because maximum number of elements in heap or frequency map is 26
"""
import heapq
from collections import Counter


def reorganize_string(string: str) -> str:
    frequency = []
    result = ""

    counter = Counter(string)
    for char, count in counter.items():
        frequency.append([-count, char])

    heapq.heapify(frequency)

    previous = None

    while len(frequency) > 0 or previous:
        char_count, char = heapq.heappop(frequency)
        result += char

        char_count += 1  # we are adding one as we converted the count to -ve

        if previous:
            # we are pushing it in the same iteration of the loop as the next pop might give the same character.
            heapq.heappush(frequency, previous)
            previous = None

        if char_count != 0:
            previous = [char_count, char]

    return result


def main():
    test_cases = ["programming", "hello", "fofjjb",
                  "abbacdde", "aba", "awesome", "aaab"]
    for i in range(len(test_cases)):
        print(i+1, '. \tInput string: "', test_cases[i], '"', sep="")
        temp = reorganize_string(test_cases[i])
        print('\tReorganized string: "', temp + '"' if temp else '"', sep="")
        print("-"*100)


if __name__ == '__main__':
    main()

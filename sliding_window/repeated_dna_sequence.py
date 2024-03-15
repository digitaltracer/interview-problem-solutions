# Created by Adarsh N B at 9/6/2023

# Description:
"""
Given a string `s` and a number `k` find all the substrings of length `k` that occurs more than once in `s`
"""


def find_repeated_sequences(s: str, k: int) -> set[str]:
    """
    This is the naive approach. With this we get time complexity of O((n-k)*k) with the same space complexity as well.
    since in the worst case, our set can contain (n−k+1) elements, and at each iteration of the traversal,
    we are allocating memory to generate a new k-length substring.
    """
    all_substrings = set()
    repeated_substrings = set()
    string_length = len(s)

    left_index = 0
    right_index = k

    while right_index < string_length:
        sub_str = s[left_index: right_index]
        if sub_str in all_substrings:
            repeated_substrings.add(sub_str)
        else:
            all_substrings.add(sub_str)
        left_index += 1
        right_index += 1

    return repeated_substrings


"""
The performance can be improved to O(n) TC and SC by using Rabin-Karp algorithm that utilizes sliding window with
rolling hash for pattern matching. Rolling hash is used to prevent rehashing the whole string while calculating hash 
values of the substrings of a given string.
"""


if __name__ == "__main__":
    inputs_string = ["ACGT", "AGACCTAGAC", "AAAAACCCCCAAAAACCCCCC", "GGGGGGGGGGGGGGGGGGGGGGGGG",
                     "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", "TTTTTGGGTTTTCCA",
                     "AAAAAACCCCCCCAAAAAAAACCCCCCCTG", "ATATATATATATATAT"]
    inputs_k = [3, 3, 8, 12, 10, 14, 10, 6]

    for i in range(len(inputs_k)):
        print(i + 1, ".\tInput Sequence: \'", inputs_string[i], "\'", sep="")
        print("\tk: ", inputs_k[i], sep="")
        print()
        find_repeated_sequences(inputs_string[i], inputs_k[i])
        print("-" * 100)

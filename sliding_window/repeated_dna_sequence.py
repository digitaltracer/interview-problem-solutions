# Created by Adarsh N B at 9/6/2023

# Description:
"""
Given a string `s` and a number `k` find all the substrings of length `k` that occurs more than once in `s`
"""


def find_repeated_sequences(s: str, k: int) -> set[str]:
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


if __name__ == "__main__":
    pass

# Created by Adarsh N B at 11/16/2023

# Description:
"""
Given an input string, return all possible permutations of the string.

Time complexity - O(n!)
Space complexity - O(n)
n -> length of the string
"""
from typing import List


"""
Let's explain the logic with an example of input [1, 2, 3]
we will start swapping characters/int for each positions
Let's start at index 0, we start by swapping 1 with 1 and then 1 with 2 and then 1 with 3
that will give us [1, 2, 3] , [2, 1, 3] and [3, 2, 1] and the pointer at index 1
Now, consider the first one [1, 2, 3] (at index 1), we start by swapping 2 with 2 and then 2 with 3 and so on.
"""


def swap_char(word: str, first_index: int, second_index: int) -> str:
    word_list = [i for i in word]
    word_list[first_index], word_list[second_index] = word_list[second_index], word_list[first_index]

    return ''.join(word_list)


def permute_string_rec(word: str, cur_index: int, result: List[str]) -> None:

    # base case to stop recursion
    if cur_index == len(word) - 1:
        result.append(word)
        return

    for i in range(cur_index, len(word)):
        changed_word = swap_char(word, cur_index, i)
        permute_string_rec(changed_word, cur_index+1, result)


def permute_word(word):
    result = []

    # Starts finding permutations from start of string
    permute_string_rec(word, 0, result)

    return result


if __name__ == "__main__":
    input_words = ["ab", "bad", "abcd"]

    for index in range(len(input_words)):
        permuted_words = permute_word(input_words[index])

        print(index + 1, ".\t Input string: '", input_words[index], "'", sep="")
        print("\t All possible permutations are: ",
              "[", ', '.join(permuted_words), "]", sep="")
        print('-' * 100)

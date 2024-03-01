# Created by Adarsh N B at 11/16/2023

# Description:
"""
Given an input string, return all possible permutations of the string.

Time complexity - O(n!)
Space complexity - O(n)
n -> length of the string
"""
from typing import List


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

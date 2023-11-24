# Created by Adarsh N B at 11/17/2023

# Description:
"""
Given a string containing digits from 2 to 9 inclusive, return all possible letter combinations that the number could
represent. Return the answer in any order.

n -> number of input digits
k -> max number of letters associated with any given digits

Time complexity -> O(n * k**n)
Space complexity -> O(n*k)
"""
from typing import List, Dict


def backtrack(index: int, path: List[str], digits: str,
              digits_mapping: Dict[str, List[str]], combinations: List[str]) -> None:

    if len(path) == len(digits):
        combinations.append(''.join(path))
        return

    possible_letters = digits_mapping[digits[index]]

    for letter in possible_letters:
        path.append(letter)

        backtrack(index + 1, path, digits, digits_mapping, combinations)
        # remove the current added letter for the next letter of the same index
        path.pop()


def letter_combinations(digits):
    combinations = []

    # If the input is empty, immediately return an empty answer array
    if len(digits) == 0:
        return []

    #  Mapping the digits to their corresponding letters
    digits_mapping = {
        "1": [],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]}

    # Initiate backtracking with an empty path and starting index of 0

    backtrack(0, [], digits, digits_mapping, combinations)
    return combinations


def main():
    digits_array = ["23", "73", "426", "78", "925", "2345", "98"]
    counter = 1
    for digits in digits_array:
        print(counter, ".\t All letter combinations for '",
              digits, "': ", letter_combinations(digits), sep="")
        counter += 1
        print("-" * 100)


if __name__ == "__main__":
    main()

# Created by Adarsh N B at 9/20/2023

# Description:
"""
Given two strings `str1` and `str2`, find the shortest substring in `str1` such that `str2` is a subsequence
of that substring.
"""


def min_window(str1: str, str2: str) -> str:

    size_str1, size_str2 = len(str1), len(str2)

    min_sub_length = float('inf')

    min_sub_str = ""

    index_str1, index_str2 = 0, 0

    start, end = 0, 0

    while index_str1 < size_str1:

        if str1[index_str1] == str2[index_str2]:
            index_str2 += 1

            if index_str2 == 0:
                start = index_str1

            if index_str2 == size_str2:
                # we need to restart checking from the beginning of the string
                end = index_str1

                if min_sub_length > (end - start) + 1:
                    min_sub_length = (end - start) + 1
                    min_sub_str = str1[start: end+1]

                index_str2 = 0

        index_str1 += 1
    return min_sub_str


if __name__ == "__main__":
    str1 = ["abcdebdde", "fgrqsqsnodwmxzkzxwqegkndaa", "zxcvnhss", "alpha", "beta"]
    str2 = ["bde", "kzed", "css", "la", "ab"]

    for i in range(len(str1)):
        print(i+1, ". \tInput string: (" + str1[i]+", " + str2[i]+")", sep="")
        print("\tSubsequence string: ", min_window(str1[i], str2[i]))
        print("-"*100)

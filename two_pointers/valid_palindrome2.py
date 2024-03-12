# Created by Adarsh N B at 3/5/2024

# Description:
"""

Time complexity - 
Space complexity - 
"""


def is_palindrome(s):
    # Replace this placeholder return statement with your code
    left = 0
    right = len(s) - 1
    invalids_count = 0
    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        elif invalids_count == 0:
            right -= 1
            invalids_count += 1
        else:
            return False

    return True


if __name__ == "__main__":
    is_palindrome()

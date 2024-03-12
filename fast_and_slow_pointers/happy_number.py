# Created by Adarsh N B at 3/5/2024

# Description:
"""
Write an algorithm to determine if a number n is a happy number.
Return TRUE if n is a happy number, and FALSE if not.

In number theory, a happy number is a number which eventually reaches 1 when
replaced by the sum of the square of each digit.
Time complexity - O(log n)
Space complexity - O(1)
"""

"""
Brute force approach is to calculate the sum of squared numbers and store it in a hash set. For every calculation,
if the sum is already present in the hash set then we have detected a cycle

While this approach works well for small numbers, we might have to perform several computations for larger numbers to 
get the required result. So, it might get infeasible for such cases. The time complexity of this approach is  O(log n). 
The space complexity is O(log n) since we're using additional space to store our calculated sums.

If we use the fast and slow pointers approach here, the fast pointer would eventually reach 1, in which case
we will return TRUE. Otherwise, it would meet the slow pointer, which would mean that the two pointers are in an endless
loop, and we can return FALSE.
"""


def sum_of_squared_digits(number: int) -> int:
    total_sum = 0
    while number > 0:
        number, digit = divmod(number, 10)
        total_sum += digit ** 2
    return total_sum


def is_happy_number(num: int) -> bool:
    slow_pointer = num
    fast_pointer = sum_of_squared_digits(num)

    number_of_loops = 0

    while fast_pointer != 1 and slow_pointer != fast_pointer:
        number_of_loops += 1
        slow_pointer = sum_of_squared_digits(slow_pointer)
        fast_pointer = sum_of_squared_digits(sum_of_squared_digits(fast_pointer))

    print(number_of_loops)
    if fast_pointer == 1:
        return True
    return False


if __name__ == "__main__":
    inputs = [1, 5, 19, 25, 7]
    for i in range(len(inputs)):
        print(i + 1, ".\tInput Number: ", inputs[i], sep="")
        print("\n\tIs it a happy number? ", is_happy_number(inputs[i]))
        print("-" * 100)

"""
This is to decide if a number is a happy number.
A number is called a happy number -> Starting with the given number n, replace the number with the sum of the squares
of its digits without entering into a loop the sum will be 1
"""


def sum_of_squared_digits(number: int) -> int:
    total_sum = 0
    for digit in str(number):
        total_sum += int(digit)**2
    return total_sum


def is_happy_number(number: int) -> bool:
    slow_pointer = number
    fast_pointer = sum_of_squared_digits(number)

    number_of_loops = 0
    while fast_pointer != 1 and fast_pointer != slow_pointer:
        number_of_loops += 1
        slow_pointer = sum_of_squared_digits(slow_pointer)
        fast_pointer = sum_of_squared_digits(sum_of_squared_digits(fast_pointer))

    print(f"Number of loops for {number} is {number_of_loops}")
    if fast_pointer == 1:
        return True
    return False


if __name__ == "__main__":
    sample_numbers = [1, 5, 19, 25, 7]
    for num in sample_numbers:
        print(f"Started calculating for {num}")
        result_text = "is" if is_happy_number(num) else "is not"
        print(f"{num} {result_text} a happy number")

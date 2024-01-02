
def count_nums(arr):
    """Counts the elements in the array with a sum of digits greater than 0."""

    count = 0
    for num in arr:
        sum_of_digits = 0
        is_negative = False

        if num < 0:
            is_negative = True
            num = -num  # Handle negative numbers by making them positive first

        while num > 0:
            digit = num % 10
            sum_of_digits += digit
            num //= 10

        if is_negative:  # Adjust the sum for negative numbers
            sum_of_digits = -sum_of_digits

        if sum_of_digits > 0:
            count += 1

    return count

def check(count_nums):
    # Check some simple cases
    assert count_nums([]) == 0
    assert count_nums([-1, -2, 0]) == 0
    assert count_nums([1, 1, 2, -2, 3, 4, 5]) == 6
    assert count_nums([1, 6, 9, -6, 0, 1, 5]) == 5
    assert count_nums([1, 100, 98, -7, 1, -1]) == 4
    assert count_nums([12, 23, 34, -45, -56, 0]) == 5
    assert count_nums([-0, 1**0]) == 1
    assert count_nums([1]) == 1

    # Check some edge cases that are easy to work out by hand.
    assert True

check(count_nums)

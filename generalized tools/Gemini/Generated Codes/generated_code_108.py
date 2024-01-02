
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

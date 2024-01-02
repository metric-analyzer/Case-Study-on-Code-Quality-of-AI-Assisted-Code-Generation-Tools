
def rounded_avg(n, m):
    """
    Calculates the rounded average of integers from n to m, inclusive, and returns it as a binary string.

    Args:
        n: The lower bound of the range.
        m: The upper bound of the range.

    Returns:
        A binary string representing the rounded average, or "-1" if n is greater than m.
    """

    if n > m:
        return "-1"

    sum_of_numbers = sum(range(n, m + 1))  # Calculate the sum of integers in the range
    average = round(sum_of_numbers / (m - n + 1))  # Calculate the average and round to nearest integer
    binary_string = f"0b{average:b}"  # Convert the rounded average to binary string
    return binary_string

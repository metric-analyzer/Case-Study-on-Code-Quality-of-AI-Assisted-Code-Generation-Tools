
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


def check(rounded_avg):
    assert rounded_avg(1, 5) == "0b11", "Test 1"
    assert rounded_avg(7, 13) == "0b1010", "Test 2"
    assert rounded_avg(964, 977) == "0b1111001010", "Test 3"
    assert rounded_avg(996, 997) == "0b1111100100", "Test 4"
    assert rounded_avg(560, 851) == "0b1011000010", "Test 5"
    assert rounded_avg(185, 546) == "0b101101110", "Test 6"
    assert rounded_avg(362, 496) == "0b110101101", "Test 7"
    assert rounded_avg(350, 902) == "0b1001110010", "Test 8"
    assert rounded_avg(197, 233) == "0b11010111", "Test 9"

# Check some edge cases that are easy to work out by hand.
assert rounded_avg(7, 5) == -1, "Edge Test 1"
assert rounded_avg(5, 1) == -1, "Edge Test 2"
assert rounded_avg(5, 5) == "0b101", "Edge Test 3"

check(rounded_avg)

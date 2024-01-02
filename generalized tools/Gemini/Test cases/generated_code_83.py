
def starts_one_ends(n):
    """
    Counts the n-digit positive integers that start or end with 1.

    Args:
        n: The number of digits.

    Returns:
        The count of n-digit numbers starting or ending with 1.
    """

    total_numbers = 10 ** n  # Total possible n-digit numbers
    numbers_not_starting_or_ending_with_1 = 8 * 9 ** (n - 2)  # Fixed middle digits, excluding 1
    return total_numbers - numbers_not_starting_or_ending_with_1


def check(starts_one_ends):
    # Check some simple cases
    assert starts_one_ends(1) == 1, "Test 1"
    assert starts_one_ends(2) == 18, "Test 2"
    assert starts_one_ends(3) == 180, "Test 3"
    assert starts_one_ends(4) == 1800, "Test 4"
    assert starts_one_ends(5) == 18000, "Test 5"

check(starts_one_ends)

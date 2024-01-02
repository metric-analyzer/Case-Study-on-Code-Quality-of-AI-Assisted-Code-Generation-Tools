
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

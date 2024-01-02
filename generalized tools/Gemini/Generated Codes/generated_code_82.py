
def prime_length(string):
    """
    Determines if the length of a string is a prime number.

    Args:
        string: The input string.

    Returns:
        True if the length of the string is prime, False otherwise.
    """

    string_length = len(string)

    if string_length <= 1:
        return False  # 1 and 0 are not prime

    for divisor in range(2, int(string_length**0.5) + 1):
        if string_length % divisor == 0:
            return False  # Found a divisor, not prime

    return True  # No divisors found, prime

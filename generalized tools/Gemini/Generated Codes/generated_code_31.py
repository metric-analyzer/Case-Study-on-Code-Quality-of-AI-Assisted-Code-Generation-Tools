
def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n: The number to be checked.

    Returns:
        True if the number is prime, False otherwise.
    """

    if n <= 1:
        return False  # 1 or less is not prime
    if n <= 3:
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False  # Multiples of 2 and 3 are not prime

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

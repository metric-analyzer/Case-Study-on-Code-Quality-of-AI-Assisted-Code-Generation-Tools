
def largest_divisor(n: int) -> int:
    """Finds the largest divisor of a number n, smaller than n."""

    largest_div = 1  # Initialize largest divisor to 1
    for i in range(2, n // 2 + 1):  # Iterate from 2 up to n/2
        if n % i == 0:  # Check if i is a divisor of n
            largest_div = i  # Update largest divisor if found
    return largest_div

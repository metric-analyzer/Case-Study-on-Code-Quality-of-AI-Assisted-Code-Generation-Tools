
from typing import List


def factorize(n: int) -> List[int]:
    """Factorizes a given integer into its prime factors in ascending order."""

    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:  # Handle remaining prime factors greater than the square root of n
        factors.append(n)
    return factors

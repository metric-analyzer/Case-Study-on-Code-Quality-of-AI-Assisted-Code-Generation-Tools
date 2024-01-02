
def make_a_pile(n):
    """
    Creates a list representing a pile of stones with n levels, following the given rules.

    Args:
        n: A positive integer representing the number of levels in the pile.

    Returns:
        A list of integers, where each element represents the number of stones in a level.
    """

    if n <= 0:
        raise ValueError("n must be a positive integer")

    pile = [n]
    next_number = n + (1 if n % 2 else 2)  # Start with the next odd or even number

    for _ in range(1, n):
        pile.append(next_number)
        next_number += 2  # Increment by 2 to maintain odd/even pattern

    return pile

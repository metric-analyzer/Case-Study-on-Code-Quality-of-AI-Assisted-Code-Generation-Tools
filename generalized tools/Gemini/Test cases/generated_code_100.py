
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


def check(make_a_pile):
    assert make_a_pile(3) == [3, 5, 7], "Test 3"
    assert make_a_pile(4) == [4, 6, 8, 10], "Test 4"
    assert make_a_pile(5) == [5, 7, 9, 11, 13], "Test 5"
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16], "Test 6"
    assert make_a_pile(8) == [8, 10, 12, 14, 16, 18, 20, 22], "Test 8"

# Check some edge cases that are easy to work out by hand.
assert True, "This prints if this assert fails 2 (also good for debugging!)"

check(make_a_pile)

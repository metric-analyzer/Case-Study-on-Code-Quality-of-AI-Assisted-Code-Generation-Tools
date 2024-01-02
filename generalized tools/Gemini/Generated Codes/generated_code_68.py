
def pluck(arr):
    """Plucks the node with the smallest even value and its index from the given array."""

    smallest_even = float("inf")  # Initialize to a large value to find the smallest
    smallest_index = -1

    for i, val in enumerate(arr):
        if val % 2 == 0 and val < smallest_even:  # Check for even value and update if smaller
            smallest_even = val
            smallest_index = i

    return [smallest_even, smallest_index] if smallest_index != -1 else []

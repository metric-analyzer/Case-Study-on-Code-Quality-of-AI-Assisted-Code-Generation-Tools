
def choose_num(x, y):
    """
    Returns the largest even integer within the range [x, y] inclusive, or -1 if none exists.

    Args:
        x: The lower bound of the range.
        y: The upper bound of the range.

    Returns:
        The largest even integer within the range, or -1 if none exists.
    """

    if x > y:
        return -1  # No even numbers in the range if x is greater than y

    # Start from the higher number and decrement until an even number is found
    for num in range(y, x - 1, -1):
        if num % 2 == 0:
            return num

    return -1  # No even numbers found in the range

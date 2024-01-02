
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


def check(choose_num):
    assert choose_num(12, 15) == 14, "Test 1"
    assert choose_num(13, 12) == -1, "Test 2"
    assert choose_num(33, 12354) == 12354, "Test 3"
    assert choose_num(5234, 5233) == -1, "Test 4"
    assert choose_num(6, 29) == 28, "Test 5"
    assert choose_num(27, 10) == -1, "Test 6"

# Check some edge cases that are easy to work out by hand.
assert choose_num(7, 7) == -1, "Edge Test 1"
assert choose_num(546, 546) == 546, "Edge Test 2"

check(choose_num)

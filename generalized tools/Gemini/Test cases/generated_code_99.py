
def closest_integer(value):
    """
    Returns the closest integer to the given value, rounding away from zero if equidistant.

    Args:
        value (str): A string representing a number.

    Returns:
        int: The closest integer to the given value.
    """

    try:
        number = float(value)
    except ValueError:
        raise ValueError("Invalid input: value must be a string representing a number")

    rounded = round(number)

    if abs(number - rounded) == 0.5:
        # If equidistant, round away from zero
        return int(number + (number / abs(number)))  # Use sign of number to determine direction
    else:
        return rounded


def check(closest_integer):
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, "Test 2"
    assert closest_integer("-15.5") == -16, "Test 3"
    assert closest_integer("15.3") == 15, "Test 4"

# Check some edge cases that are easy to work out by hand.
assert closest_integer("0") == 0, "Test 0"

check(closest_integer)

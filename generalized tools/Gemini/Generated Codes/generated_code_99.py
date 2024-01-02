
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

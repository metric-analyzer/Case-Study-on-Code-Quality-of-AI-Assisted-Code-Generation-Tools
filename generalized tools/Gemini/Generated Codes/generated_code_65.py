
def circular_shift(x: int, shift: int) -> str:
    """Circularly shifts the digits of an integer to the right by the given shift."""

    digits = str(x)  # Convert the integer to a string to work with digits
    num_digits = len(digits)  # Get the number of digits

    # Handle cases where shift is greater than or equal to the number of digits
    shift = shift % num_digits

    # Efficiently perform the circular shift using slicing
    return digits[-shift:] + digits[:-shift]


def circular_shift(x: int, shift: int) -> str:
    """Circularly shifts the digits of an integer to the right by the given shift."""

    digits = str(x)  # Convert the integer to a string to work with digits
    num_digits = len(digits)  # Get the number of digits

    # Handle cases where shift is greater than or equal to the number of digits
    shift = shift % num_digits

    # Efficiently perform the circular shift using slicing
    return digits[-shift:] + digits[:-shift]


def check(circular_shift):
    # Check some simple cases
    assert circular_shift(100, 2) == "001"
    assert circular_shift(12, 2) == "12"
    assert circular_shift(97, 8) == "79"
    assert circular_shift(12, 1) == "21", "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert circular_shift(11, 101) == "11", "This prints if this assert fails 2 (also good for debugging!)"

check(circular_shift)

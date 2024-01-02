
def change_base(x: int, base: int) -> str:
    """Converts a positive integer x to a string representation in a given base (2-9)."""

    if not 2 <= base <= 9:
        raise ValueError("Base must be between 2 and 9.")

    digits = "0123456789"  # Use digits for bases up to 9
    result = ""

    while x > 0:
        digit = x % base  # Get the remainder in the new base
        result = digits[digit] + result  # Append digit to the result string
        x //= base  # Divide x by the base for the next iteration

    return result

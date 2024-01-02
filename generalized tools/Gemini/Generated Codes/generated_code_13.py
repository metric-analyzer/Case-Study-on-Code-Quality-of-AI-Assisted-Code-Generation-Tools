
def greatest_common_divisor(a: int, b: int) -> int:
    """Returns the greatest common divisor (GCD) of two integers using the Euclidean algorithm."""

    while b:
        a, b = b, a % b  # Repeatedly swap and take remainder until b becomes 0
    return a  # The GCD is the remaining value of a

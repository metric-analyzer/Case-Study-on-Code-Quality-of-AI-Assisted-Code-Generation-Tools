
import math


def poly(xs: list, x: float) -> float:
    """Evaluates polynomial with coefficients xs at point x."""

    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))


def find_zero(xs: list) -> float:
    """
    Finds a zero of the polynomial with coefficients xs.

    Args:
        xs: List of polynomial coefficients, assumed to have even length
            with the largest non-zero coefficient being the last one.

    Returns:
        A zero of the polynomial, or None if no zero is found within 500 iterations.
    """

    if len(xs) % 2 != 0 or xs[-1] == 0:
        raise ValueError("Invalid coefficient list: must have even length with non-zero largest coefficient.")

    # Initial guess for the zero
    x = 0.5

    for _ in range(500):  # Limit iterations to avoid infinite loops
        value = poly(xs, x)
        derivative = poly([i * coeff for i, coeff in enumerate(xs)], x)  # Calculate derivative
        if abs(value) < 1e-6:  # Check for a zero
            return x
        x -= value / derivative  # Newton-Raphson step

    # Indicate failure to find a zero within iterations
    return None


def derivative(xs: list) -> list:
    """Calculates the derivative of a polynomial represented by its coefficients."""

    if not xs:
        return []  # Empty list for the derivative of a constant polynomial

    return [i * x for i, x in enumerate(xs[1:])]  # Apply the power rule efficiently using list comprehension

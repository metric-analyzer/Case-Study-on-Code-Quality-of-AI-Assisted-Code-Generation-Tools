
def triangle_area(a, h):
    """Calculates the area of a triangle given its base and height."""

    # Ensure positive values for base and height
    if a <= 0 or h <= 0:
        raise ValueError("Base and height must be positive values.")

    area = 0.5 * a * h  # Apply the formula for triangle area
    return area

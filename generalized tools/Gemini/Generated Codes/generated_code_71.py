
import math

def triangle_area(a, b, c):
    """Calculates the area of a triangle given its side lengths, or -1 if it's not a valid triangle."""

    if not (a + b > c and a + c > b and b + c > a):  # Check for valid triangle
        return -1

    s = (a + b + c) / 2  # Calculate the semi-perimeter
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Heron's formula
    return round(area, 2)  # Round to 2 decimal places


from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """Finds the two closest elements in a list of numbers and returns them as a tuple."""

    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements.")

    min_diff = float("inf")  # Initialize minimum difference to a large value
    closest_pair = None  # Initialize closest pair to None

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            current_diff = abs(numbers[i] - numbers[j])
            if current_diff < min_diff:
                min_diff = current_diff
                closest_pair = (numbers[i], numbers[j])

    return closest_pair

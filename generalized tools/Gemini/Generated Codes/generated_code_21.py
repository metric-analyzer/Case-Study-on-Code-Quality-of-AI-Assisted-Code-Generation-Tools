
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Rescales a list of numbers to the unit interval [0, 1]."""

    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements.")

    min_value = min(numbers)
    max_value = max(numbers)
    range_value = max_value - min_value

    rescaled_numbers = []
    for number in numbers:
        rescaled_number = (number - min_value) / range_value  # Apply linear transformation
        rescaled_numbers.append(rescaled_number)

    return rescaled_numbers

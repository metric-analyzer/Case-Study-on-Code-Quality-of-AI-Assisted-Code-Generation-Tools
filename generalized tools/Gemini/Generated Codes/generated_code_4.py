
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """Calculates the mean absolute deviation of a list of numbers.

    Args:
        numbers: A list of floating-point numbers.

    Returns:
        The mean absolute deviation of the numbers.
    """

    if not numbers:
        raise ValueError("Input list cannot be empty.")

    # Calculate the mean:
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviations from the mean:
    absolute_deviations = [abs(number - mean) for number in numbers]

    # Calculate the mean of the absolute deviations:
    mean_absolute_deviation = sum(absolute_deviations) / len(absolute_deviations)

    return mean_absolute_deviation

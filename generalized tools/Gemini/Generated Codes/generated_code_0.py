
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if any two numbers in the given list are closer to each other than the given threshold.

    Args:
        numbers: A list of numbers.
        threshold: The minimum distance between two numbers to be considered close.

    Returns:
        True if there are any two numbers in the list that are closer to each other than the threshold, False otherwise.
    """

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True

    return False

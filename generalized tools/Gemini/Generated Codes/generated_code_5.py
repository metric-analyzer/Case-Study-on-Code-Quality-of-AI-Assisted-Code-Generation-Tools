
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """Intersperses a delimiter between every two consecutive elements of a list.

    Args:
        numbers: The list of numbers to intersperse.
        delimiter: The number to insert between the elements.

    Returns:
        A new list with the delimiter inserted between every two consecutive elements.
    """

    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Don't add a delimiter after the last element
            result.append(delimiter)
    return result

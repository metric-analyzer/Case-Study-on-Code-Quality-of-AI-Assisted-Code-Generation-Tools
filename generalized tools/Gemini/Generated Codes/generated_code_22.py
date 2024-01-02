
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """Filters a list of arbitrary values, returning only the integers."""

    integers = [value for value in values if isinstance(value, int)]
    return integers

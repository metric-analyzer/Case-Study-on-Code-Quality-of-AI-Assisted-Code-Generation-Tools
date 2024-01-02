
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filters a list of strings to those that start with the given prefix."""

    return [string for string in strings if string.startswith(prefix)]

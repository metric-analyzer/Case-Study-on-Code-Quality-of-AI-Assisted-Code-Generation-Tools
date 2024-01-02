
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filters a list of strings, keeping only those that contain the given substring.

    Args:
        strings: The list of strings to filter.
        substring: The substring to search for.

    Returns:
        A new list containing only the strings that contain the substring.
    """

    return [string for string in strings if substring in string]

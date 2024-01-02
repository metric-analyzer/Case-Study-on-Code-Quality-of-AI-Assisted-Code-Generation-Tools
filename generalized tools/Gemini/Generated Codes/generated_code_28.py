
from typing import List


def concatenate(strings: List[str]) -> str:
    """Concatenates a list of strings into a single string."""

    return "".join(strings)  # Leverage the efficient join() method

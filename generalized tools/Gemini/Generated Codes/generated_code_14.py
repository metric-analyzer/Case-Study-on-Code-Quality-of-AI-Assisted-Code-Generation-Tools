
from typing import List


def all_prefixes(string: str) -> List[str]:
    """Returns a list of all prefixes of a string, from shortest to longest."""

    prefixes = []
    for i in range(len(string) + 1):
        prefixes.append(string[:i])
    return prefixes


from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """Returns the longest string in a list, or None if the list is empty.

    Args:
        strings: A list of strings.

    Returns:
        The longest string in the list, or None if the list is empty.
    """

    if not strings:
        return None  # Handle empty list

    longest_string = strings[0]  # Initialize with the first string
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string

    return longest_string

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(longest): 
    assert longest([]) == None 
    assert longest(['x', 'y', 'z']) == 'x' 
    assert longest(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz' 

check(longest)

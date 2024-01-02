
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filters a list of strings to those that start with the given prefix."""

    return [string for string in strings if string.startswith(prefix)]


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(filter_by_prefix): 
    assert filter_by_prefix([], 'john') == [] 
    assert filter_by_prefix(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx'] 
    
check(filter_by_prefix)
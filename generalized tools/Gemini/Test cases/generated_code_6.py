
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """Parses a string of nested parentheses and returns the maximum nesting depth for each group.

    Args:
        paren_string: A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        A list of integers, where each integer represents the maximum nesting depth of the corresponding group.
    """

    nesting_levels = []
    current_level = 0

    for char in paren_string:
        if char == '(':
            current_level += 1
        elif char == ')':
            if current_level == 0:
                raise ValueError("Unbalanced parentheses")
            current_level -= 1
        elif char == ' ' and current_level > 0:
            nesting_levels.append(current_level)
            current_level = 0  # Reset for the next group

    # Check for balanced parentheses at the end:
    if current_level > 0:
        raise ValueError("Unbalanced parentheses")

    return nesting_levels

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(parse_nested_parens): 
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3] 
    assert parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4] 
    assert parse_nested_parens('(()(())((())))') == [4] 
    
check(parse_nested_parens)

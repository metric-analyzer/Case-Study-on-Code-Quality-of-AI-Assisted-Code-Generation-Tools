from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separates balanced parentheses groups within a string and returns a list of them.

    Args:
        paren_string: The input string containing nested parentheses.

    Returns:
        A list of strings, each representing a separate balanced parentheses group.
    """

    groups = []  # Stores the separated groups
    current_group = ""  # Holds the characters of the current group being built
    open_count = 0  # Tracks the number of open parentheses encountered

    for char in paren_string:
        if char == "(":
            open_count += 1
            current_group += char
        elif char == ")":
            open_count -= 1
            current_group += char
            if open_count == 0:  # Found a balanced group
                groups.append(current_group)
                current_group = ""  # Reset for the next group

    return groups

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(separate_paren_groups): 
    assert separate_paren_groups('(()()) ((())) () ((())()())') == [ '(()())', '((()))', '()', '((())()())' ] 
    assert separate_paren_groups('() (()) ((())) (((())))') == [ '()', '(())', '((()))', '(((())))' ] 
    assert separate_paren_groups('(()(())((())))') == [ '(()(())((())))' ] 
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())'] 
    

check(separate_paren_groups)
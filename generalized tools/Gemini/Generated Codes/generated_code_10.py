
def is_palindrome(string: str) -> bool:
    """Tests if a given string is a palindrome."""
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """Finds the shortest palindrome that begins with the supplied string."""

    if is_palindrome(string):
        return string  # Already a palindrome

    for i in range(len(string) - 1, -1, -1):
        prefix = string[:i]
        suffix = string[i:]
        if is_palindrome(suffix):
            return string + prefix[::-1]  # Append reversed prefix to form palindrome

    return string + string[::-1]  # No palindrome suffix found, append entire string reversed

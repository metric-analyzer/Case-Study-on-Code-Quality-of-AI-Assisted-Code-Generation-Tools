
def same_chars(s0: str, s1: str) -> bool:
    """Checks if two strings have the same characters, regardless of order."""

    # Use a set to efficiently track unique characters
    s0_chars = set(s0.lower())
    s1_chars = set(s1.lower())

    # Check if all characters in one set are present in the other
    return s0_chars.issubset(s1_chars) and s1_chars.issubset(s0_chars)

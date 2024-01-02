
def count_distinct_characters(string: str) -> int:
    """Counts the number of distinct characters in a string, ignoring case."""

    seen_chars = set()  # Use a set to store unique characters
    for char in string.lower():  # Convert characters to lowercase for case-insensitivity
        seen_chars.add(char)
    return len(seen_chars)  # Return the number of unique characters in the set

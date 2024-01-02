
def words_string(s):
    """
    Splits a string into words based on commas or spaces, and returns a list of the words.

    Args:
        s: The string to split.

    Returns:
        A list of the words in the string.
    """

    return s.split(r",\s*|\s+")  # Split on commas or one or more spaces

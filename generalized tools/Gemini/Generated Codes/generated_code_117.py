
def select_words(s, n):
    """Returns a list of words from string s that contain exactly n consonants.

    Args:
        s: The input string.
        n: The number of consonants to match.

    Returns:
        A list of words that meet the criteria.
    """

    if not s:
        return []  # Handle empty string case

    consonants = set("bcdfghjklmnpqrstvwxyz")
    words = s.split()
    matching_words = []

    for word in words:
        consonant_count = sum(1 for char in word.lower() if char in consonants)
        if consonant_count == n:
            matching_words.append(word)

    return matching_words


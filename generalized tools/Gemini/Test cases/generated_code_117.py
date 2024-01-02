
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

def check(select_words):
    # Check some simple cases
    assert select_words("Mary had a little lamb", 4) == ["little"], "Test 1"
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"], "Test 2"
    assert select_words("simple white space", 2) == [], "Test 3"
    assert select_words("Hello world", 4) == ["world"], "Test 4"
    assert select_words("Uncle sam", 3) == ["Uncle"], "Test 5"

    # Check some edge cases that are easy to work out by hand.
    assert select_words("", 4) == [], "Test 6"
    assert select_words("a b c d e f", 1) == ["b", "c", "d", "f"], "Test 7"

    # Check the function
    check(select_words)

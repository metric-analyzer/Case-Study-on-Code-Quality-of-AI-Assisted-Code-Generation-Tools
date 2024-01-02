
def get_closest_vowel(word):
    """Finds the closest vowel that stands between two consonants from the right side of the word.

    Args:
        word: The word to analyze.

    Returns:
        The closest vowel that meets the conditions, or an empty string if no such vowel is found.
    """

    vowels = "aeiouAEIOU"
    word_len = len(word)

    for i in range(word_len - 2, -1, -1):  # Iterate from right to left, excluding the first and last letters
        if word[i] in vowels:
            if not word[i + 1] in vowels and not word[i - 1] in vowels:  # Check for consonants surrounding the vowel
                return word[i]  # Found the closest qualifying vowel

    return ""  # No qualifying vowel found

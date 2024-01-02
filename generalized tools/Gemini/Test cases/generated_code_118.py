
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

def check(get_closest_vowel):
    # Check some simple cases
    assert get_closest_vowel("yogurt") == "u", "Test 1"
    assert get_closest_vowel("full") == "u", "Test 2"
    assert get_closest_vowel("easy") == "", "Test 3"
    assert get_closest_vowel("eAsy") == "", "Test 4"
    assert get_closest_vowel("ali") == "", "Test 5"
    assert get_closest_vowel("bad") == "a", "Test 6"
    assert get_closest_vowel("most") == "o", "Test 7"
    assert get_closest_vowel("ab") == "", "Test 8"
    assert get_closest_vowel("ba") == "", "Test 9"
    assert get_closest_vowel("quick") == "", "Test 10"
    assert get_closest_vowel("anime") == "i", "Test 11"
    assert get_closest_vowel("Asia") == "", "Test 12"
    assert get_closest_vowel("Above") == "o", "Test 13"

    # Check the function
    check(get_closest_vowel)


def remove_vowels(text: str) -> str:
    """Returns a string with all vowels removed."""

    vowels = "aeiouAEIOU"  # Define vowels for efficient removal
    no_vowels = ""
    for char in text:
        if char not in vowels:
            no_vowels += char
    return no_vowels

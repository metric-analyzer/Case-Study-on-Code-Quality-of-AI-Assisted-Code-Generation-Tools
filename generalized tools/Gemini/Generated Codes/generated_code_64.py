
def vowels_count(s: str) -> int:
    """Counts the number of vowels in a string, considering 'y' as a vowel only at the end."""

    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
        elif char == "y" and s.endswith("y"):  # Check for 'y' at the end
            count += 1
    return count

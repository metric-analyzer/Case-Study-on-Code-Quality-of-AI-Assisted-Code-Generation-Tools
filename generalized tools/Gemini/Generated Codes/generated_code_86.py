
def anti_shuffle(s):
    """
    Returns a string with words rearranged in ascending ASCII order within each word.
    """

    words = s.split()  # Split the string into words
    ordered_words = []

    for word in words:
        ordered_chars = sorted(word)  # Sort characters alphabetically
        ordered_words.append("".join(ordered_chars))  # Join sorted characters back into a word

    return " ".join(ordered_words)  # Join ordered words with spaces

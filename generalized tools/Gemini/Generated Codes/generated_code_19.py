
from typing import List


def sort_numbers(numbers: str) -> str:
    """Sorts space-delimited string numerals ('zero' to 'nine') from smallest to largest."""

    number_words = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    words = numbers.split()  # Split string into individual words
    sorted_words = sorted(words, key=lambda word: number_words[word])  # Sort using the word-to-number mapping
    return " ".join(sorted_words)  # Join back into a space-separated string

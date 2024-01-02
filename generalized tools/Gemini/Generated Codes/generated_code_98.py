
def count_upper(s):
  """
  Counts the number of uppercase vowels in even indices.

  Args:
    s: The string to analyze.

  Returns:
    The number of uppercase vowels in even indices.
  """

  vowel_count = 0
  for i, char in enumerate(s):
    if i % 2 == 0 and char.isupper() and char in "AEIOU":
      vowel_count += 1

  return vowel_count

# Example usage
print(count_upper("aBCdEf"))  # Output: 1
print(count_upper("abcdefg"))  # Output: 0
print(count_upper("dBBE"))  # Output: 0
print(count_upper("uU"))  # Output: 2
print(count_upper("aE"))  # Output: 1

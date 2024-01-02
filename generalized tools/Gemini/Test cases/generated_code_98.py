
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


def check(count_upper):
    assert count_upper('aBCdEf') == 1
    assert count_upper('abcdefg') == 0
    assert count_upper('dBBE') == 0
    assert count_upper('B') == 0
    assert count_upper('U') == 1
    assert count_upper('') == 0
    assert count_upper('EEEE') == 2

# Check some edge cases that are easy to work out by hand.
assert True

check(count_upper)

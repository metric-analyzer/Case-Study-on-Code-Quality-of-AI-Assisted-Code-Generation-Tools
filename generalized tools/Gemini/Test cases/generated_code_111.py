
def histogram(test):
  """
  Creates a dictionary of letter counts in a string.

  Args:
      test: A string containing lowercase letters.

  Returns:
      A dictionary mapping letters to their counts, or an empty dictionary if the
      string is empty.
  """

  # Initialize an empty dictionary
  letter_counts = {}

  # Loop through each character in the string
  for char in test:
    # Check if the character is a lowercase letter
    if char.islower():
      # Add the character to the dictionary with its count
      letter_counts[char] = letter_counts.get(char, 0) + 1

  # Return the dictionary of letter counts
  return letter_counts

# Example usage
test_string = "a b c"
print(histogram(test_string))  # Output: {'a': 1, 'b': 1, 'c': 1}

test_string = "a b b a"
print(histogram(test_string))  # Output: {'a': 2, 'b': 2}

test_string = ""
print(histogram(test_string))  # Output: {}


def check(histogram):
    # Check some simple cases
    assert histogram('a b b a') == {'a': 2, 'b': 2}, "Test 1"
    assert histogram('a b c a b') == {'a': 2, 'b': 2, 'c': 1}, "Test 2"
    assert histogram('a b c d g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'g': 1}, "Test 3"
    assert histogram('r t g') == {'r': 1, 't': 1, 'g': 1}, "Test 4"
    assert histogram('b b b b a') == {'b': 4, 'a': 1}, "Test 5"
    
    # Check some edge cases that are easy to work out by hand.
    assert histogram('') == {}, "Test 6"
    assert histogram('a') == {'a': 1}, "Test 7"

check(histogram)

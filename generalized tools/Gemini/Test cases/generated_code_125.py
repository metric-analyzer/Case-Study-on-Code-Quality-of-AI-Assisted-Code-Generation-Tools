def split_words(txt):
  """
  Splits a string of words based on whitespace, commas, or odd-ordered lowercase letters.

  Args:
      txt: The string to split.

  Returns:
      A list of words or the number of odd-ordered lowercase letters if no separators are found.
  """

  # Try splitting on whitespace
  words = txt.split()
  if words:
    return words

  # Try splitting on commas
  words = txt.split(",")
  if words:
    return words

  # No separators found, count odd-ordered lowercase letters
  count = 0
  for char in txt.lower():
    if ord(char) - ord('a') % 2 == 1:
      count += 1
  return count


def check(split_words):
    # Check some simple cases
    assert split_words("Hello world!") == ["Hello", "world!"], "Test 1"
    assert split_words("Hello,world!") == ["Hello", "world!"], "Test 2"
    assert split_words("Hello world,!") == ["Hello", "world,!"], "Test 3"
    assert split_words("Hello,Hello,world !") == ["Hello,Hello,world", "!"], "Test 4"
    
    # Check some cases with unique words
    assert split_words("abcdef") == 3, "Test 5"
    assert split_words("aaabb") == 2, "Test 6"
    assert split_words("aaaBb") == 1, "Test 7"
    
    # Check an empty string
    assert split_words("") == 0, "Test 8"

    # Check the function
    check(split_words)

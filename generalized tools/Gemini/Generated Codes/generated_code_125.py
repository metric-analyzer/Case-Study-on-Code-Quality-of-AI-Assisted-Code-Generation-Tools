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

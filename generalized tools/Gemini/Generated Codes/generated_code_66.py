
def digitSum(s):
  """
  This function calculates the sum of the ASCII codes of all uppercase characters in a string.

  Args:
      s: The string to analyze.

  Returns:
      The sum of the ASCII codes of all uppercase characters in the string.
  """

  sum = 0
  for char in s:
    if char.isupper():
      sum += ord(char)

  return sum

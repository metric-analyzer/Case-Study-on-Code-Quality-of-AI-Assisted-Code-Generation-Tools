
def iscube(a):
  """
  Determines if a given integer is a perfect cube (i.e., the cube of another integer).

  Args:
    a: The integer to check.

  Returns:
    True if a is a perfect cube, False otherwise.
  """

  potential_root = 0
  while potential_root ** 3 <= a:
    if potential_root ** 3 == a:
      return True  # Found a perfect cube root
    potential_root += 1

  return False  # No perfect cube root found

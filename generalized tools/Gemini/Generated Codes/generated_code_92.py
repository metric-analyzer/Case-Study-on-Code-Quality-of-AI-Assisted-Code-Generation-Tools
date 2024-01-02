
def any_int(x, y, z):
  """
  Checks if any of the three numbers are equal to the sum of the other two.

  Args:
    x: The first number.
    y: The second number.
    z: The third number.

  Returns:
    True if any of the numbers are equal to the sum of the other two, False otherwise.
  """

  # Check if all numbers are integers.
  if not all(isinstance(num, int) for num in (x, y, z)):
    return False

  # Check if x is equal to the sum of y and z.
  if x == y + z:
    return True

  # Check if y is equal to the sum of x and z.
  if y == x + z:
    return True

  # Check if z is equal to the sum of x and y.
  if z == x + y:
    return True

  # If none of the conditions are met, return False.
  return False

# Example usage
print(any_int(5, 2, 7))  # True
print(any_int(3, 2, 2))  # False
print(any_int(3, -2, 1))  # True
print(any_int(3.6, -2.2, 2))  # False

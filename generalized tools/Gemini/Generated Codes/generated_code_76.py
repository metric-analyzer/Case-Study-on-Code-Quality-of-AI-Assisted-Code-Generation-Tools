
def is_simple_power(x, n):
  """
  Determines if x is a simple power of n, meaning n raised to some integer power equals x.

  Args:
    x: The number to check.
    n: The base to check for simple power.

  Returns:
    True if x is a simple power of n, False otherwise.
  """

  # Handle the base cases:
  if x == 1:
    return True  # Any number to the power of 0 equals 1
  elif x == n:
    return True  # Any number to the power of 1 equals itself
  elif x < n:
    return False  # No simple power of n can be less than n (except 1)

  # Iterate through potential exponents, starting from 2:
  exponent = 2
  while n ** exponent <= x:
    if n ** exponent == x:
      return True
    exponent += 1

  return False  # No matching power found

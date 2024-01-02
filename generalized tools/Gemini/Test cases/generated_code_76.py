
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


def check(is_simple_power):
    # Check some simple cases
    assert is_simple_power(1, 4) == True, "Test 1"
    assert is_simple_power(2, 2) == True, "Test 2"
    assert is_simple_power(8, 2) == True, "Test 3"
    assert is_simple_power(3, 2) == False, "Test 4"
    assert is_simple_power(3, 1) == False, "Test 5"
    assert is_simple_power(5, 3) == False, "Test 6"
    
    # Check some additional simple cases
    assert is_simple_power(16, 2) == True, "Test 7"
    assert is_simple_power(143214, 16) == False, "Test 8"
    assert is_simple_power(4, 2) == True, "Test 9"
    assert is_simple_power(9, 3) == True, "Test 10"
    assert is_simple_power(16, 4) == True, "Test 11"
    assert is_simple_power(24, 2) == False, "Test 12"
    assert is_simple_power(128, 4) == False, "Test 13"
    assert is_simple_power(12, 6) == False, "Test 14"
    
    # Check some edge cases that are easy to work out by hand.
    assert is_simple_power(1, 1) == True, "Test 15"
    assert is_simple_power(1, 12) == True, "Test 16"

check(is_simple_power)

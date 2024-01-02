
def multiply(a, b):
  """
  Multiplies the unit digits of two integers.

  Args:
    a: The first integer.
    b: The second integer.

  Returns:
    The product of the unit digits of a and b.
  """

  # Extract the unit digits
  unit_digit_a = a % 10
  unit_digit_b = b % 10

  # Multiply the unit digits
  product = unit_digit_a * unit_digit_b

  # Return the product
  return product

# Example usage
print(multiply(148, 412))  # Output: 16
print(multiply(19, 28))  # Output: 72
print(multiply(2020, 1851))  # Output: 0
print(multiply(14, -15))  # Output: 20

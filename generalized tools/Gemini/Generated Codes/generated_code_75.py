
def is_multiply_prime(a):
  """
  Determines if a number is the product of exactly three prime numbers.

  Args:
    a: The number to check.

  Returns:
    True if a is the product of three primes, False otherwise.
  """

  prime_factors = []
  divisor = 2

  while a > 1:
    if a % divisor == 0:
      prime_factors.append(divisor)
      a //= divisor
    else:
      divisor += 1

  return len(prime_factors) == 3

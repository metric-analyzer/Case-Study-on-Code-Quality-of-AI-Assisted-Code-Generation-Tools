
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


def check(is_multiply_prime):
    assert is_multiply_prime(5) == False
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(8) == True
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(125) == True
    assert is_multiply_prime(3 * 5 * 7) == True
    assert is_multiply_prime(3 * 6 * 7) == False
    assert is_multiply_prime(9 * 9 * 9) == False
    assert is_multiply_prime(11 * 9 * 9) == False
    assert is_multiply_prime(11 * 13 * 7) == True

check(is_multiply_prime)

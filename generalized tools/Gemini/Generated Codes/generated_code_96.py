
def count_up_to(n):
  """
  This function takes an integer n and returns a list of all prime numbers less than or equal to n.

  Args:
    n: An integer.

  Returns:
    A list of prime numbers less than or equal to n.
  """

  if n < 2:
    return []

  primes = [2]
  for num in range(3, n + 1, 2):  # Iterate only over odd numbers
    is_prime = True
    for prime in primes:
      if num % prime == 0:
        is_prime = False
        break
    if is_prime:
      primes.append(num)

  return primes


def skjkasdkd(lst):
  """
  Finds the largest prime number in a list and returns the sum of its digits.

  Args:
    lst: A list of integers.

  Returns:
    The sum of the digits of the largest prime number in the list, or 0 if no prime numbers are found.
  """

  largest_prime = 0
  digit_sum = 0

  for num in lst:
    if is_prime(num) and num > largest_prime:
      largest_prime = num
      digit_sum = sum(map(int, str(num)))

  return digit_sum

def is_prime(n):
  """
  Checks if a number is prime.

  Args:
    n: An integer.

  Returns:
    True if n is prime, False otherwise.
  """

  if n <= 1:
    return False

  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False

  return True

# Example usage
lst1 = [0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]
lst2 = [1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]
lst3 = [1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]
lst4 = [0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6]
lst5 = [0, 81, 12, 3, 1, 21]
lst6 = [0, 8, 1, 2, 1, 7]

print(skjkasdkd(lst1))  # Output: 10
print(skjkasdkd(lst2))  # Output: 25
print(skjkasdkd(lst3))  # Output: 13
print(skjkasdkd(lst4))  # Output: 11
print(skjkasdkd(lst5))  # Output: 3
print(skjkasdkd(lst6))  # Output: 7

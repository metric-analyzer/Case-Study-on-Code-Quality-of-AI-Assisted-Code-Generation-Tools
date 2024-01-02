
import math


def f(n):
  """
  This function generates a list of size n, where the element at index i is:
    - the factorial of i if i is even
    - the sum of numbers from 1 to i otherwise.

  Args:
    n: The size of the list to generate.

  Returns:
    A list of size n, containing the calculated values.
  """

  result = []
  for i in range(1, n + 1):
    if i % 2 == 0:
      # Calculate factorial for even numbers
      factorial = math.factorial(i)
      result.append(factorial)
    else:
      # Calculate sum for odd numbers
      summation = sum(range(1, i + 1))
      result.append(summation)

  return result

# Example usage
print(f(5))  # Output: [1, 2, 6, 24, 15]


def check(f):
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(7) == [1, 2, 6, 24, 15, 720, 28]
    assert f(1) == [1]
    assert f(3) == [1, 2, 6]

check(f)

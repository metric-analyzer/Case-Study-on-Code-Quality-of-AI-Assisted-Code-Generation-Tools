
def solution(lst):
  """Calculates the sum of odd elements in even positions within a list.

  Args:
    lst: A non-empty list of integers.

  Returns:
    The sum of odd elements in even positions.
  """

  sum_of_odd_even_positioned = 0
  for i in range(len(lst)):
    if i % 2 == 0 and lst[i] % 2 != 0:  # Even position and odd element
      sum_of_odd_even_positioned += lst[i]

  return sum_of_odd_even_positioned


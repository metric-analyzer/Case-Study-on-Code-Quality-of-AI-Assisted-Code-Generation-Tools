
def unique_digits(x):
  """Given a list of positive integers x, return a sorted list of all elements that
  haven't any even digit.

  Note: Returned list should be sorted in increasing order.
  """

  odd_digit_elements = []
  for i in x:
    if all(int(c) % 2 == 1 for c in str(i)):
      odd_digit_elements.append(i)

  return sorted(odd_digit_elements)

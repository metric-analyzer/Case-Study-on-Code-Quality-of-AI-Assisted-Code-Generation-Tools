
def by_length(arr):
  """Sorts integers between 1 and 9 in an array, reverses them, and replaces digits with names.

  Args:
    arr: An array of integers.

  Returns:
    An array of strings, where valid integers are replaced with their corresponding names.
  """

  digit_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

  # Filter valid integers and sort them in descending order
  valid_integers = sorted((x for x in arr if 1 <= x <= 9), reverse=True)

  # Replace digits with names
  return [digit_names[x - 1] for x in valid_integers]


def check(by_length):
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"], "Error"
    assert by_length([]) == [], "Error"
    assert by_length([1, -1 , 55]) == ['One'], "Error"

# Check some edge cases that are easy to work out by hand.
assert True, "This prints if this assert fails 2 (also good for debugging!)"
assert by_length([1, -1, 3, 2]) == ["Three", "Two", "One"]
assert by_length([9, 4, 8]) == ["Nine", "Eight", "Four"]

check(by_length)

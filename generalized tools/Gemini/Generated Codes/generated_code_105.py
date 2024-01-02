
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

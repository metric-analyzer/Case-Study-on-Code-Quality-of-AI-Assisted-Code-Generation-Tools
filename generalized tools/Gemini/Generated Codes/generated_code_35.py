
def max_element(l: list) -> int:
  """Returns the maximum element in a list."""

  if not l:
    raise ValueError("The list is empty.")  # Handle empty list

  largest = l[0]  # Initialize with the first element
  for element in l:
    if element > largest:
      largest = element
  return largest

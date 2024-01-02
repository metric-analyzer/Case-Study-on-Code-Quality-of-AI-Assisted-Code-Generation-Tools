
def max_element(l: list) -> int:
  """Returns the maximum element in a list."""

  if not l:
    raise ValueError("The list is empty.")  # Handle empty list

  largest = l[0]  # Initialize with the first element
  for element in l:
    if element > largest:
      largest = element
  return largest

METADATA = {} 
def check(max_element): 
  assert max_element([1, 2, 3]) == 3 
  assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124 
  
check(max_element)
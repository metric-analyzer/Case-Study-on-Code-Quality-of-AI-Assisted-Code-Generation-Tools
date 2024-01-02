
def next_smallest(lst):
  """
  Finds the second smallest element in a list.

  Args:
    lst: A list of integers.

  Returns:
    The second smallest element in the list, or None if there is no such element.
  """

  if len(lst) < 2:
    return None

  # Find the smallest element and its index.
  smallest = min(lst)
  smallest_index = lst.index(smallest)

  # Remove the smallest element and find the next smallest.
  del lst[smallest_index]
  return min(lst)

# Example usage
lst = [1, 2, 3, 4, 5]
second_smallest = next_smallest(lst)
print(f"Second smallest element in {lst}: {second_smallest}")

lst = [5, 1, 4, 3, 2]
second_smallest = next_smallest(lst)
print(f"Second smallest element in {lst}: {second_smallest}")

lst = []
second_smallest = next_smallest(lst)
print(f"Second smallest element in {lst}: {second_smallest}")

lst = [1, 1]
second_smallest = next_smallest(lst)
print(f"Second smallest element in {lst}: {second_smallest}")

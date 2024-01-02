
def total_match(lst1, lst2):
  """
  Finds the list with the least total character count in all its strings.

  Args:
      lst1: The first list of strings.
      lst2: The second list of strings.

  Returns:
      The list with the least total character count, or the first list if equal.
  """

  total_chars1 = sum(len(s) for s in lst1)
  total_chars2 = sum(len(s) for s in lst2)

  if total_chars1 < total_chars2:
    return lst1
  elif total_chars1 > total_chars2:
    return lst2
  else:
    return lst1  # Tiebreaker: return the first list if equal


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




def check(total_match):
    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert total_match([], []) == []
    assert total_match(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hii']) == ['hi', 'admin']

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert total_match([], ['this']) == []
    assert total_match(['this'], []) == []

check(total_match)

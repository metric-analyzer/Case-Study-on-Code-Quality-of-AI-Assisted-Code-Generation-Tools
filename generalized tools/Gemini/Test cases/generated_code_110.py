
def exchange(lst1, lst2):
  """
  Determines if exchanging elements between two lists can make lst1 all even.
  """

  # Count even and odd elements in both lists
  even_lst1, odd_lst1 = 0, 0
  even_lst2, odd_lst2 = 0, 0
  for num in lst1:
    if num % 2 == 0:
      even_lst1 += 1
    else:
      odd_lst1 += 1
  for num in lst2:
    if num % 2 == 0:
      even_lst2 += 1
    else:
      odd_lst2 += 1

  # Check if the difference in even/odd elements can be balanced
  return odd_lst1 <= even_lst2 and even_lst1 <= odd_lst2

# Example usage
lst1 = [1, 2, 3, 4]
lst2 = [1, 2, 3, 4]
print(exchange(lst1, lst2))  # Output: "YES"

lst1 = [1, 2, 3, 4]
lst2 = [1, 5, 3, 4]
print(exchange(lst1, lst2))  # Output: "NO"


def check(exchange):
    # Check some simple cases
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES", "Test 1"
    assert exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO", "Test 2"
    assert exchange([1, 2, 3, 4], [2, 1, 4, 3]) == "YES", "Test 3"
    assert exchange([5, 7, 3], [2, 6, 4]) == "YES", "Test 4"
    assert exchange([5, 7, 3], [2, 6, 3]) == "NO", "Test 5"
    assert exchange([3, 2, 6, 1, 8, 9], [3, 5, 5, 1, 1, 1]) == "NO", "Test 6"

    # Check some edge cases that are easy to work out by hand.
    assert exchange([100, 200], [200, 200]) == "YES", "Test 7"

check(exchange)


def will_it_fly(q, w):
  """Determines if an object will fly based on balance and weight restrictions."""

  return (
      q == q[::-1]  # Check for palindrome (balance)
      and sum(q) <= w  # Check for weight limit
  )

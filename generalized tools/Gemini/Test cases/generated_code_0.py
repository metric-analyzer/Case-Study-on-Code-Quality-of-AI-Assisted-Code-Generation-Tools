#0
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if any two numbers in the given list are closer to each other than the given threshold.

    Args:
        numbers: A list of numbers.
        threshold: The minimum distance between two numbers to be considered close.

    Returns:
        True if there are any two numbers in the list that are closer to each other than the threshold, False otherwise.
    """

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True

    return False

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(has_close_elements): 
  assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True 
  assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False 
  assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True 
  assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False 
  assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True 
  assert has_close_elements([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True 
  assert has_close_elements([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False 
  print("all test passed")

check(has_close_elements)

from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """Finds the two closest elements in a list of numbers and returns them as a tuple."""

    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements.")

    min_diff = float("inf")  # Initialize minimum difference to a large value
    closest_pair = None  # Initialize closest pair to None

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            current_diff = abs(numbers[i] - numbers[j])
            if current_diff < min_diff:
                min_diff = current_diff
                closest_pair = (numbers[i], numbers[j])

    return closest_pair


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(find_closest_elements): 
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0) 
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9) 
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2) 
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0) 
    assert find_closest_elements([1.1, 2.2, 3.1, 4.1, 5.1]) == (2.2, 3.1) 
    
check(find_closest_elements)

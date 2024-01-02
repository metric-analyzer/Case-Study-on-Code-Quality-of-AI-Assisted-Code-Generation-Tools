
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """Calculates the rolling maximum of a list of integers.

    Args:
        numbers: A list of integers.

    Returns:
        A list containing the rolling maximum value found up to each index in the input list.
    """

    max_so_far = numbers[0]  # Initialize the maximum value with the first element
    result = []

    for num in numbers:
        if num > max_so_far:
            max_so_far = num  # Update the maximum value if a larger number is found
        result.append(max_so_far)  # Append the current maximum value to the result list

    return result

METADATA = { 'author': 'jt', 'dataset': 'test' } 

def check(rolling_max): 
    assert rolling_max([]) == [] 
    assert rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4] 
    assert rolling_max([4, 3, 2, 1]) == [4, 4, 4, 4] 
    assert rolling_max([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100] 
    
check(rolling_max)
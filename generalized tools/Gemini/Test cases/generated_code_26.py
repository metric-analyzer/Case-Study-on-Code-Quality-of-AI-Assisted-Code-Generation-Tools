
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """Removes duplicates from a list of integers while preserving order."""

    seen = set()  # Use a set to efficiently track seen elements
    unique_numbers = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            unique_numbers.append(num)
    return unique_numbers

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(remove_duplicates): 
    assert remove_duplicates([]) == [] 
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4] 
    assert remove_duplicates([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5] 
    
check(remove_duplicates)

from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Rescales a list of numbers to the unit interval [0, 1]."""

    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements.")

    min_value = min(numbers)
    max_value = max(numbers)
    range_value = max_value - min_value

    rescaled_numbers = []
    for number in numbers:
        rescaled_number = (number - min_value) / range_value  # Apply linear transformation
        rescaled_numbers.append(rescaled_number)

    return rescaled_numbers


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(rescale_to_unit): 
    assert rescale_to_unit([2.0, 49.9]) == [0.0, 1.0] 
    assert rescale_to_unit([100.0, 49.9]) == [1.0, 0.0] 
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0] 
    assert rescale_to_unit([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75] 
    assert rescale_to_unit([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75] 
    
check(rescale_to_unit)
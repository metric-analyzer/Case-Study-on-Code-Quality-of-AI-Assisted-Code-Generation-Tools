
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """Calculates the sum and product of a list of integers.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and product of the integers, in that order.
    """

    sum_result = 0
    product_result = 1

    for number in numbers:
        sum_result += number
        product_result *= number

    return sum_result, product_result

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(sum_product): 
    assert sum_product([]) == (0, 1) 
    assert sum_product([1, 1, 1]) == (3, 1) 
    assert sum_product([100, 0]) == (100, 0) 
    assert sum_product([3, 5, 7]) == (3 + 5 + 7, 3 * 5 * 7) 
    assert sum_product([10]) == (10, 10) 
    
check(sum_product)
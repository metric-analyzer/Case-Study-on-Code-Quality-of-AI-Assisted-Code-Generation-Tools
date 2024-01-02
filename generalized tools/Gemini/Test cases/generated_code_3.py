
from typing import List


def below_zero(operations: List[int]) -> bool:
    """Detects if the account balance falls below zero at any point.

    Args:
        operations: A list of integers representing deposits (positive) and withdrawals (negative).

    Returns:
        True if the balance falls below zero at any point, False otherwise.
    """

    balance = 0  # Initialize the balance to 0

    for operation in operations:
        balance += operation  # Apply each operation to the balance
        if balance < 0:  # Check if the balance has fallen below zero
            return True

    return False  # If the loop completes without returning True, the balance never went below zero

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(below_zero): 
    assert below_zero([]) == False 
    assert below_zero([1, 2, -3, 1, 2, -3]) == False 
    assert below_zero([1, 2, -4, 5, 6]) == True 
    assert below_zero([1, -1, 2, -2, 5, -5, 4, -4]) == False 
    assert below_zero([1, -1, 2, -2, 5, -5, 4, -5]) == True 
    assert below_zero([1, -2, 2, -2, 5, -5, 4, -4]) == True 

check(below_zero)


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

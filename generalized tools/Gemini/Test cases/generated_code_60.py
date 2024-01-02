
def sum_to_n(n: int) -> int:
    """Calculates the sum of numbers from 1 to n using the efficient arithmetic series formula."""

    return n * (n + 1) // 2  # Apply the formula for the sum of an arithmetic series


METADATA = {}

def check(sum_to_n):
    assert sum_to_n(1) == 1
    assert sum_to_n(6) == 21
    assert sum_to_n(11) == 66
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050

check(sum_to_n)

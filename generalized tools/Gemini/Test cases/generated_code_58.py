
def common(l1: list, l2: list) -> list:
    """Returns the sorted unique common elements between two lists."""

    return sorted(set(l1) & set(l2))  # Efficiently find common elements using set intersection and sort

METADATA = {}

def check(common):
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert common([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
    assert common([4, 3, 2, 8], []) == []

check(common)

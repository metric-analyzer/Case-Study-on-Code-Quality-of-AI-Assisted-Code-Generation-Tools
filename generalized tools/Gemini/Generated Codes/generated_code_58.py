
def common(l1: list, l2: list) -> list:
    """Returns the sorted unique common elements between two lists."""

    return sorted(set(l1) & set(l2))  # Efficiently find common elements using set intersection and sort

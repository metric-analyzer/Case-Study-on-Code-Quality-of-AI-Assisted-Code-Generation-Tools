
def sort_third(l: list) -> list:
    """Sorts elements at indices divisible by 3 in a list while preserving other elements."""

    result = []
    for i in range(len(l)):
        if i % 3 == 0:
            result.extend(sorted(l[i:i + 3]))  # Sort and extend 3 elements
        else:
            result.append(l[i])  # Append directly for other indices
    return result

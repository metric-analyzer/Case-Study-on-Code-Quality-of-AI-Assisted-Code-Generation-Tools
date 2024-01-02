
def sort_even(l: list) -> list:
    """Sorts elements at even indices in a list while preserving elements at odd indices."""

    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            even_values = sorted(l[i::2])  # Sort even values
            result.extend(even_values)  # Extend sorted even values
        else:
            result.append(l[i])  # Append odd values directly
    return result

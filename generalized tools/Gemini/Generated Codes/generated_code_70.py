
def strange_sort_list(lst):
    """Sorts a list in the strange order (min, max, min, max, ...) using a temporary list."""

    if not lst:  # Handle empty list
        return []

    strange_sorted = []
    while lst:
        strange_sorted.append(min(lst))  # Add the minimum value
        lst.remove(min(lst))  # Remove it from the original list
        if lst:  # Avoid out-of-bounds error if only one element was present
            strange_sorted.append(max(lst))  # Add the maximum value
            lst.remove(max(lst))  # Remove it from the original list

    return strange_sorted

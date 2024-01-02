
def add(lst):
    """Adds the even elements at odd indices in a list."""

    total = 0
    for i in range(1, len(lst), 2):  # Iterate over odd indices
        if lst[i] % 2 == 0:  # Check if element is even
            total += lst[i]

    return total

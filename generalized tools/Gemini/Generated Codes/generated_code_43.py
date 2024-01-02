
def pairs_sum_to_zero(l: list) -> bool:
    """Checks if there are two distinct elements in the list that sum to zero."""

    seen = set()  # Use a set to efficiently track seen elements and their complements
    for num in l:
        if -num in seen:  # Check if the complement exists in the set
            return True
        seen.add(num)  # Add the current number to the set
    return False

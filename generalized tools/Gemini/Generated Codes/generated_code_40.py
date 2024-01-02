
def triples_sum_to_zero(l: list) -> bool:
    """Checks if there are three distinct elements in the list that sum to zero."""

    l.sort()  # Sort the list for efficient comparison
    for i in range(len(l) - 2):
        if i > 0 and l[i] == l[i - 1]:  # Skip duplicates
            continue
        left, right = i + 1, len(l) - 1
        while left < right:
            current_sum = l[i] + l[left] + l[right]
            if current_sum == 0:
                return True
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return False

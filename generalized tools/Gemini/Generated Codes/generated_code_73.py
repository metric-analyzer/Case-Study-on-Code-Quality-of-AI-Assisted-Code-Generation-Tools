
def smallest_change(arr):
    """Calculates the minimum number of changes needed to make an array palindromic."""

    changes = 0
    left, right = 0, len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            changes += 1

            # Move towards the center to find a matching element
            while left < right and arr[left] != arr[right]:
                left += 1
            while left < right and arr[left] != arr[right]:
                right -= 1

        left += 1
        right -= 1

    return changes

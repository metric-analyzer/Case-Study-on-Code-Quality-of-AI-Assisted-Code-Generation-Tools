
def move_one_ball(arr):
    """
    Determines if the array can be sorted in non-decreasing order using right shifts.
    """

    if not arr:  # Empty array is already sorted
        return True

    n = len(arr)
    minimum_index = arr.index(min(arr))  # Find the index of the minimum element

    # Check if right shifts can position the minimum element correctly
    return (minimum_index == 0 or
            minimum_index == n - 1 or
            arr[minimum_index - 1] <= arr[minimum_index + 1])

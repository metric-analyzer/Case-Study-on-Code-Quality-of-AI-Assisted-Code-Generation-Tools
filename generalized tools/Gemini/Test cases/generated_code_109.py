
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


def check(move_one_ball):
    # Check some simple cases
    assert move_one_ball([3, 4, 5, 1, 2]) == True, "Test 1"
    assert move_one_ball([3, 5, 10, 1, 2]) == True, "Test 2"
    assert move_one_ball([4, 3, 1, 2]) == False, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert move_one_ball([3, 5, 4, 1, 2]) == False, "Test 4"
    assert move_one_ball([]) == True, "Test 5"

check(move_one_ball)

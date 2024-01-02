
def minSubArraySum(nums):
    """
    Finds the minimum sum of any non-empty sub-array of the given array.

    Args:
        nums: An array of integers.

    Returns:
        The minimum sum of any non-empty sub-array.
    """

    min_sum = float('inf')  # Initialize minimum sum to infinity
    current_sum = 0  # Initialize current sub-array sum

    for num in nums:
        current_sum += num  # Add current number to the sub-array sum

        # Update minimum sum if current sub-array sum is smaller
        min_sum = min(min_sum, current_sum)

        # If current sum exceeds minimum sum, reset it (start a new sub-array)
        if current_sum > min_sum:
            current_sum = 0

    # Ensure a non-empty sub-array is found (handle cases with all non-negative numbers)
    return min_sum if min_sum != float('inf') else min(nums)


def check(minSubArraySum):
    # Check some simple cases
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1, "Test 1"
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([-1, -2, -3, 2, -10]) == -14
    assert minSubArraySum([-9999999999999999]) == -9999999999999999
    assert minSubArraySum([0, 10, 20, 1000000]) == 0
    assert minSubArraySum([-1, -2, -3, 10, -5]) == -6
    assert minSubArraySum([100, -1, -2, -3, 10, -5]) == -6
    assert minSubArraySum([10, 11, 13, 8, 3, 4]) == 3
    assert minSubArraySum([100, -33, 32, -1, 0, -2]) == -33

    # Check some edge cases that are easy to work out by hand
    assert minSubArraySum([-10]) == -10, "Test 2"
    assert minSubArraySum([7]) == 7
    assert minSubArraySum([1, -1]) == -1

# Check the function
check(minSubArraySum)

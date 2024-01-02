
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


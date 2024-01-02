
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """

    sum = 0
    for i in range(k):
        if arr[i] <= 99:
            sum += arr[i]
    return sum

# Example usage
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(result)  # Output: 24


def check(add_elements):
    # Check some simple cases
    assert add_elements([1, -2, -3, 41, 57, 76, 87, 88, 99], 3) == -4, "Test 1"
    assert add_elements([111, 121, 3, 4000, 5, 6], 2) == 0, "Test 2"
    assert add_elements([11, 21, 3, 90, 5, 6, 7, 8, 9], 4) == 125, "Test 3"
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24, "Test 4"

    # Check the function
    check(add_elements)

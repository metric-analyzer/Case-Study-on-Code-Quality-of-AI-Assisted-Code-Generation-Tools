
def get_odd_collatz(n):
    """
    Generates the Collatz sequence starting from n, storing only the odd numbers,
    and returns them as a sorted list.
    """

    odd_numbers = []
    current_number = n

    while current_number != 1:
        if current_number % 2 == 1:
            odd_numbers.append(current_number)

        if current_number % 2 == 0:
            current_number //= 2
        else:
            current_number = 3 * current_number + 1

    # Ensure 1 is always included in the result
    odd_numbers.append(1)

    return sorted(odd_numbers)  # Sort the odd numbers in ascending order

def check(get_odd_collatz):
    # Check some simple cases
    assert get_odd_collatz(14) == [1, 5, 7, 11, 13, 17], "Test 1"
    assert get_odd_collatz(5) == [1, 5], "Test 2"
    assert get_odd_collatz(12) == [1, 3, 5], "Test 3"

    # Check the function
    check(get_odd_collatz)

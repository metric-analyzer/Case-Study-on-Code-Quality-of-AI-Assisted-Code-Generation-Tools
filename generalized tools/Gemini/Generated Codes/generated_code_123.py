
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


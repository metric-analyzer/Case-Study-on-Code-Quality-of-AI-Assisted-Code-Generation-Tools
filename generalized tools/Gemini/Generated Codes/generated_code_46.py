
def fib4(n: int) -> int:
    """Calculates the nth Fib4 number efficiently without recursion."""

    if n < 0:
        raise ValueError("n must be non-negative.")

    # Base cases for the first four values
    if n <= 3:
        return 0 if n < 2 else 2

    # Initialize a list to store the first four Fib4 numbers
    fib_sequence = [0, 0, 2, 0]

    # Iterate from the 5th Fib4 number up to the nth
    for i in range(4, n + 1):
        next_fib = sum(fib_sequence[-4:])  # Calculate the next Fib4 number
        fib_sequence.append(next_fib)  # Append it to the list

    return fib_sequence[-1]  # Return the nth Fib4 number

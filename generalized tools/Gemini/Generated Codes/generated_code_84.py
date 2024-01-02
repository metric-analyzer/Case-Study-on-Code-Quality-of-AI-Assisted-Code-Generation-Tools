
def solve(N):
    """Calculates the sum of digits in the binary representation of N and returns it as a binary string."""

    binary_sum = 0
    while N > 0:
        binary_sum += N % 2  # Add the current binary digit to the sum
        N //= 2  # Shift N right to process the next digit

    return bin(binary_sum)[2:]  # Convert the sum to binary and remove the "0b" prefix

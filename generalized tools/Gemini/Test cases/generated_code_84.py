
def solve(N):
    """Calculates the sum of digits in the binary representation of N and returns it as a binary string."""

    binary_sum = 0
    while N > 0:
        binary_sum += N % 2  # Add the current binary digit to the sum
        N //= 2  # Shift N right to process the next digit

    return bin(binary_sum)[2:]  # Convert the sum to binary and remove the "0b" prefix


def check(solve):
    # Check some simple cases
    assert solve(1000) == "1", "Test 1"
    assert solve(150) == "110", "Test 2"
    assert solve(147) == "1100", "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert solve(333) == "1001", "Test 4"
    assert solve(963) == "10010", "Test 5"

check(solve)

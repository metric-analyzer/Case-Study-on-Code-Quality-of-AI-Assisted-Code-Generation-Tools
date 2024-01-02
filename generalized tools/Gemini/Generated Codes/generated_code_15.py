
def string_sequence(n: int) -> str:
    """Returns a string containing space-delimited numbers from 0 up to n, inclusive."""

    return " ".join(str(num) for num in range(n + 1))  # Create a string using a generator expression

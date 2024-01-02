
def fib(n: int) -> int:
    """Calculates the nth Fibonacci number efficiently using memoization."""

    memo = {}  # Create a memoization dictionary to store previously calculated results

    def fib_helper(n):
        if n in memo:
            return memo[n]  # Reuse cached result if already calculated

        if n <= 2:
            result = 1  # Base cases for Fibonacci sequence
        else:
            result = fib_helper(n - 1) + fib_helper(n - 2)  # Recursively calculate using the Fibonacci rule

        memo[n] = result  # Store the result in the memoization dictionary
        return result

    return fib_helper(n)


METADATA = {}

def check(fib):
    assert fib(10) == 55
    assert fib(1) == 1
    assert fib(8) == 21
    assert fib(11) == 89
    assert fib(12) == 144

check(fib)

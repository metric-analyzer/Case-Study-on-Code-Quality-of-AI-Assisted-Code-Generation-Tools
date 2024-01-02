
def fibfib(n: int) -> int:
    """Efficiently calculates the nth FibFib number using memoization."""

    memo = {0: 0, 1: 0, 2: 1}  # Initialize memoization dictionary with base cases

    def fibfib_helper(n):
        if n not in memo:
            memo[n] = fibfib_helper(n - 1) + fibfib_helper(n - 2) + fibfib_helper(n - 3)  # Recursively calculate using the FibFib rule
        return memo[n]

    return fibfib_helper(n)

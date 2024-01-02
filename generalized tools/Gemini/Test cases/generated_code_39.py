
def prime_fib(n: int) -> int:
    """
    Finds the nth Fibonacci number that is also prime.

    Args:
        n: The desired index of the prime Fibonacci number.

    Returns:
        The nth prime Fibonacci number.

    Raises:
        ValueError: If n is less than 1.
    """

    if n < 1:
        raise ValueError("n must be a positive integer.")

    # Initialize Fibonacci sequence
    a, b = 0, 1
    count = 1  # Count of encountered Fibonacci numbers

    # Iterate until the nth prime Fibonacci number is found
    while count < n:
        # Check if current Fibonacci number is prime
        if is_prime(b):
            count += 1
        # Generate next Fibonacci number
        a, b = b, a + b

    return b  # Return the nth prime Fibonacci number

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


METADATA = {} 
def check(prime_fib): 
    assert prime_fib(1) == 2 
    assert prime_fib(2) == 3 
    assert prime_fib(3) == 5 
    assert prime_fib(4) == 13 
    assert prime_fib(5) == 89 
    assert prime_fib(6) == 233 
    assert prime_fib(7) == 1597 
    assert prime_fib(8) == 28657 
    assert prime_fib(9) == 514229 
    assert prime_fib(10) == 433494437 

check(prime_fib)
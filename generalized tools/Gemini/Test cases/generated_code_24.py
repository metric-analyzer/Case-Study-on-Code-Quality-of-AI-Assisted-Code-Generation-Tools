
def largest_divisor(n: int) -> int:
    """Finds the largest divisor of a number n, smaller than n."""

    largest_div = 1  # Initialize largest divisor to 1
    for i in range(2, n // 2 + 1):  # Iterate from 2 up to n/2
        if n % i == 0:  # Check if i is a divisor of n
            largest_div = i  # Update largest divisor if found
    return largest_div

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(largest_divisor): 
    assert largest_divisor(3) == 1 
    assert largest_divisor(7) == 1 
    assert largest_divisor(10) == 5 
    assert largest_divisor(100) == 50 
    assert largest_divisor(49) == 7 
    
check(largest_divisor)
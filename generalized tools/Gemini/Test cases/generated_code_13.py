
def greatest_common_divisor(a: int, b: int) -> int:
    """Returns the greatest common divisor (GCD) of two integers using the Euclidean algorithm."""

    while b:
        a, b = b, a % b  # Repeatedly swap and take remainder until b becomes 0
    return a  # The GCD is the remaining value of a


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(greatest_common_divisor): 
    assert greatest_common_divisor(3, 7) == 1 
    assert greatest_common_divisor(10, 15) == 5 
    assert greatest_common_divisor(49, 14) == 7 
    assert greatest_common_divisor(144, 60) == 12 
    
check(greatest_common_divisor)
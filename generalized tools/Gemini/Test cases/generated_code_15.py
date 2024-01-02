
def string_sequence(n: int) -> str:
    """Returns a string containing space-delimited numbers from 0 up to n, inclusive."""

    return " ".join(str(num) for num in range(n + 1))  # Create a string using a generator expression

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(string_sequence): 
    assert string_sequence(0) == '0' 
    assert string_sequence(3) == '0 1 2 3' 
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10' 
    
check(string_sequence)
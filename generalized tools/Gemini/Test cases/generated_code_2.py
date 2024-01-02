
def truncate_number(number: float) -> float:
    """Returns the decimal part of a positive floating-point number.

    Args:
        number: The positive floating-point number to truncate.

    Returns:
        The decimal part of the number, as a float.
    """

    # Ensure the input is a valid positive number:
    if number <= 0:
        raise ValueError("Input must be a positive number.")

    # Extract the integer part using the built-in int() function:
    integer_part = int(number)

    # Subtract the integer part from the original number to get the decimal part:
    decimal_part = number - integer_part

    return decimal_part


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(truncate_number): 
    assert truncate_number(3.5) == 0.5 
    assert abs(truncate_number(1.33) - 0.33) < 1e-6 
    assert abs(truncate_number(123.456) - 0.456) < 1e-6 
    
check(truncate_number)

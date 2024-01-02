
from typing import List


def string_xor(a: str, b: str) -> str:
    """Performs binary XOR on two strings of 1s and 0s and returns the result as a string.

    Args:
        a: The first binary string.
        b: The second binary string.

    Returns:
        The result of performing XOR on the two strings, as a string.

    Raises:
        ValueError: If the input strings have different lengths or contain characters other than '0' and '1'.
    """

    if len(a) != len(b):
        raise ValueError("Input strings must have the same length.")

    result = ""
    for i in range(len(a)):
        if a[i] not in "01" or b[i] not in "01":
            raise ValueError("Input strings must only contain '0' and '1' characters.")
        result += str(int(a[i]) ^ int(b[i]))  # Perform bitwise XOR and convert back to string

    return result
METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(string_xor): 
    assert string_xor('111000', '101010') == '010010' 
    assert string_xor('1', '1') == '0' 
    assert string_xor('0101', '0000') == '0101' 
    
check(string_xor)
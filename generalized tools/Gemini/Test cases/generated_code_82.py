
def prime_length(string):
    """
    Determines if the length of a string is a prime number.

    Args:
        string: The input string.

    Returns:
        True if the length of the string is prime, False otherwise.
    """

    string_length = len(string)

    if string_length <= 1:
        return False  # 1 and 0 are not prime

    for divisor in range(2, int(string_length**0.5) + 1):
        if string_length % divisor == 0:
            return False  # Found a divisor, not prime

    return True  # No divisors found, prime


def check(prime_length):
    # Check some simple cases
    assert prime_length('Hello') == True, "Test 1"
    assert prime_length('abcdcba') == True, "Test 2"
    assert prime_length('kittens') == True, "Test 3"
    assert prime_length('orange') == False, "Test 4"
    assert prime_length('wow') == True, "Test 5"
    assert prime_length('world') == True, "Test 6"
    assert prime_length('MadaM') == True, "Test 7"
    assert prime_length('Wow') == True, "Test 8"
    assert prime_length('') == False, "Test 9"
    assert prime_length('HI') == True, "Test 10"
    assert prime_length('go') == True, "Test 11"
    assert prime_length('gogo') == False, "Test 12"
    assert prime_length('aaaaaaaaaaaaaaa') == False, "Test 13"

check(prime_length)

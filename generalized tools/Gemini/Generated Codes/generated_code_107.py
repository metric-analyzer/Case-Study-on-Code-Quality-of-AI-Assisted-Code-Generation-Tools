
def is_palindrome(num):
    """Checks if a given number is a palindrome."""
    return str(num) == str(num)[::-1]

def even_odd_palindrome(n):
    """
    Returns a tuple with the counts of even and odd palindromes within 1 to n, inclusive.
    """
    even_count = 0
    odd_count = 0

    for num in range(1, n + 1):
        if is_palindrome(num):
            if num % 2 == 0:  # Even palindrome
                even_count += 1
            else:  # Odd palindrome
                odd_count += 1

    return even_count, odd_count

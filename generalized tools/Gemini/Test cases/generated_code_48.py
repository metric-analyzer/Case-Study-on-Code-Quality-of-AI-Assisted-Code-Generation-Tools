
def is_palindrome(text: str) -> bool:
    """Checks if a string is a palindrome (reads the same forwards and backwards)."""

    # Handle empty string case
    if not text:
        return True

    # Efficiently iterate through half the string
    for i in range(len(text) // 2):
        if text[i] != text[-(i + 1)]:  # Compare first and last characters, working inwards
            return False

    return True


METADATA = {}

def check(is_palindrome):
    assert is_palindrome('') == True
    assert is_palindrome('aba') == True
    assert is_palindrome('aaaaa') == True
    assert is_palindrome('zbcd') == False
    assert is_palindrome('xywyx') == True
    assert is_palindrome('xywyz') == False
    assert is_palindrome('xywzx') == False

check(is_palindrome)

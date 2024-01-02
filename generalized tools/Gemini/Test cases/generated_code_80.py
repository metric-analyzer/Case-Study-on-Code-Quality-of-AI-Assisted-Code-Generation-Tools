
def is_happy(s):
    """Checks if a string is happy (has distinct consecutive triplets)."""

    if len(s) < 3:
        return False  # Too short to be happy

    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False  # Found non-distinct triplet

    return True  # All triplets are distinct


def check(is_happy):
    # Check some simple cases
    assert is_happy("a") == False, "Test 1"
    assert is_happy("aa") == False, "Test 2"
    assert is_happy("abcd") == True, "Test 3"
    assert is_happy("aabb") == False, "Test 4"
    assert is_happy("adb") == True, "Test 5"
    assert is_happy("xyy") == False, "Test 6"
    assert is_happy("iopaxpoi") == True, "Test 7"
    assert is_happy("iopaxioi") == False, "Test 8"

check(is_happy)

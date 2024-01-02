
def match_parens(lst):
    """Checks if it's possible to concatenate two strings of parentheses to form a balanced string.

    Args:
        lst: A list of two strings containing only parentheses.

    Returns:
        'Yes' if the strings can be concatenated to form a balanced string, 'No' otherwise.
    """

    counts = [0, 0]  # Count opening and closing parentheses in each string
    for i in range(2):
        for char in lst[i]:
            counts[i] += 1 if char == '(' else -1

    # If one string needs more opening parens and the other needs more closing parens, they can be combined
    return 'Yes' if counts[0] * counts[1] < 0 else 'No'


def check(match_parens):
    # Check some simple cases
    assert match_parens(['()(', ')']) == 'Yes', "Test 1"
    assert match_parens([')', ')']) == 'No', "Test 2"
    assert match_parens(['(()(())', '())())']) == 'No', "Test 3"
    assert match_parens([')())', '(()()(']) == 'Yes', "Test 4"
    assert match_parens(['(())))', '(()())((']) == 'Yes', "Test 5"
    assert match_parens(['()', '())']) == 'No', "Test 6"
    assert match_parens(['(()(', '()))()']) == 'Yes', "Test 7"
    assert match_parens(['((((', '((())']) == 'No', "Test 8"
    assert match_parens([')(()', '(()(']) == 'No', "Test 9"
    assert match_parens([')(', ')(']) == 'No', "Test 10"

    # Check the function
    check(match_parens)

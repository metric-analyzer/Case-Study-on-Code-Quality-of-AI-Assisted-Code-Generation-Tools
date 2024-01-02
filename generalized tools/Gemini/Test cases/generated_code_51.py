
def remove_vowels(text: str) -> str:
    """Returns a string with all vowels removed."""

    vowels = "aeiouAEIOU"  # Define vowels for efficient removal
    no_vowels = ""
    for char in text:
        if char not in vowels:
            no_vowels += char
    return no_vowels
METADATA = {}

def check(remove_vowels):
    assert remove_vowels('') == ''
    assert remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert remove_vowels('fedcba') == 'fdcb'
    assert remove_vowels('eeeee') == ''
    assert remove_vowels('acBAA') == 'cB'
    assert remove_vowels('EcBOO') == 'cB'
    assert remove_vowels('ybcd') == 'ybcd'

check(remove_vowels)

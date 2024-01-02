
def flip_case(string: str) -> str:
    """Flips the case of a given string (lowercase to uppercase, uppercase to lowercase)."""

    flipped_string = ""
    for char in string:
        if char.islower():
            flipped_string += char.upper()
        elif char.isupper():
            flipped_string += char.lower()
        else:
            flipped_string += char  # Keep non-alphabetic characters as-is
    return flipped_string


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(flip_case): 
    assert flip_case('') == '' 
    assert flip_case('Hello!') == 'hELLO!' 
    assert flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS' 
    
check(flip_case)
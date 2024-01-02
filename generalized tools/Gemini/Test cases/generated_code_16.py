
def count_distinct_characters(string: str) -> int:
    """Counts the number of distinct characters in a string, ignoring case."""

    seen_chars = set()  # Use a set to store unique characters
    for char in string.lower():  # Convert characters to lowercase for case-insensitivity
        seen_chars.add(char)
    return len(seen_chars)  # Return the number of unique characters in the set


METADATA = { 'author': 'jt', 'dataset': 'test' } 

def check(count_distinct_characters): 
    assert count_distinct_characters('') == 0 
    assert count_distinct_characters('abcde') == 5 
    assert count_distinct_characters('abcde' + 'cade' + 'CADE') == 5 
    assert count_distinct_characters('aaaaAAAAaaaa') == 1 
    assert count_distinct_characters('Jerry jERRY JeRRRY') == 5 
    
check(count_distinct_characters)
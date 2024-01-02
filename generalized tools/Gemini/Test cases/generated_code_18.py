
def how_many_times(string: str, substring: str) -> int:
    """Counts the number of times a substring appears in a string, including overlapping occurrences."""

    count = 0
    i = 0
    while i < len(string):
        j = string.find(substring, i)  # Find the next occurrence of the substring
        if j == -1:
            break  # No more occurrences found
        count += 1
        i = j + 1  # Start the next search after the current occurrence

    return count

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(how_many_times): 
    assert how_many_times('', 'x') == 0 
    assert how_many_times('xyxyxyx', 'x') == 4 
    assert how_many_times('cacacacac', 'cac') == 4 
    assert how_many_times('john doe', 'john') == 1 
    
check(how_many_times)
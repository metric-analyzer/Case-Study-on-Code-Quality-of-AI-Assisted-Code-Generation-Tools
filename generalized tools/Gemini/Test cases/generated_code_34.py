
def unique(l: list) -> list:
    """Returns a sorted list of unique elements from the input list."""

    return sorted(set(l))  # Leverage set for uniqueness and sorting


METADATA = {} 
def check(unique): 
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123] 
    
check(unique)
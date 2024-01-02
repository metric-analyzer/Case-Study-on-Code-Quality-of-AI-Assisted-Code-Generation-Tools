
def monotonic(l: list) -> bool:
    """Checks if a list is monotonically increasing or decreasing."""

    # Handle lists with less than two elements
    if len(l) < 2:
        return True

    direction = None  # Initialize direction as unknown
    for i in range(1, len(l)):
        if l[i - 1] < l[i]:
            if direction is not None and direction != "increasing":
                return False  # Not monotonic if there's a change in direction
            direction = "increasing"
        elif l[i - 1] > l[i]:
            if direction is not None and direction != "decreasing":
                return False  # Not monotonic if there's a change in direction
            direction = "decreasing"
        else:
            continue  # Equal elements are allowed

    return True  # List is monotonic if no direction changes were found


METADATA = {}

def check(monotonic):
    assert monotonic([1, 2, 4, 10]) == True
    assert monotonic([1, 2, 4, 20]) == True
    assert monotonic([1, 20, 4, 10]) == False
    assert monotonic([4, 1, 0, -10]) == True
    assert monotonic([4, 1, 1, 0]) == True
    assert monotonic([1, 2, 3, 2, 5, 60]) == False
    assert monotonic([1, 2, 3, 4, 5, 60]) == True
    assert monotonic([9, 9, 9, 9]) == True

check(monotonic)

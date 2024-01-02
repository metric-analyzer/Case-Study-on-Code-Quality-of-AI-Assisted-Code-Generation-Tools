
def below_threshold(l: list, t: int) -> bool:
    """Checks if all numbers in the list l are below the threshold t."""

    return all(x < t for x in l)  # Use all() for concise and efficient check

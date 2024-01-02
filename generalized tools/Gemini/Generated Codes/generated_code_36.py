
def fizz_buzz(n: int) -> int:
    """Counts the number of 7s in integers divisible by 11 or 13, less than n."""

    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count("7")  # Count 7s in the string representation
    return count

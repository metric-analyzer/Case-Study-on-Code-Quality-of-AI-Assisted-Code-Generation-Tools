
def search(lst):
    """
    Finds the greatest integer in a list that has a frequency greater than or equal to its value.
    """

    counts = {}  # Dictionary to store frequencies of each integer
    for num in lst:
        counts[num] = counts.get(num, 0) + 1

    # Iterate through the numbers in descending order to find the first matching one
    for num in sorted(counts, reverse=True):
        if num > 0 and counts[num] >= num:
            return num

    return -1  # No matching integer found


def sort_array(array):
    """
    Sorts a copy of the array in ascending or descending order based on the sum of first and last elements.
    """

    copy_array = array.copy()  # Create a copy to avoid modifying the original

    if (copy_array[0] + copy_array[-1]) % 2 == 1:  # Sum is odd, sort ascending
        copy_array.sort()
    else:  # Sum is even, sort descending
        copy_array.sort(reverse=True)

    return copy_array

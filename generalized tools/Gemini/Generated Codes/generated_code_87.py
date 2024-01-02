
def get_row(lst, x):
    """
    Finds coordinates of integer x in a 2D list with varying row lengths, sorted as specified.
    """

    coordinates = []
    for row_index, row in enumerate(lst):
        for col_index, item in reversed(list(enumerate(row))):  # Reverse for descending column order
            if item == x:
                coordinates.append((row_index, col_index))

    return sorted(coordinates)  # Sort by row index in ascending order

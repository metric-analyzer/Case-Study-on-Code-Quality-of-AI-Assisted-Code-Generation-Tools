
def max_fill(grid, capacity):
    """Calculates the minimum number of bucket lowerings to empty the wells.

    Args:
        grid: A 2D list of integers representing the grid of wells, where 1
            indicates water and 0 indicates no water.
        capacity: An integer representing the capacity of each bucket.

    Returns:
        An integer representing the minimum number of bucket lowerings required.
    """

    num_wells = len(grid)
    num_units_water = sum(sum(row) for row in grid)

    if num_units_water == 0:  # Optimization for empty grid
        return 0

    total_lowerings = 0

    for row in grid:
        water_in_well = sum(row)
        num_full_buckets = water_in_well // capacity
        remaining_water = water_in_well % capacity

        total_lowerings += num_full_buckets

        # Handle remaining water
        if remaining_water > 0:
            total_lowerings += 1

    return total_lowerings

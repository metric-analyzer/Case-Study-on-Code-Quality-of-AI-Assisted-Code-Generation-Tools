
def car_race_collision(n: int) -> int:
    """
    Calculates the number of collisions between two sets of n cars moving in opposite directions.
    """

    if n == 0:
        return 0  # No cars, no collisions

    # Simulate the collisions using a list to track car positions
    car_positions = [i for i in range(n)]
    collisions = 0

    # Iterate until all cars have passed each other
    while car_positions:
        # Move cars from left to right
        for i in range(len(car_positions)):
            car_positions[i] += 1

        # Check for collisions with cars moving right to left
        for i in range(len(car_positions) - 1, -1, -1):
            if car_positions[i] == 0:
                collisions += 1
                car_positions.pop(i)  # Remove collided car

    return collisions


def fruit_distribution(s: str, n: int) -> int:
    """Calculates the number of mango fruits in the basket."""

    apples_str, oranges_str = s.split(" and ")  # Split the string into apples and oranges parts
    apple_count = int(apples_str.split()[0])  # Extract the apple count
    orange_count = int(oranges_str.split()[-1])  # Extract the orange count

    mango_count = n - apple_count - orange_count  # Calculate the mango count
    return mango_count

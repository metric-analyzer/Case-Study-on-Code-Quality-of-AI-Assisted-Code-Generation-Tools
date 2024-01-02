
def decimal_to_binary(decimal):
    """Converts a decimal number to a binary string with 'db' prefix and suffix."""

    binary = bin(decimal)[2:]  # Use built-in bin() function for conversion, remove '0b' prefix
    return f"db{binary}db"  # Add 'db' prefix and suffix

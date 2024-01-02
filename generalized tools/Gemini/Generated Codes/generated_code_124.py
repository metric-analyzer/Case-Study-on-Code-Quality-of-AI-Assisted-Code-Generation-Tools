
def valid_date(date):
    """Validates a given date string and returns True if the date is valid, otherwise False."""

    # 1. Check for empty string
    if not date:
        return False

    # 2. Split the date string into components
    try:
        month, day, year = map(int, date.split("-"))
    except ValueError:
        return False  # Invalid format

    # 3. Validate month
    if not 1 <= month <= 12:
        return False

    # 4. Validate day based on month and leap year
    if month in (1, 3, 5, 7, 8, 10, 12):
        max_days = 31
    elif month == 2:
        max_days = 29 if is_leap_year(year) else 28
    else:
        max_days = 30

    if not 1 <= day <= max_days:
        return False

    # All conditions are met, the date is valid
    return True


def is_leap_year(year):
    """Checks if a given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

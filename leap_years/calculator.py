


def calculate_leap_year(year: int) -> bool:
    if type(year) != int:
        raise TypeError("Year must be an integer")
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False
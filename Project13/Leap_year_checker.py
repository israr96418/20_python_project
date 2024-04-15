def is_leap_year(year):
     """
     Check if a given year is a leap year.
    
    Args:
        year (int): The year to be checked.
    
    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if __name__ == '__main__':
    year = int(input('Enter the year that you want to check whether it is a leap year or not: '))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

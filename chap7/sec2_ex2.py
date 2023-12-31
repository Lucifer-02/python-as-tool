import calendar as cal


def shopping_days(year: int) -> int:
    """year a number >= 1957
    returns the number of days between U.S. Thanksgiving and
            Christmas in year"""
    assert year >= 1957

    thanksgiving_day = find_thanksgiving(year)
    christmas_day = 25
    days_of_november = cal.monthrange(year, 11)[1]

    return days_of_november - thanksgiving_day + christmas_day


def find_thanksgiving(year: int):
    """return Canadian Thanksgiving day"""
    assert year > 0

    month = cal.monthcalendar(year, 10)
    if month[0][cal.MONDAY] != 0:
        thanksgiving = month[1][cal.MONDAY]
    else:
        thanksgiving = month[2][cal.MONDAY]

    return thanksgiving


year = 2023
print(f"Number of shopping days in {year} is {shopping_days(2023)}")

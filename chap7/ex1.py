import calendar as cal


def shopping_days(year: int) -> int:
    """year a number >= 1941
    returns the number of days between U.S. Thanksgiving and
            Christmas in year"""
    assert year >= 1941

    thanksgiving_day = find_thanksgiving(year)
    christmas_day = 25
    days_of_november = cal.monthrange(year, 11)[1]

    return days_of_november - thanksgiving_day + christmas_day


def find_thanksgiving(year: int):
    month = cal.monthcalendar(year, 11)
    if month[0][cal.THURSDAY] != 0:
        thanksgiving = month[3][cal.THURSDAY]
    else:
        thanksgiving = month[4][cal.THURSDAY]
    return thanksgiving


year = 2011
print(f"Number of shopping days in {year} is {shopping_days(2023)}")

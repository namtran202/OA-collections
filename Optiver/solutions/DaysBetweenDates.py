def daysBetweenDates(date1: str, date2: str) -> int:
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def get_days(date):
        y, m, d = date.split("-")
        y = int(y)
        m = int(m)
        d = int(d)
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = d

        if is_leap_year(y) and m > 2:
            days += 1

        for year in range(1971, y):
            if is_leap_year(year):
                days += 366
            else:
                days += 365

        if m != 1:
            for month in months[:m - 1]:
                days += month

        return days

    return abs(get_days(date1) - get_days(date2))
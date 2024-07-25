class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f"{self.day:02d}-{self.month:02d}-{self.year}"


def parse_date(date_str):
    day, month, year = map(int, date_str.split('-'))
    return Date(day, month, year)


# def date_comparator(date1, date2):
#     if date1.year != date2.year:
#         return date1.year - date2.year
#     if date1.month != date2.month:
#         return date1.month - date2.month
#     return date1.day - date2.day


def find_third_latest_date(dates):
    # Sort the dates using the custom comparator
    dates.sort(key=lambda date: (date.year, date.month, date.day), reverse=True)
    # Return the third-latest date
    return dates[2]


# Example usage
dates_input = ["14-04-2001", "29-12-2061", "21-10-2019", "07-01-1973", "19-07-2014", "11-03-1992", "21-10-2019"]
dates = [parse_date(date_str) for date_str in dates_input]
third_latest_date = find_third_latest_date(dates)
print(third_latest_date)

# Generator that generates seconds from 0 - 59
def gen_secs():
    for second in range(60):
        yield second


# Generator that generates minutes from 0 - 59
def gen_mins():
    for minute in range(60):
        yield minute


# Generator that generates hours from 0 - 23
def gen_hour():
    for hour in range(24):
        yield hour


# Generator that generates all clock times from 00:00:00 to 23:59:59
def gen_time():
    for hour in gen_hour():
        for minute in gen_mins():
            for second in gen_secs():
                yield f"{hour:02d}:{minute:02d}:{second:02d}"


# Generator that generates all years from current year and forward
def gen_years(start=2024):
    while True:
        yield start
        start += 1


# Generator that generates all months in the year 1 - 12
def gen_months():
    for month in range(1, 13):
        yield month


# Generator that generates all days in a specific month considering leap years
def gen_days(month, leap_year):
    # Dictionary for month - days in month
    days_in_month = {
        1: 31,
        2: 29 if leap_year else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    for day in range(1, days_in_month[month] + 1):
        yield day


# Generator that generates all dates with clock time 00:00:00 and forward
def gen_date():
    for year in gen_years(2019):
        # For each year check for a leap year
        leap_year = (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield f"{day:02d}/{month:02d}/{year:04d} {time}"


def main():
    count = 0  # Counter for current next method call
    for date in gen_date():  # Generate all dates
        count += 1
        if count % 1000000 == 0:  # Every 1000000 calls print the date
            print(date)


if __name__ == '__main__':
    main()

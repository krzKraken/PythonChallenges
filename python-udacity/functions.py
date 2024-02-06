def date_format(days):
    weeks = int(days/7)
    days = days % 7
    return "{} week(s) and {} day(s).".format(weeks, days)

print(date_format(10))



import calendar

day, month, year = map(int, input('dd.mm.yyyy').split('.'))
print(calendar.day_name[calendar.weekday(year, month, day)])

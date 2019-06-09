import calendar

_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

day, month, year = map(int, input('dd.mm.yyyy').split('.'))
print(_dict.get(calendar.weekday(year, month, day)))

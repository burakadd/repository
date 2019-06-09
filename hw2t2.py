import calendar
import datetime

_this_year, _this_month = datetime.datetime.today().year, datetime.datetime.today().month
_user_day = input('Enter the day of the week: ')
_days = {day: number for number, day in enumerate(calendar.day_name)}


def _date_iter(year, month):
    while year >= 1970:
        yield year, month
        month -= 1
        if not month:
            year -= 1
            month = 12
    else:
        print("It's too difficult")


for i in _date_iter(_this_year, _this_month):
    if calendar.weekday(*i, 1) == _days[_user_day]:
        print(*i)
        break

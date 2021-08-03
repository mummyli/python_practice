from datetime import date, datetime, time, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)

    # 返回本月包含的周数和本月天数
    _, month_days = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days = month_days)
    return start_date, end_date

a_day = timedelta(days=1)

first_day, last_day = get_month_range()

while first_day < last_day:
    print(first_day)
    first_day += a_day
from datetime import datetime, time, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()

    day_num = start_date.weekday()
    day_target_num = weekdays.index(dayname)
    days_ago = (day_num + 7 - day_target_num) % 7

    if days_ago == 0:
        days_ago = 7

    target_date = start_date - timedelta(days=days_ago)
    return target_date

print(get_previous_byday("Wednesday"))

# 使用Dateutil模块计算
from dateutil.relativedelta import FR, relativedelta
d = datetime.now()

print(d + relativedelta(weekday=FR))
print(d + relativedelta(weekday=FR(-1)))
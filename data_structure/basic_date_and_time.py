from datetime import date, datetime, timedelta

# 表示时段
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)

c = a + b

print(c)
print(c.days)
print(c.seconds)
print(c.total_seconds())

# datetime创建指定日期
a = datetime(2012, 9, 23)
b = datetime(2012, 12, 21)

print(a + timedelta(days=2, hours=5))

d = b-a
print(d.days)

# 当前时间
now = datetime.now()
print(now)

# 本天
today = datetime.today()
print(today)

print("-" * 40)
# 对于复杂的时间处理 使用dateutil模块

from dateutil.relativedelta  import relativedelta

a = datetime(2012, 9, 23)
print(a + relativedelta(months = +2))

b = datetime(2012, 12, 21)
print(relativedelta(b, a))
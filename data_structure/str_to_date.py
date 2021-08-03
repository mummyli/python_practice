from datetime import datetime

# 字符串转日期  性能很差
str = "2021-08-03"
print(datetime.strptime(str, "%Y-%m-%d"))

# 日期转字符串
now = datetime.today()
print(datetime.strftime(now, "%Y-%m-%d"))
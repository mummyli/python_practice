# str.replace() 进行简单替换 该方法返回一个新的字符串
text = "yeah, but no, but yeah, but no, but yeah"
new_text = text.replace("yeah", "yep")
print(new_text)

import re
# re.sub() 替换复杂模式
# 参数1：分组匹配；参数2：对匹配分组进行调整
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub("(\d{1,2})/(\d{1,2})/(\d{4})", r"\3-\1-\2", text))


# 可以传入回调函数 进行复杂替换
from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

subpatt = re.compile("(\d{1,2})/(\d{1,2})/(\d{4})")
print(subpatt.sub(change_date, text))
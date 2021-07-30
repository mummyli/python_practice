text = 'yeah, but no, but yeah, but no, but yeah'

# find()返回首次发现的位置索引
print(text.find("no"))

import re
# 复杂匹配使用 re 模块
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

print(re.match(r"\d{2}/\d{2}/\d{4}", text1))
print(re.match(r"\d{2}/\d{2}/\d{4}", text2))

# 一个模式多次匹配，可先compile
patt = re.compile("\d{1,2}/\d{1,2}/\d{4}")
print(patt.match(text1))


print("+" * 50)
# match()总是从字符串开始位置去匹配
# 任意位置匹配使用findall()
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(patt.match(text))
print(patt.findall(text))
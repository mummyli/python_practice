# str的lstrip和rstrip，左右删除字符 默认空白字符 也可指定字符
# strip两端同时
s1 = "---- hello ---- world -----"
print(s1.lstrip("-"))
print(s1.rstrip("-"))
print(s1.strip("-"))

# replace()替换任意位置字符
print(s1.replace("-", '+'))

# re.sub通过正则替换
import re
print(re.sub("\s+", "", s1))
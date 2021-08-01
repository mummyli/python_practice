import re

# 默认情况下 .  不会匹配换行
text = ''''/* this is a comment
with multi lines */
'''
pat = re.compile("/\*(.*)\*/")
print(pat.findall(text))

print("-" * 50)
# 1、显示的指定换行符
pat = re.compile("/\*((?:.|\n)*)\*/")
print(pat.findall(text))

# 2、设置re.DOTALL标志
pat = re.compile("/\*(.*)\*/", flags=re.DOTALL)
print(pat.findall(text))
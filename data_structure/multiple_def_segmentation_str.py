import re

# str.split()只适用于简单的字符串分割
line = 'asdf fjdk; afed, fjek,asdf, foo'

result = re.split("[\s;,]\s*", line)
print(result)

# 如果使用了捕获分组， 那么分组匹配也会出现
result = re.split("(\s|,|;)\s*", line)
print(result)
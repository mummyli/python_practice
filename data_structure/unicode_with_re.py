import re

# 默认支持部分unicode字符
num_pat = re.compile("\d+")
print(num_pat.match('\u0661\u0662\u0663'))

# 使用Unicode字符对应的转义序列指定Unicode字符
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s))
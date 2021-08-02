x = 1234.56789

# 保留两位小数
print(format(x, '0.2f'))

# 向右补齐10位字符，保留两位小数
print(format(x, "->10.2f"))

# 向左补齐10位字符，保留两位小数
print(format(x, "-<10.2f"))

# 居中补齐10位字符，保留两位小数
print(format(x, "-^10.2f"))

# 加入千分位分隔符
print(format(x, ",.1f"))

# 指数计数法，f改为e或E
print(format(x, ".1e"))
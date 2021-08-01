# ljsut rjust center

s = "hello"

print(s.ljust(20, "="))
print(s.rjust(20, "="))
print(s.center(20, "="))

# format(): < 左对齐  >右对齐  ^居中
print(format(s, "*<20"))
print(format(s, "*>20"))
print(format(s, "*^20"))

# 格式化多个值
print('{:>10s} {:->10s}'.format('Hello', 'World'))
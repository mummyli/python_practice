# 正无穷
a = float("inf")

# 负无穷
b = float("-inf")

# Nan
c = float("nan")

# 测试这些值
import math
print(math.isinf(a))
print(math.isnan(c))

# 无穷大数在执行数学计算时会传播
print(a+46)
print(a-45)
print(a/45)
print(45/a)
print(a*45)

# nan值在数学计算时也会传播, 所有nan值的比较结果都是false
c = float("nan")
d = float("nan")
print(c == d)
print(round(1.23, 1))
print(round(1.36, 1))

# round传入负数  会作用于十分位、百分位等
print(round(123868, -1))
print(round(123868, -2))


# 如果只是格式化输出  使用format
x = 1.23456
print(format(x, '0.2f'))
print(format(x, '0.3f'))
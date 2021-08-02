x = 1234

# 二进制
print(bin(x))

# 八进制
print(oct(x))

# 十六进制
print(hex(x))

# 去掉0b,0o,0x可使用format
x1 = format(x, 'b')
print(x1)

print(format(x, 'o'))
print(format(x, 'x'))
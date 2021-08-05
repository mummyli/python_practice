import os

path1 = "D:/pyworkspace/python_practice/testfiles/passwd.txt"
path2 = "D:/pyworkspace/"

# 测试文件或者路径是否存在
print(os.path.exists(path1))
print(os.path.exists(path2))

# 判断是否是文件
print(os.path.isfile(path1))

# 判断是否是目录
print(os.path.isdir(path2))

# 判断是否是符号链接
print(os.path.islink(path2))

# 获取链接的实际路径
print(os.path.realpath(path2))
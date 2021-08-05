import os

path = "D:/pyworkspace/python_practice/testfiles/passwd.txt"

# 获取文件名
print(os.path.basename(path))

# 获取目录路径
print(os.path.dirname(path))

# 拼接路径
print(os.path.join("tmp", "data", os.path.basename(path)))

path2 = '~/Data/data.csv'

print(os.path.expanduser(path2))

print(os.path.splitext(path))
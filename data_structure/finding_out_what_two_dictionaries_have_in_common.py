a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# 查找相同的key
print(a.keys() & b.keys())

# 查找在a 但是不在b的key
print(a.keys() - b.keys())

# 查找a和b的相同项
print(a.items() & b.items())

# 结合字典生成器表达式过滤字典
result = {key: a[key] for key in a.keys() - b.keys()}
print(result)
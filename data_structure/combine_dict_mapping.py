from collections import ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

# ChainMap逻辑上将多个字典变成一个字典
# 如果出现重复键，那么第一次出现的映射值会被返回。
c = ChainMap(a, b)
print(c)
for key, value in ChainMap(a, b).items():
    print(key, ":", value)


# update来合并两个字典
# 重复键 保留最后一个
mergeddict = dict(a)
mergeddict.update(b)
print(mergeddict)
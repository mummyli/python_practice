xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99, 4, 55, 23]

for x, y in zip(xpts, ypts):
    print(x, y)

# zip生成一个可以返回元组的迭代器， 某个序列到结尾，则迭代结束
# iteraltools.zip_longest()会以最长的序列为准
import itertools
for i in itertools.zip_longest(xpts, ypts):
    print(i)


# 可以利用zip来生一个字典
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]

d = dict(zip(headers, values))
print(d)
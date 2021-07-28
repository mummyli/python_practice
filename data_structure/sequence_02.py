'''
1、元组拆包
'''
from collections import deque


data = ["ACME", 50, 1.9, (2019, 2, 5)]
name, shares, price, date = data

name, shares, price, (year, month, day) = data

# 通过占位符 “_” 丢弃不需要的值
name, shares, _, date = data

# 解压赋值多个变量
data = ("David", "082-222352", "010-989234", "028-222999")
name, *phones = data
print(phones)

print("+" * 20)
'''
2、deque
'''
# 构造固定大小队列
# 不指定大小maxlen 则构建无限队列
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print("append 3 items: ", q)
q.append(4)
print("append one item: ", q)
q.appendleft(5)
print("append left: ", q)
q.pop()
print("pop one item: ", q)
q.popleft()
print("popleft : ", q)
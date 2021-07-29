from collections import namedtuple

# 传入list
Subscriber = namedtuple("Subscriber", ["addr", "joined"])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)

# 或者是空格分隔的字符串
Subscriber = namedtuple("Subscriber", "addr joined")
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)

# 元组的操作同样适用于命名元组
addr, joined = sub

# 命名元组的值跟元组一样是不能修改的
# 可以用_replace()方法修改一个元组的某个属性， 它会创建一个全新的命名元组并将对应的字段用新的值取代。

sub = sub._replace(joined="2017-02-11")
print(sub)
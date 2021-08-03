a = [1, 2, 3, 4]

# 反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效。
for i in reversed(a):
    print(i)


print("-" * 20)
# 自定义 __reversed__()实现反向迭代
class Countdown:
    def __init__(self, start) -> None:
        self.start = start

    def __iter__(self):
        n = self.start
        while n>0:
            yield n
            n -=1

    def __reversed__(self):
        n = 1
        while n < self.start:
            yield n
            n += 1

for i in reversed(Countdown(5)):
    print(i)
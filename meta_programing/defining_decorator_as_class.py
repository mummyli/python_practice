import types
from functools import wraps

'''
为了将装饰器定义为类，要确保实现了__call__()和__get__()方法
'''
class Profiled:
    def __init__(self, func) -> None:
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwds):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwds)

    def __get__(self, instance, cls):
        if instance is None:
            print(">>>> instance is None")
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x+y

result = add(1, 2)
result = add(3, 4)
result = add(5, 6)

print(add.ncalls)

class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


s = Spam()
s.bar(1)

Spam.bar(None, 2)

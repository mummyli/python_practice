class A:
    def spam(self):
        print("A.spam()")
    
    def foo(self):
        print("A.foo()")


'''
使用__getattr__()， 当访问的属性不存在时会被调用
'''
class B:
    def __init__(self) -> None:
        self._a = A()

    def __getattr__(self, name):
        return getattr(self._a, name)

b = B()
b.spam()


'''
实现代理模式
'''
class Proxy:
    def __init__(self, obj) -> None:
        self._obj = obj

    def __getattr__(self, name):
        print("getattr: ", name)
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            print("setattr:", name, value)
            setattr(self._obj, name, value)
            
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)

class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)

s = Spam(2)
p = Proxy(s)

print(p.x)
p.bar(3)
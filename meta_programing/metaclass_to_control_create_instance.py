'''
定义元类并实现call方法
'''

class NoInstance(type):
    '''
    禁止创建实例
    '''
    def __call__(self, *args, **kwds):
        raise TypeError("Can't instantiate directly")


class Spam(metaclass=NoInstance):
    @staticmethod
    def grok(x):
        print("Spam.grok")

# 无法创建 s = Spam()

class Singleton(type):
    '''实现单例模式
    '''
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self._instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self._instance

class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')

a = Spam()
b = Spam()
print(a is b)


print("-" * 30)

import weakref
class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj

class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name

a = Spam('Guido')
b = Spam('Diana')
c = Spam('Guido')

print(a is b)
print(a is c)

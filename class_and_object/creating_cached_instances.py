import weakref

class Spam:
    def __init__(self, name) -> None:
        self.name = name

_spam_cache = weakref.WeakValueDictionary()

def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]

    return s

a = get_spam("foo")
b = get_spam("bar")
if a is b:
    print("True")
else:
    print("False")

c = get_spam("foo")
if a is c:
    print("True")
else:
    print("False")

print("-" * 20)

class Spam2:
    _spam_cache = weakref.WeakValueDictionary()
    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self

    def __init__(self, name) -> None:
        print('Initializing Spam')
        self.name = name

# 缺点是每次都会进行初始化
s = Spam2("Dave")
t = Spam2("Dave")
print(s is t)

print("-" * 20)

class CachedSpamManager:
    def __init__(self) -> None:
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam3(name)
            self._cache[name] = s
        else:
            s = self._cache[name]

        return s
    
    def clear(self):
        self._cache.clear()

class Spam3:
    manager = CachedSpamManager()
    def __init__(self, name) -> None:
        self.name = name

def get_spam(name):
    return Spam3.manager.get_spam(name)
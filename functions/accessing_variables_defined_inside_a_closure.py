def sample():
    n = 0
    # Closure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func

f = sample()
print(f())
f.set_n(10)
print(f.get_n())

print("-" * 80)

import sys
class ClosureInstance:
    def __init__(self, locals = None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        self.__dict__.update((key, value) for key, value in locals.items()
                             if callable(value))
    
    def __len__(self):
        return self.__dict__["__len__"]()


def stack():
    items = []
    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()

s = stack()
s.push("aa")
s.push("bbb")
s.push("cc")
print(s.pop())

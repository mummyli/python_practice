class Integer:
    def __init__(self, name) -> None:
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance ,value):
        if not isinstance(value, int):
            raise TypeError("expected an int")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer("x")
    y = Integer("y")
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.x)
print(type(p.x))
p.y = 3.4


print("-" * 60)

class Typed:
    def __init__(self, name, expected_type) -> None:
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError("expected " + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


def typeassert(*kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate

@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
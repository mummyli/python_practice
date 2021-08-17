import types

def __init__(self, name, share, price):
    self.name = name
    self.share = share
    self.price = price

def cost(self):
    return self.share * self.price

cls_dict = {
    "__init__": __init__,
    "cost": cost
}

Stock = types.new_class("Stock", (), {}, lambda ns: ns.update(cls_dict))
# 每次当一个类被定义后，它的 __module__ 属性包含定义它的模块名。 这个名字用于生成 __repr__() 方法的输出。
Stock.__module__ = __name__

s = Stock("ACME", 100, 91.1)
print(s.cost())

print("-" * 50)

import operator
import sys

def named_tuple(clsname, fieldnames):
    cls_dict = {name: property(operator.itemgetter(n))
                for n, name in enumerate(fieldnames)}

    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        return tuple.__new__(cls, args)

    cls_dict["__new__"] = __new__

    cls = types.new_class(clsname, (tuple,), {}, lambda ns: ns.update(cls_dict))
    cls.__module__ = sys._getframe(1).f_globals["__name__"]

    return cls

Point = named_tuple('Point', ['x', 'y'])
p = Point(4, 5)
print(p)
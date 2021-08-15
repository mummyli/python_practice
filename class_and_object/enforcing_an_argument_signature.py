from inspect import Parameter, Signature

def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
             for name in names]
    return Signature(parms)


class Structure:
    __signature__ = make_sig()
    def __init__(self, *args, **kwargs):
        bound_value = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_value.arguments.items():
            setattr(self, name, value)

class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')

class Point(Structure):
    __signature__ = make_sig('x', 'y')

'''
通过元类来创建签名对象
'''
class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict["__signature__"] = make_sig(*clsdict.get("_fields", []))
        return super().__new__(cls, clsname, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)

# Example
class Stock2(Structure):
    _fields = ['name', 'shares', 'price']

class Point2(Structure):
    _fields = ['x', 'y']
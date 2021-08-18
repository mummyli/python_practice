import inspect
import types
from typing import Type

class MultiMethod:
    def __init__(self, name):
        self._methods = {}
        self.__name__ = name

    def register(self, meth):
        sig = inspect.signature(meth)

        types = []

        for name, parm in sig.parameters.items():
            if name == "self":
                continue
            if parm.annotation is inspect.Parameter.empty:
                raise TypeError(
                    "Argument {} must be annotated with a type".format(name)
                )
            if not isinstance(parm.annotation, type):
                raise TypeError(
                    "Argument {} annotation must be a type".format(name)
                )
            if parm.default is not inspect.Parameter.empty:
                self._methods[tuple(types)] = meth
            types.append(parm.annotation)

        self._methods[tuple(types)] = meth

    def __call__(self, *args):
        types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types, None)
        if meth:
            return meth(*args)
        else:
            raise TypeError("No matching methods for types {}".format(types))

    def __get__(self, instance, cls):
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self

class MultiDict(dict):
    def __setitem__(self, key, value):
        if(key in self):
            current_value = self[key]
            if isinstance(current_value, MultiMethod):
                current_value.register(value)
            else:
                mvalue = MultiMethod(key)
                mvalue.register(current_value)
                mvalue.register(value)
                super().__setitem__(key, value)
        else:
            super().__setitem__(key, value)


class MultipleMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        return type.__new__(cls, clsname, bases, dict(clsdict))

    @classmethod
    def __prepare__(cls, clsname, bases):
        return MultiDict()

class Spam(metaclass=MultipleMeta):
    def bar(self, x:int, y:int):
        print('Bar 1:', x, y)

    def bar(self, s:str, n:int = 0):
        print('Bar 2:', s, n)

print(Spam.__dict__)
# Example: overloaded __init__
import time

class Date(metaclass=MultipleMeta):
    def __init__(self, year: int, month:int, day:int):
        self.year = year
        self.month = month
        self.day = day

    def __init__(self):
        t = time.localtime()
        self.__init__(t.tm_year, t.tm_mon, t.tm_mday)

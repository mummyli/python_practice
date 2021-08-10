from typing import Dict


class LoggedMappingMixin:
    # 混入类都没有实例变量，因为直接实例化混入类没有任何意义
    __slots__ = ()

    def __getitem__(self, key):
        print("Getting " + str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print("Setting {} = {!r}".format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print("Deleting " + str(key))
        return super().__delitem__(key)


class SetOnceMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + " already set")
        
        super().__setitem__(key, value)

class StringKeysMappingMixin:
    __slots__=()

    def __setitem__(self, key, value):
        if key in self:
            raise TypeError("keys must be string")
        super().__setitem__(key, value)


class LoggedDict(LoggedMappingMixin, Dict):
    pass

d = LoggedDict()
d["X"] = 21
print(d["X"])
del d["X"]
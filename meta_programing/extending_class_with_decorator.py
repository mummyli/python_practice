def log_getattribute(cls):
    orig_getattribute = cls.__getattribute__

    def new_getattribute(self, name):
        print("getting ", name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = new_getattribute
    return cls


@log_getattribute
class A:
    def __init__(self, x) -> None:
        self.x = x

    def spam(self):
        print(">>>>")

a = A(2)
a.x
a.spam()
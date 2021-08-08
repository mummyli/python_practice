class Person:
    def __init__(self, first_name:str) -> None:
        self._first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("expected a str!")

        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("cannot delete!")


p = Person("Jon")
print(p.first_name)
p.first_name = 22

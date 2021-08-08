from typing import Type


class Person:
    def __init__(self, name) -> None:
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("expected a str!")
        
        self._name = value

    
    @name.deleter
    def name(self):
        raise AttributeError("can not delete!")


class SubPerson(Person):
    @property
    def name(self):
        print("Getting name")
        return super().name

    @name.setter
    def name(self, value):
        print("setting name to ", value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print("Deleting name")
        super(SubPerson, SubPerson).name.__delete__(self)


'''
如果仅仅是想扩展某一方法
'''
class SubPerson2(Person):
    @Person.name.setter
    def name(self, value):
        print("setting name to ", value)
        super(SubPerson, SubPerson).name.__set__(self, value)
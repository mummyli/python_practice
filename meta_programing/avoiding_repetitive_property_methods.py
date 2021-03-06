def typed_property(name, expected_type):
    storage_name = "_" + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError("{} must be a {}".format(name, expected_type))
        setattr(self, storage_name, value)

    return prop

class Person:
    name = typed_property("name", str)
    age = typed_property("age", int)

    def __init__(self, name, age):
        self.name = name
        self.age = age
class lazyproperty:
    def __init__(self, func) -> None:
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @lazyproperty
    def area(self):
        print("Computing area")
        return math.pi * self.radius**2

c = Circle(5)
print(c.radius)
print(">>>> ", vars(c))
print(c.area)
print(c.area)
print(">>>> ", vars(c))
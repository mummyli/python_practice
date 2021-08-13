import time
from functools import wraps


def thistime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result

    return wrapper


class Spam:
    @thistime
    def instance_mth(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @thistime
    def class_mth(cls, n):
        print(cls, n)
        while(n>0):
            n -= 1

    @staticmethod
    @thistime
    def static_mth(n):
        print(n)
        while(n>0):
            n -= 1

s = Spam()
s.instance_mth(500000)
Spam.class_mth(500000)
Spam.static_mth(5000000)
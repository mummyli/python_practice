import time
from functools import wraps

def timethis(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(func.__name__, end - start)
        return result
    return wrapper


@timethis
def countdown(n):
    while n>0:
        n -= 1

countdown(50000)

print("-" * 50)

# __wrapped__访问原始函数
countdown.__wrapped__(50000)

# 但是当同时存在多个装饰器的时候 __wrapped__属性的行为是不可预知的 应该避免这样做
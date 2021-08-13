from functools import wraps

def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print("Calling ", func.__name__)
        return func(*args, **kwargs)

    return wrapper

@optional_debug
def add(x, y):
    return x + y

result = add(1, 2)
print(result)
print("-" * 30)
result = add(1, 2, debug=True)
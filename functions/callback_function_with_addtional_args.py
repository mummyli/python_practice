def apply_async(func, args, callback):
    result = func(*args)

    callback(result)


def add(x, y):
    return x + y

def print_result(result):
    print("GOT: {}".format(result))

apply_async(add, (2, 3), print_result)

print("-" * 80)

class ResultHandler:
    def __init__(self) -> None:
        self.sequence = 0

    def handler(self, result: int) -> None:
        self.sequence += 1
        print("[{}] Got: {}".format(self.sequence, result))


r = ResultHandler()

apply_async(add, (3, 4), r.handler)
apply_async(add, (5, 6), r.handler)

print("-" * 80)

# 使用闭包来保存状态
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print("[{}] Got: {}".format(sequence, result))
    
    return handler

handler = make_handler()
apply_async(add, (3, 4), handler)
apply_async(add, (5, 6), handler)

print("-" * 80)

# 使用协程
def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print("[{}] Got: {}".format(sequence, result))

handler = make_handler()
next(handler)
apply_async(add, (3, 4), handler.send)
apply_async(add, (5, 6), handler.send)
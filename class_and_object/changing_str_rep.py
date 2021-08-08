class Pair:
    '''
    __repr__()返回一个实例的代码表示形式， 通常用来重新构造这个实例
    __str__()将实例转换为字符串
    如果没有定义__str__()，那么在print时会使用__repr__()来代替
    '''
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "Pair({0.x!r}, {0.y!r})".format(self)

    def __str__(self) -> str:
        return "({0.x!r}, {0.y!r})".format(self)


p = Pair(3, 4)
print(repr(p))
print(p)
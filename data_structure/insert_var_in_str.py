s = '{name} has {n} messages.'

print(s.format(name="Guio", n=37))
print(s.format(n=37, name="Guio"))

# 如果能在变量域中找到，可以结合使用format_map和vars()
name = "Jack"
n = 15

print(s.format_map(vars()))

# var() 同样适用于对象实例
class Info:
    def __init__(self, name, n) -> None:
        self.name = name
        self.n = n

info  = Info("Mical", 22)
print(s.format_map(vars(info)))
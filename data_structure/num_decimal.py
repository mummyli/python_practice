from decimal import Decimal, localcontext

a = Decimal("1.3")
b = Decimal("1.7")

print(a+b)

print(a/b)

with localcontext() as ctx:
    ctx.prec = 5
    print(a/b)

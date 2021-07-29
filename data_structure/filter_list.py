mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print([val for val in mylist if val>0])

print("+" * 40)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

isvals = list(filter(is_int, values))
print(isvals)

print("+" * 40)
# 通过生成器表达式转换元素
print([n if n>0 else 0 for n in mylist])

print("+" * 40)
# 通过Boolean序列来过滤序列
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n>5 for n in counts]

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

from itertools import compress

print(list(compress(addresses, more5)))
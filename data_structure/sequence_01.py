'''
根据容纳类型分类：
    1、容器序列：list、collection.deque、tuple
    2、扁平序列：array.array、bytearray、memoryview、str、bytes

根据是否可变分类：
    1、可变序列(MultableSequence): list、collection.deque、array.array、bytearray、memoryview
    2、不可变序列(Sequence): tuple、str、bytes

'''

'''
1、列表推导
   通常原则是：只用列表推导创建新的列表，并尽量保持简短。
'''
symbols="#$%^&*("
codes = [ord(symbol) for symbol in symbols]
print(codes)

'''
2、与filter和map的比较
'''
# 通过列表推导来过滤
beyond_ascii = [ord(symbol) for symbol in symbols if (ord(symbol)>=40)]
print(beyond_ascii)

# 通过filter和map来过滤
beyond_ascii = list(filter(lambda c: c>=40, map(ord, symbols)))
print(beyond_ascii)

'''
3、列表推导构建笛卡儿积
'''
colors = ["black", "white"]
sizes = ["S", "M", "L"]
tshirts = [(c, s) for c in colors
                  for s in sizes]
print(tshirts)

'''
4、生成器表达式
'''
gen_shirts = ((c, s) for c in colors
                     for s in sizes)
print(gen_shirts)
for i in gen_shirts:
    print(i)
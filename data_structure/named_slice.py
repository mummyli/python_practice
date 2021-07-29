record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])

print(cost)

# slice: slice(start, stop, step). step默认为1
items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = slice(2, 10, 2)
print(items[a])

del items[a]
print(items)

b = slice(2, 50, 3)
print(items[b])
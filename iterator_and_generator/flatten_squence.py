from collections.abc import Iterable

def flatten(items, ignore_typs = (str, bytes)):
    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, ignore_typs):
            yield from flatten(item)
        else:
            yield item

items = [1, 2, [3, 4, [5, 6], 7], 8]

for x in flatten(items):
    print(x, end=" ")
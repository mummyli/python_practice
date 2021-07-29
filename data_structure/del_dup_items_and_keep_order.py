# 元素可hash的
def dequeue(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dequeue(a)))

# 元素不可hash，例如dict
def dequeue(items, key):
    seen = set()
    for item in items:
        val = key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dequeue(a, key=lambda d: (d["x"],d["y"]))))
print(list(dequeue(a, key=lambda b: b["x"])))
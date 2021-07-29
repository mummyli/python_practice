from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

sorted_rows = sorted(rows, key = itemgetter("uid"))
print(sorted_rows)
# 也可以指定多个key
sorted_rows = sorted(rows, key = itemgetter("uid", "fname"))
print(sorted_rows)

# lambda的区别：
# itemgetter速度会稍微快一点
sorted_rows = sorted(rows, key=lambda v: v["uid"])
print(sorted_rows)
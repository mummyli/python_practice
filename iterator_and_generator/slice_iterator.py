import itertools

def unlimit_count(n):
    while True:
        yield n
        n += 1

for x in itertools.islice(unlimit_count(2), 5, 10):
    print(x)
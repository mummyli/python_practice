def frang(start, stop, step):
    x = start
    while x<stop:
        yield x
        x += step

for i in frang(1, 10, 2):
    print(i) 
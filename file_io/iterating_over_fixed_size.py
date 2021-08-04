from functools import partial

RECORD_SIZE=32
# iter() 函数有一个鲜为人知的特性就是，如果你给它传递一个可调用对象和一个标记值，它会创建一个迭代器。 这个迭代器会一直调用传入的可调用对象直到它返回标记值为止，这时候迭代终止。
with open("./testfiles/data.bin", "rb") as f:
    records = iter(partial(f.read, RECORD_SIZE), b"")

    for x in records:
        print(x)
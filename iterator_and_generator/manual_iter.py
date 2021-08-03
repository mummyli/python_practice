# 使用next并捕获StopIteration异常
def manual_iter():
    with open("./testfiles/somefile.txt") as f:
        try:
            while True:
                line = next(f)
                print(line)
        except StopIteration:
            print("-"*40)
            print("catch StopIteration!")
            print("-"*40)

manual_iter()

print("="*80)
# 使用指定值来标记结尾
def manual_iter2():
    with open("./testfiles/somefile.txt") as f:
        while True:
            line = next(f, None)

            if line is None:
                break
            print(line)

manual_iter2()
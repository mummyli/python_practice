from collections import deque

def search(lines, pattern, history=5):
    pre_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, pre_lines
        pre_lines.append(line)


if __name__ == "__main__":
    with open(r"testfiles\somefile.txt", "r") as f:
        for lines, prevlines in search(f, "python", 7):
            for pline in prevlines:
                print(pline, end=" ")
            print(lines, end=" ")
            print("-" * 20)
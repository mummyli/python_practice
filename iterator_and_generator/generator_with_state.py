from collections import deque

class Linehistory:
    def __init__(self, lines, histlen = 3) -> None:
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines):
            self.history.append((lineno, line))
            yield line

with open("./testfiles/somefile.txt") as f:
    l = Linehistory(f)
    for line in l:
        if "python" in line:
            for lineno, line in l.history:
                print("{} : {}".format(lineno, line))
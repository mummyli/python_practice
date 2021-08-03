from itertools import dropwhile

with open("./testfiles/passwd.txt") as f:
    for line in dropwhile(lambda line:line.startswith('#'), f):
        print(line, end="")
# startswith
# endswith
filename = "spam.txt"
print(filename.endswith(".txt"))

filename = "http://www.python.org"
print(filename.startswith("http:"))

# 也可以指定多个匹配项， 放入元组中
files = [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
filterfiles = [f for f in files if f.endswith((".py", ".c"))]
print(filterfiles)
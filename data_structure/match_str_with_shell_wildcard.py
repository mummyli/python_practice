from fnmatch import fnmatch, fnmatchcase

# fnmatch会使用操作系统底层的大小写规则来匹配模式
print(fnmatch("foo.txt", "*.txt"))
print(fnmatch("foo.txt", "?oo.txt"))
print(fnmatch("Dat45.txt", "Dat[0-9]*.txt"))

print(fnmatch("spam.txt", "*.TxT")) # windows是True, ubuntu是False

# fnmatchcase全使用你的模式大小写匹配
print(fnmatchcase('foo22.txt', '*.TXT'))
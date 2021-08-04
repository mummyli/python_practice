# 读取文本
'''
Character	Meaning
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	create a new file and open it for writing
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)
'U'	universal newline mode (deprecated)
'''
from os import write

filename = "./testfiles/somefile.txt"
with open(filename, "rt") as f:
    # 一次性读取所有内容
    data = f.read()
    print(data)

with open(filename, "rt") as f:
    # 按行迭代读取
    for line in f:
        print(line)

# 覆盖并且写入
with open("./testfiles/somefile2.txt", "wt") as f:
    f.write("new line")

# 指定编码
with open(filename, "rt", encoding="GBK") as f:
    # 按行迭代读取
    for line in f:
        print(line)

# 处理编码错误：
# 1、open('sample.txt', 'rt', encoding='ascii', errors='replace')
# 2、open('sample.txt', 'rt', encoding='ascii', errors='ignore')
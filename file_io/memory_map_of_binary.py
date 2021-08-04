import os
import mmap
'''
内存映射文件并不会将整个文件读取到内存，
仅仅为文件保留一段虚拟内存，
当访问不同区域时，该部分内容才加载到内存中
'''

filename = "./testfiles/data"
# 初始化文件
size = 1000000
with open(filename, "wb") as f:
    f.seek(size-1)
    f.write(b'\x00')


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)

    return mmap.mmap(fd, size, access=access)

m = memory_map(filename)
print(len(m))
print(m[0:11])

m[0:11] = b"hello world"
m.close()

# mmap也可以作为一个上下文管理器使用
with memory_map(filename) as m:
    print(m[0:11])
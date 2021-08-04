import os

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    # readinto()方法为预先分配内存的数据填充数据， 填充已存在的缓冲区， 避免大量的内存分配
    with open(filename, "rb") as f:
        l = f.readinto(buf)
        print("read length: ", l)
    
    return buf

buf = read_into_buffer("./testfiles/data.bin")
print(buf)

# 使用readinto()需要时刻关注读取的实际字节数 以此来判断读取结束
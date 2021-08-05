import urllib.request
import io


# 为二进制模式打开的IO添加unicode编码
u = urllib.request.urlopen("http://juejin.im/")
f = io.TextIOWrapper(u, encoding="utf-8")
print(f.read())
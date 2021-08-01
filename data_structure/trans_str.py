s = 'pýtĥöñ\fis\tawesome\r\n'
print("source str: ", s)

# clean blank char
remap = {
    ord("\t"): "",
    ord("\f"): "",
    ord("\r"): None
}
a = s.translate(remap)
print("clean blan: ", a)

# 构建和音字符映射表
import unicodedata
import sys
cmb_chars = dict.fromkeys(c for c in range(sys.maxunicode)
                          if unicodedata.combining(chr(c)))

b = unicodedata.normalize("NFD", a)
b = b.translate(cmb_chars)
print("del: ", b)
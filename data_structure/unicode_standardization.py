import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1)
print(s2)
print("s1==s2? ", s1==s2)

print("-" * 50)

t1 = unicodedata.normalize("NFC", s1)
t2 = unicodedata.normalize("NFC", s2)

print("t1==t2? ", t1==t2)
print("len(t1)=", len(t1))
print("len(t2)=", len(t2))

print("-" * 50)
t1 = unicodedata.normalize("NFD", s1)
t2 = unicodedata.normalize("NFD", s2)

print("t1==t2? ", t1==t2)
print("len(t1)=", len(t1))
print("len(t2)=", len(t2))

# 也支持扩展的标准形式NFKC和NFKD。它们在处理某些字符的时候增加了额外的兼容特性。
print("-" * 50)

# combining()测试字符是否是和音字符

print(''.join(c for c in t1 if not unicodedata.combining(c)))
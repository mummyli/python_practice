import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall("python", text, flags=re.IGNORECASE))
print(re.sub("python", "snake", text, flags=re.IGNORECASE))

# sub() 与被匹配的单词保持大小写一致
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

print(re.sub("python", matchcase("snake"), text, flags=re.IGNORECASE))
import re

str_pat = re.compile("\"(.*)\"")

text = 'Computer says "no." Phone says "yes."'

print(str_pat.findall(text))

str_pat = re.compile("\"(.*?)\"")
print(str_pat.findall(text))
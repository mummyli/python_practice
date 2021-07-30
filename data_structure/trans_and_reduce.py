
nums = [1, 2, 3, 4, 5]
s = sum(x*x for x in nums)
print(s)

import os
files = os.listdir("./data_structure")

if(any(file.endswith(".py") for file in files)):
    print("exists python file!")
else:
    print("there is no python file")


## tuple to csv
s = ('ACME', 50, 123.45)
print(",".join(str(x) for x in s))

portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
print(min(s["shares"] for s in portfolio))
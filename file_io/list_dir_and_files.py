import os

path = "D:/pyworkspace/python_practice"

print(os.listdir(path))


for x in os.walk(path):
    print(x)
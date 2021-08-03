import random

values = [1, 2, 3, 4, 5, 6]

print(random.choice(values))
print(random.sample(values, 3))

random.shuffle(values)
print(values)

# 生成随机整数
print(random.randint(0, 10))

# 0-1的浮点数
print(random.random())
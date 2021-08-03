from itertools import permutations, combinations, combinations_with_replacement

items = ['a', 'b', 'c']

for i in permutations(items):
    print(i)

print("-" * 20)
for i in permutations(items, 2):
    print(i) 

print("-" * 20)
for i in combinations(items, 2):
    print(i)

print("-" * 20)
for i in combinations_with_replacement(items, 3):
    print(i)
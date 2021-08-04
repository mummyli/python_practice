import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

# a和b必须是有序的
for x in heapq.merge(a, b):
    print(x, end=" ")
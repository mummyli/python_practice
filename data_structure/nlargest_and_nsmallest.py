import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

print("+" * 50)
# 指定关键字参数， 用于更加复杂的数据类型
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

ncheap = heapq.nsmallest(3, portfolio, key=lambda s: s["price"])
nexpensive = heapq.nlargest(3, portfolio, key=lambda s: s["price"])

print(ncheap)
print(nexpensive)

print("+" * 50)

# heapq提供了堆排序的相关算法
# 堆数据结构最重要的特征是 heap[0] 永远是最小的元素。
heap = list(nums)

# 构建堆
heapq.heapify(heap)
print(heap)

# 弹出元素
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
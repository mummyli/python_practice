prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 通过zip函数 反转键值 然后使用min、max、sorted等函数
maxprice = max(zip(prices.values(), prices.keys()))
minprice = min(zip(prices.values(), prices.keys()))
sortedPrices = sorted(zip(prices.values(), prices.keys()))
print(maxprice)
print(minprice)
print(sortedPrices)

# zip创建的是只能访问一次的迭代器
# 错误用法：prices_and_names = zip(prices.values(), prices.keys())
#          print(min(prices_and_names)) # OK
#          print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

print("+" * 50)
# min max sorted也可以指定key，但是返回结果为key
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))
print(sorted(prices, key=lambda k: prices[k]))
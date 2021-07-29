prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

## 字典推导
print({key: value for key, value in prices.items() if value>50})

## 或者创建元组序列，然后传递给dict
print(dict((key, value) for key, value in prices.items() if value>50))
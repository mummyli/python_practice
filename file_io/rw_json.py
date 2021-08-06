import json

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}

json_str = json.dumps(data)
print(type(json_str))
print(json_str)

data = json.loads(json_str)
print(type(data))
print(data)

print("\n", "-" * 80, "\n")

with open("./testfiles/data.json", "w") as f:
    json.dump(data, f)

with open("./testfiles/data.json") as f:
    result = json.load(f)
    print(result)

print("\n", "-" * 80, "\n")

'''
一般情况下 JSON解码会根据提供的数据 创建dict或者list
如果要创建其他类型对象 可以在json.load()时 传递object_pairs_hooks或object_hook参数
'''
from collections import OrderedDict

s = '{"name": "ACME", "shares": 100, "price": 542.23}'

data = json.loads(s, object_pairs_hook=OrderedDict)
print(type(data))
print(data)

# 对象实例
class JsonObject:
    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price

def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d

classes = {
    "JsonObject": JsonObject
}

def unserialize_instance(d):
    clsname = d.pop("__classname__", None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d

jsonObject = JsonObject(name="ACEM", shares=100, price=542.3)

s = json.dumps(jsonObject, default=serialize_instance)
print(s)

data = json.loads(s, object_hook=unserialize_instance)
print(data)
print(data.name)
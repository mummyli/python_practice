from collections import defaultdict

# 1、defaultdict会自动为将要访问的键（就算目前字典中并不存在这样的键）创建映射实体。
d = defaultdict(list)
# d = defaultdict(set)
d["a"].append(1)
d["a"].append(2)
d["b"].append(4)
print(d)

# 2、普通字典的setdefault方法
d = {}
d.setdefault("aa", []).append(1)
d.setdefault("aa", []).append(2)
d.setdefault("bb", []).append(4)
print(d)
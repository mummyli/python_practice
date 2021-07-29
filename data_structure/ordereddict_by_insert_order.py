from collections import OrderedDict

'''
OrderedDict 内部维护一个根据键插入顺序的双向链表。
新元素插入时 放到链表尾部。
对于已存在键的重复赋值 不改变位置
'''

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])

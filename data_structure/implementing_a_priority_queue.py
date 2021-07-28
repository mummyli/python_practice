import heapq

'''
heapq模块：heappush： 队列上插入一个元素
           heappop： 删除第一个元素
'''
class PriorityQueue:
    def __init__(self) -> None:
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self) -> str:
        return "Item({!r})".format(self.name)


if __name__ == "__main__":
    q = PriorityQueue()
    q.push(Item("foo"), 1)
    q.push(Item("bar"), 5)
    q.push(Item("spam"), 4)
    q.push(Item("grok"), 1)

    print(q.pop())
    print(q.pop())
    print(q.pop())
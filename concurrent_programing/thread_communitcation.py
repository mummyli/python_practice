from queue import Queue
import threading
import heapq

'''
线程安全队列 queue
'''
'''
使用Condition来自定义线程间通信数据结构
'''
class ProrityQueue:
    def __init__(self) -> None:
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()
    
    def put(self, item, prority):
        with self._cv:
            heapq.heappush(self._queue, (-prority, self._count, item))
            self._count += 1
            self._cv.notify()

    def get(self):
        with self._cv:
            while(len(self._queue) == 0):
                self._cv.wait()
            return heapq.heappop(self._queue)[-1]

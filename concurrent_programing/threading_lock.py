import threading

class SharedCounter:
    def __init__(self, initial_value:int = 0) -> None:
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta: int = 1) -> None:
        # 保证互斥最好只在临界区使用锁
        with self._value_lock:
            self._value += delta

    def decr(self, delta: int = 1) -> None:
        with self._value_lock:
            self._value -= delta
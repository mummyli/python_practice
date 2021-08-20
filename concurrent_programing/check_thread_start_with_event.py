from threading import Thread, Event
import time

'''
Event对象包含一个可以有线程设置的信号标志
初始状态下Event的信号标志设置为False
线程会一直等待Event信号标志位True
event对象最好单次使用
'''
def countdown(n: int, started_evt: Event) -> None:
    print("countdown starting")
    started_evt.set()
    while(n>0):
        print("T-minus", n)
        n -= 1
        time.sleep(5)

started_evt = Event()

print("Launching countdown")
t = Thread(target=countdown, args=(10, started_evt))

t.start()

started_evt.wait()

print("countdown is runnning")


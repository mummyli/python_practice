import time

def countdown(n):
    while(n>0):
        print("T-minus", n)
        n -= 1
        time.sleep(5)

def check_t_live(thd):
    while(thd.is_alive()):
        print("Still Running")
        time.sleep(2)
    
    print("Completed")

from threading import Thread
t = Thread(target=countdown, args=(10, ))
t.start()

t_check = Thread(target=check_t_live, args=(t, ))
t_check.start()

print("-" * 40)

class CountdownTask:
    def __init__(self) -> None:
        self._running = True
    
    def terminate(self):
        self._running = False

    def run(self, n):
        while(self._running and n>0):
            print("Countdown Task T-minus", n)
            n -= 1
            time.sleep(3)


c = CountdownTask()
t = Thread(target=c.run, args=(10, ))
t.start()
c.terminate()
t.join()
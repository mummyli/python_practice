from queue import Queue
from threading import Thread, Event

class ActorExit(Exception):
    pass

class Actor:
    def __init__(self) -> None:
        self._mailbox = Queue()

    def send(self, msg: str) -> None:
        self._mailbox.put(msg)

    def recv(self) -> str:
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        
        return msg
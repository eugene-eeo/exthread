from contextlib import contextmanager
from collections import deque
from .core import ExThread


class MQThread(ExThread):
    def __init__(self, target, *args, **kwargs):
        ExThread.__init__(self,
                          lambda *a, **k: target(self, *a, **k),
                          *args,
                          **kwargs)
        self.queue = deque()

    def put(self, k):
        self.queue.append(k)

    @contextmanager
    def ready(self):
        while not self.queue:
            pass
        yield

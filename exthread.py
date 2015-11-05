from enum import Enum
from threading import Thread


class Result(Enum):
    class Nothing: pass
    class Error: pass
    class Ok: pass


class ExThread(object):
    def __init__(self, target, *args, **kwargs):
        self.target = target
        self.thread = Thread(target=self.run,
                             *args,
                             **kwargs)
        self.result = Result.Nothing, None

    def run(self, *a, **kw):
        try:
            self.result = Result.Ok, target(*a, **kw)
        except BaseException as err:
            self.result = Result.Err, err

    def start(self):
        self.thread.start()

    def join(self, *a, **kw):
        self.thread.join(*a, **kw)

    def unwind(self, *a, **kw):
        self.join(*a, **kw)
        res, val = self.result
        if res is Result.Error:
            raise val
        return val

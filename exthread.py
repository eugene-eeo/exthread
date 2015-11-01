"""
    exthread
    ~~~~~~~~

    Opinionated and lightweight exception-propogating
    wrapper around the standard library thread.

    :copyright: (c) 2015 by Eeo Jun.
    :license: MIT, see LICENSE for details.
"""

from threading import Thread
from contextlib import contextmanager


def _catchbind(self, target):
    def wrapper():
        try:
            self.val = target()
        except BaseException as err:
            self.err = err
    return wrapper


class ExThread(object):
    """
    Exception propogating thread.

    :param target: Target function to execute.
    :param args: Sequence of positional arguments to be passed.
    :param kwargs: Mapping of keyword arguments to be passed.
    """
    err = None
    val = None

    def __init__(self, target, args=(), kwargs={}, **kw):
        self.thread = Thread(target=_catchbind(self, target),
                             args=args,
                             kwargs=kwargs,
                             **kw)

    def start(self):
        """
        Starts execution of the *target* function
        in another thread.
        """
        return self.thread.start()

    def join(self, timeout=None):
        """
        Wait for the thread to finish, may raise an
        exception (if any is uncaught during execution),
        and return the value returned by the target
        function.
        """
        rv = self.thread.join(timeout)
        if self.err:
            raise self.err
        return self.val

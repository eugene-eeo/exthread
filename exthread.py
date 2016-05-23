"""
    exthread
    ~~~~~~~~

    Opinionated and lightweight exception-propogating
    wrapper around the standard library thread.

    :copyright: (c) 2015 by Eeo Jun.
    :license: MIT, see LICENSE for details.
"""

from threading import Thread


class ExThread(object):
    """
    Exception propagating thread.

    :param target: Target function to execute.
    :param args: Sequence of positional arguments to be passed.
    :param kwargs: Mapping of keyword arguments to be passed.
    """
    err = None
    val = None

    def __init__(self, target, args=(), kwargs={}, **kw):
        self.target = target
        self.thread = Thread(target=self.run,
                             args=args,
                             kwargs=kwargs,
                             **kw)

    def run(self, *args, **kwargs):
        try:
            self.val = self.target(*args, **kwargs)
        except BaseException as err:
            self.err = err

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

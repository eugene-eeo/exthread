|logo| ExThread
===============

ExThread is an MIT-licensed library that provides supercharged
threads that is basically a wrapper around threads that allows
for exception propogation.

Usage:
------

To execute a function in a separate thread::

    >>> from exthread import ExThread
    >>> def task():
    ...     return 1
    ...
    >>> t = ExThread(task)
    >>> t.start()

Then to wait for it to complete, which may raise an exception
if any uncaught exceptions were raised while the task was
executing, as well as obtain the return value of the task::

    >>> t.join()
    1

.. |logo| image:: https://github.com/eugene-eeo/exthread/raw/master/images/logo.png

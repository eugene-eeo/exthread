|logo| ExThread
===============

ExThread is an MIT-licensed library that provides supercharged
threads - basically an opinionated wrapper around standard library
Threads that allows for exception propogation. Because we deserve
better exception semantics when writing/testing multithreaded
programs.

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

Installation:
-------------

From PyPI::

    $ pip install exthread

For hacking on ExThread it is recommended that you install
from the git repository::

    $ git clone git@github.com:eugene-eeo/exthread.git
    $ cd exthread
    $ pip install --editable .

.. |logo| image:: https://github.com/eugene-eeo/exthread/raw/master/images/small.png

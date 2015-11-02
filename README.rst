ExThread
========

Supercharged (sensible) execption propogating and lightweight
wrapper around the standard library Thread. Basically ensures
that you don't have to perform cartwheels just to ensure that
the execution of your threaded tests/programs do not fail behind
your back with some exception. Usage example:

.. code-block:: python

    >>> from exthread import ExThread
    >>> def task():
            arr = [1,2,3]
            arr[4]

    >>> t = ExThread(task)
    >>> t.start()
    >>> t.join()
    Traceback (most recent call last):
        ...
    IndexError: ...

You don't really need it. **But you want it.**

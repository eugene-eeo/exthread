# ExThread

<img src='https://github.com/eugene-eeo/exthread/raw/master/images/logo.png'
     align='left'/>

Supercharged (sensible) execption propogating and lightweight
wrapper around the standard library Thread. Basically ensures
that you don't have to perform cartwheels just to make sure
the execution of your threaded tests/programs do not fail behind
your back. Usage example:

```python
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
```

The API is deliciously simple:

```python
>>> def task(a, b=1):
        return [a, b]

>>> t = ExThread(task, (1,), dict(b=2))
>>> t.start()
>>> t.join()
[1, 2]
>>> assert t.err is None
>>> assert t.val == [1, 2]
```

You don't really need it. **But you want it.**

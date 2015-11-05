from pytest import raises
from exthread import ExThread


def test_exthread_init():
    thread = ExThread(lambda: [])
    assert thread.val is None
    assert thread.err is None


def test_exthread_join_return():
    thread = ExThread(lambda: [])
    thread.start()
    assert thread.join() == []


def test_exthread_join_value():
    thread = ExThread(lambda: [])
    thread.start()
    thread.join()

    assert not thread.err
    assert thread.val == []


def test_exthread_join_exception():
    def task():
        arr = [1,2,3]
        return arr[3]

    thread = ExThread(task)
    thread.start()

    with raises(IndexError):
        thread.join()

    assert isinstance(thread.err, IndexError)


def test_args_kwargs():
    def task(*args, **kwargs):
        assert args == (2, 2)
        assert kwargs == dict(c=2, d=2)

    thread = ExThread(task, (2,2), dict(c=2, d=2))
    thread.start()
    thread.join()

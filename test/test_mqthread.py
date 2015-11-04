from pytest import raises
from exthread import MQThread


def test_thread_reference():
    def assertion(t):
        assert t is mq

    mq = MQThread(assertion)
    mq.start()
    mq.join()


def test_put():
    mq = MQThread(lambda t: t.queue.popleft())
    mq.put(1)
    mq.put(2)
    mq.start()
    assert mq.join() == 1


def test_put_message():
    def task1(t):
        mq2.put(1)

    def task2(t):
        while not t.queue:
            pass
        return t.queue.popleft()

    mq1 = MQThread(task1)
    mq2 = MQThread(task2)

    mq1.start()
    mq2.start()
    mq1.join()
    assert mq2.join() == 1


def test_ready():
    def task(t):
        with t.ready():
            return t.queue.popleft()

    mq = MQThread(task)
    mq.put(1)
    mq.start()
    assert mq.join() == 1

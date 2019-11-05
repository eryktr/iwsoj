import time
from collections import deque
from threading import Lock
from typing import Deque, Callable, Tuple

FETCHLOCK = Lock()


class Job:
    fn: Callable
    args: Tuple

    def __init__(self, fn, args):
        self.fn = fn
        self.args = args

    def __call__(self):
        return self.fn(*self.args)


queue: Deque[Job] = deque()


def schedule(fn, args):
    queue.append(Job(fn, args))


def has_job():
    return bool(len(queue))


def fetch() -> Job:
    FETCHLOCK.acquire()
    while not has_job():
        time.sleep(1)
    j = queue.popleft()
    FETCHLOCK.release()
    return j


def popall():
    global queue
    queue = deque()

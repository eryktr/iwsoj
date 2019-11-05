import threading

import time

from scheduler import scheduler


def test_schedule():
    assert len(scheduler.queue) == 0
    scheduler.schedule(print, (1,))
    assert len(scheduler.queue) == 1


def test_fetch_job_present():
    scheduler.popall()
    scheduler.schedule(int, (7,))
    j = scheduler.fetch()
    assert j.fn is int
    assert j.args == (7,)


def test_has_job_job_present():
    scheduler.popall()
    scheduler.schedule(int, (1,))
    assert scheduler.has_job()


def test_has_job_no_job():
    scheduler.popall()
    assert not scheduler.has_job()


def test_job_callable():
    scheduler.popall()
    scheduler.schedule(int, ("10",))
    assert scheduler.fetch()() == 10


def test_fetch_nojobs_blocking():
    def delay_schedule():
        time.sleep(2)
        scheduler.schedule(int, ("11",))

    scheduler.popall()
    t1 = threading.Thread(target=scheduler.fetch)
    t2 = threading.Thread(target=delay_schedule)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

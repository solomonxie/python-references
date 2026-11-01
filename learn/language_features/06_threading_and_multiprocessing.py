"""
threading runs multiple OS threads within one process, sharing the same memory space.
Because of the GIL (see 05_gil.py), threads don't speed up CPU-bound work, but they do
help with I/O-bound work (network, disk, sleep), where a thread releases the GIL while
waiting. A Lock prevents race conditions when threads mutate shared state concurrently.

multiprocessing bypasses the GIL entirely by using separate memory spaces and OS
processes, giving true parallelism for CPU-bound work on multi-core systems — at the
cost of higher memory use and no shared state by default.
"""

import multiprocessing
import threading


def worker(num):
    print(f"Worker: {num}")


counter = 0
lock = threading.Lock()


def increment():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1


if __name__ == "__main__":
    # threading: good for I/O-bound concurrency
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    threads = [threading.Thread(target=increment) for _ in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Counter: {counter}")

    # multiprocessing: good for CPU-bound parallelism
    processes = [multiprocessing.Process(target=worker, args=(i,)) for i in range(2)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

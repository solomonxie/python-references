"""
The Global Interpreter Lock (GIL) is a mutex that lets only one thread execute Python
bytecode at a time, even on a multi-core machine. This demonstrates its effect: running
a CPU-bound task across threads is no faster than running it single-threaded, because
threads take turns holding the GIL instead of running in parallel.
"""

import threading
import time


def cpu_bound(n):
    while n > 0:
        n -= 1


def run(num_workers, use_threads):
    workers = [
        threading.Thread(target=cpu_bound, args=(20_000_000,)) if use_threads else None
        for _ in range(num_workers)
    ]
    start = time.perf_counter()
    if use_threads:
        for w in workers:
            w.start()
        for w in workers:
            w.join()
    else:
        for _ in range(num_workers):
            cpu_bound(20_000_000)
    return time.perf_counter() - start


if __name__ == "__main__":
    single = run(1, use_threads=False)
    threaded = run(4, use_threads=True)
    print(f"Single-threaded (1x work): {single:.2f}s")
    print(f"4 threads (4x work):        {threaded:.2f}s")
    print("GIL prevents threads from scaling CPU-bound work — see 06_threading_and_multiprocessing.py for a process-based fix.")

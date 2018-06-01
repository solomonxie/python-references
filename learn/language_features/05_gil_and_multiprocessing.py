"""
The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes at once.
Multiprocessing bypasses the GIL by using separate memory spaces and multiple OS processes, allowing for true parallelism on multi-core systems.
"""

import multiprocessing


def worker(num):
    print(f"Worker: {num}")


if __name__ == "__main__":
    processes = []
    for i in range(2):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

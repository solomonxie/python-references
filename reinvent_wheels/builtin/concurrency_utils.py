"""
A minimal thread-pool task manager, reinvented on top of `threading` + `queue`
instead of pulling in `concurrent.futures` (or a 3rd party lib).

Usage:
    pool = ThreadPoolManager(concurrency=5)
    for key, url in urls.items():
        pool.add_task(key, requests.get, url)
    result_map = pool.get_result()  # {key: return_value_or_exception}
"""
import logging
import threading
from queue import Queue

logger = logging.getLogger(__name__)


class ThreadPoolManager:
    """Runs an arbitrary number of callables across a fixed pool of worker threads.

    Each task is keyed, so results (or exceptions) can be looked back up by
    that key once every task has finished.
    """

    def __init__(self, concurrency: int = 5):
        self.concurrency = max(1, int(concurrency))
        self._tasks = Queue()
        self._results = {}
        self._lock = threading.Lock()

    def add_task(self, key, func, *args, **kwargs):
        self._tasks.put((key, func, args, kwargs))

    def _worker(self):
        while True:
            try:
                key, func, args, kwargs = self._tasks.get_nowait()
            except Exception:
                return
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logger.exception(f'Task [{key}] failed: {e}')
                result = e
            with self._lock:
                self._results[key] = result
            self._tasks.task_done()

    def get_result(self) -> dict:
        """Runs every queued task to completion and returns {key: result}.

        A task that raised keeps its exception object as the "result" instead
        of failing the whole batch, so callers can inspect per-task success.
        """
        worker_count = min(self.concurrency, self._tasks.qsize()) or 1
        workers = [threading.Thread(target=self._worker, daemon=True) for _ in range(worker_count)]
        for w in workers:
            w.start()
        for w in workers:
            w.join()
        return self._results

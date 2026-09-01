# $ docker run --rm --name redis-server -p 6379:6379 redis
# $ python3 01_redis_window_counter.py
#
# A rolling-window request counter backed by Redis, without a sorted-set
# per request (which gets expensive at high volume). Time is sliced into
# fixed-size buckets (a minute each, or an hour each for long windows);
# each bucket is a single INCR'd key that expires on its own. A window's
# count is the sum of however many trailing buckets cover it — an
# approximation of a true sliding window, but O(buckets) instead of
# O(requests) per check.

import math
import time
from datetime import datetime, timedelta


class WindowCounter:
    def __init__(self, redis_conn, key, window_seconds):
        if window_seconds < 60:
            raise ValueError("window_seconds must be >= 60")
        self.conn = redis_conn
        self.key = key
        self.window_seconds = window_seconds
        # coarser buckets for longer windows keep the bucket count (and
        # thus the number of keys read per check) small
        self.bucket_seconds = 3600 if window_seconds >= 3600 else 60
        self.bucket_ttl = window_seconds * 2

    def _bucket_key(self, dt):
        fmt = "%Y%m%d%H" if self.bucket_seconds == 3600 else "%Y%m%d%H%M"
        return f"{self.key}:{dt.strftime(fmt)}"

    def _bucket_keys_covering_window(self, dt):
        n = math.ceil(self.window_seconds / self.bucket_seconds)
        keys = []
        for _ in range(n):
            keys.append(self._bucket_key(dt))
            dt -= timedelta(seconds=self.bucket_seconds)
        return keys

    def increment(self, amount=1, at=None):
        dt = at or datetime.now()
        key = self._bucket_key(dt)
        is_new = not self.conn.exists(key)
        value = self.conn.incrby(key, amount)
        if is_new:
            self.conn.expire(key, self.bucket_ttl)
        return value

    def count(self, at=None):
        dt = at or datetime.now()
        keys = self._bucket_keys_covering_window(dt)
        values = self.conn.mget(keys)
        return sum(int(v) for v in values if v is not None)

    def reset(self, at=None):
        dt = at or datetime.now()
        self.conn.delete(*self._bucket_keys_covering_window(dt))


if __name__ == "__main__":
    import redis
    conn = redis.Redis(host="localhost", port=6379, decode_responses=True)

    counter = WindowCounter(conn, key="rl:demo:login", window_seconds=60)
    counter.reset()

    for i in range(5):
        total = counter.increment()
        print(f"request {i + 1}: {total} in the last 60s")

    print("count() without incrementing:", counter.count())
    time.sleep(1)
    print("still there a second later:", counter.count())

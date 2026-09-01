# $ docker run --rm --name redis-server -p 6379:6379 redis
# $ python3 04_blacklist_escalation.py
#
# Rate limiting alone just delays an abuser by a window; a repeat offender
# should get shut out for longer. Two Redis sets, checked before any
# counting happens: a temp blacklist (short block, e.g. "solve a captcha"),
# and a perm blacklist (long/permanent block) that a caller graduates into
# after tripping the temp one enough times.

import math
from datetime import datetime, timedelta


class WindowCounter:
    def __init__(self, redis_conn, key, window_seconds):
        self.conn = redis_conn
        self.key = key
        self.window_seconds = window_seconds
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

    def reset(self, at=None):
        dt = at or datetime.now()
        self.conn.delete(*self._bucket_keys_covering_window(dt))


class Blacklist:
    def __init__(self, redis_conn, key):
        self.conn = redis_conn
        self.key = key

    def add(self, identity):
        self.conn.sadd(self.key, identity)

    def remove(self, identity):
        self.conn.srem(self.key, identity)

    def contains(self, identity):
        return self.conn.sismember(self.key, identity)


class EscalatingLoginLimiter:
    """
    - trips_within `temp_window`   -> temp-blocked (removed once the window
                                       counter for THAT block resets)
    - trips_within `perm_window`   -> perm-blocked (stays blocked)
    """

    def __init__(self, redis_conn, key_prefix,
                 temp_threshold=5, temp_window=120,
                 perm_threshold=20, perm_window=3600):
        self.conn = redis_conn
        self.temp_blacklist = Blacklist(redis_conn, f"{key_prefix}:bl:temp")
        self.perm_blacklist = Blacklist(redis_conn, f"{key_prefix}:bl:perm")
        self.temp_counter_prefix = f"{key_prefix}:cnt:temp"
        self.perm_counter_prefix = f"{key_prefix}:cnt:perm"
        self.temp_threshold = temp_threshold
        self.temp_window = temp_window
        self.perm_threshold = perm_threshold
        self.perm_window = perm_window

    def record_failed_login(self, ip):
        if self.perm_blacklist.contains(ip):
            return "perm_blocked"

        temp_counter = WindowCounter(self.conn, f"{self.temp_counter_prefix}:{ip}", self.temp_window)
        perm_counter = WindowCounter(self.conn, f"{self.perm_counter_prefix}:{ip}", self.perm_window)

        if temp_counter.increment() > self.temp_threshold:
            self.temp_blacklist.add(ip)

        if perm_counter.increment() > self.perm_threshold:
            self.perm_blacklist.add(ip)
            self.temp_blacklist.remove(ip)  # perm supersedes temp
            return "perm_blocked"

        return "temp_blocked" if self.temp_blacklist.contains(ip) else "ok"


if __name__ == "__main__":
    import redis
    conn = redis.Redis(host="localhost", port=6379, decode_responses=True)
    conn.flushdb()

    limiter = EscalatingLoginLimiter(
        conn, key_prefix="rl:demo:login",
        temp_threshold=3, temp_window=120,
        perm_threshold=6, perm_window=3600,
    )
    for i in range(8):
        status = limiter.record_failed_login("203.0.113.9")
        print(f"failed login {i + 1}: {status}")

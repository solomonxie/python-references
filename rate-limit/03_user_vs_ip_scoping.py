# $ docker run --rm --name redis-server -p 6379:6379 redis
# $ python3 03_user_vs_ip_scoping.py
#
# The same endpoint often needs two different limiter scopes: logged-in
# calls are counted per user_id (so one user can't be starved by another
# sharing a NAT'd IP), anonymous calls fall back to per-IP (the only
# identity available). A whitelist short-circuits both — trusted callers
# skip counting entirely.

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


class Whitelist:
    """Redis set of trusted ids/IPs that bypass rate limiting entirely."""

    def __init__(self, redis_conn, key):
        self.conn = redis_conn
        self.key = key

    def add(self, identity):
        self.conn.sadd(self.key, identity)

    def contains(self, identity):
        return identity is not None and self.conn.sismember(self.key, identity)


class UserOrIPRateLimiter:
    def __init__(self, redis_conn, key_prefix, window_seconds, threshold):
        self.threshold = threshold
        self.window_seconds = window_seconds
        self.key_prefix = key_prefix
        self.conn = redis_conn
        self.user_whitelist = Whitelist(redis_conn, f"{key_prefix}:wl:user")
        self.ip_whitelist = Whitelist(redis_conn, f"{key_prefix}:wl:ip")

    def _counter_for(self, scope, identity):
        return WindowCounter(self.conn, f"{self.key_prefix}:{scope}:{identity}", self.window_seconds)

    def is_allowed(self, user_id=None, ip=None):
        if user_id is not None:
            if self.user_whitelist.contains(user_id):
                return True
            return self._counter_for("user", user_id).increment() <= self.threshold

        if self.ip_whitelist.contains(ip):
            return True
        return self._counter_for("ip", ip).increment() <= self.threshold


if __name__ == "__main__":
    import redis
    conn = redis.Redis(host="localhost", port=6379, decode_responses=True)
    conn.flushdb()

    limiter = UserOrIPRateLimiter(conn, key_prefix="rl:demo:api", window_seconds=60, threshold=3)
    limiter.ip_whitelist.add("10.0.0.1")

    for i in range(4):
        print(f"user 42, call {i + 1}:", limiter.is_allowed(user_id=42))
    for i in range(4):
        print(f"anon 203.0.113.5, call {i + 1}:", limiter.is_allowed(ip="203.0.113.5"))
    for i in range(4):
        print(f"whitelisted 10.0.0.1, call {i + 1}:", limiter.is_allowed(ip="10.0.0.1"))

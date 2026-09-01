# $ docker run --rm --name redis-server -p 6379:6379 redis
# $ python3 02_weighted_and_tiered_quotas.py
#
# Two upgrades over a flat "1 request = 1 unit" counter (see
# 01_redis_window_counter.py for the WindowCounter this builds on):
# 1. Weighted cost — a single request can consume more than one unit
#    (e.g. exporting 10,000 rows costs more than fetching 10), so the
#    limiter charges a computed amount instead of always incrementing by 1.
# 2. Tiered thresholds — the limit itself depends on who's asking (a paid
#    plan gets a bigger budget).

import math
from datetime import datetime, timedelta


class WindowCounter:
    """Same fixed-bucket counter as 01_redis_window_counter.py."""

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


class TieredRateLimiter:
    """threshold/window pair chosen per plan tier, cost computed per request."""

    def __init__(self, redis_conn, key_prefix, window_seconds, threshold_by_tier):
        self.threshold_by_tier = threshold_by_tier
        self.counters = {
            tier: WindowCounter(redis_conn, f"{key_prefix}:{tier}", window_seconds)
            for tier in threshold_by_tier
        }

    def check_and_consume(self, tier, cost=1):
        counter = self.counters[tier]
        threshold = self.threshold_by_tier[tier]
        total = counter.increment(cost)
        return total <= threshold


def cost_for_export(row_count):
    """1 unit per 1,000 rows, minimum 1 — a bulk export should cost more
    than a tiny one against the same per-minute budget."""
    return max(1, row_count // 1000)


if __name__ == "__main__":
    import redis
    conn = redis.Redis(host="localhost", port=6379, decode_responses=True)

    limiter = TieredRateLimiter(
        conn, key_prefix="rl:demo:export", window_seconds=60,
        threshold_by_tier={"free": 5, "paid": 50},
    )
    for counter in limiter.counters.values():
        counter.reset()

    for row_count in [500, 4000, 12000]:
        cost = cost_for_export(row_count)
        allowed = limiter.check_and_consume("free", cost=cost)
        print(f"free tier export of {row_count} rows costs {cost} units -> allowed={allowed}")

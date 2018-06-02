"""
OOD: Rate Limiter.
Sliding-window-log limiter: keeps per-client timestamps and rejects a
request once more than `limit` requests fall inside the trailing window.
"""
from collections import defaultdict, deque


class SlidingWindowRateLimiter:
    def __init__(self, limit, window_seconds):
        self.limit = limit
        self.window = window_seconds
        self.requests = defaultdict(deque)

    def allow(self, client_id, now):
        log = self.requests[client_id]
        while log and now - log[0] >= self.window:
            log.popleft()
        if len(log) < self.limit:
            log.append(now)
            return True
        return False


if __name__ == "__main__":
    limiter = SlidingWindowRateLimiter(limit=3, window_seconds=10)

    for t in [0, 1, 2, 3, 11]:
        allowed = limiter.allow("client-1", now=t)
        print(f"t={t}: {'allowed' if allowed else 'rejected'}")

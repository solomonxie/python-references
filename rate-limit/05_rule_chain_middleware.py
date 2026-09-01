# $ docker run --rm --name redis-server -p 6379:6379 redis
# $ pip install fastapi uvicorn redis
# $ uvicorn 05_rule_chain_middleware:app --reload
# $ for i in $(seq 1 5); do curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8000/search; done
#
# Ties 01-04 together: a request is checked against an ordered list of
# independent rules. Each rule answers ALLOW (stop, let it through — e.g.
# a whitelist hit), REJECT (stop, block it), or CONTINUE (defer to the
# next rule). This is how a gateway runs a dozen unrelated limiter/
# blacklist checks per request without them needing to know about each
# other.

import math
from datetime import datetime, timedelta
from enum import Enum, auto

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


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


class RuleResult(Enum):
    ALLOW = auto()      # short-circuit: request is let through
    REJECT = auto()      # short-circuit: request is blocked
    CONTINUE = auto()   # defer to the next rule in the chain


class Rule:
    def check(self, redis_conn, ip: str) -> RuleResult:
        raise NotImplementedError


class WhitelistRule(Rule):
    def __init__(self, trusted_ips):
        self.trusted_ips = set(trusted_ips)

    def check(self, redis_conn, ip):
        return RuleResult.ALLOW if ip in self.trusted_ips else RuleResult.CONTINUE


class PermBlacklistRule(Rule):
    def check(self, redis_conn, ip):
        if redis_conn.sismember("rl:demo:bl:perm", ip):
            return RuleResult.REJECT
        return RuleResult.CONTINUE


class FrequencyRule(Rule):
    def __init__(self, key, window_seconds, threshold):
        self.key = key
        self.window_seconds = window_seconds
        self.threshold = threshold

    def check(self, redis_conn, ip):
        counter = WindowCounter(redis_conn, f"{self.key}:{ip}", self.window_seconds)
        return RuleResult.CONTINUE if counter.increment() <= self.threshold else RuleResult.REJECT


class RuleChain:
    def __init__(self, rules):
        self.rules = rules

    def evaluate(self, redis_conn, ip):
        for rule in self.rules:
            result = rule.check(redis_conn, ip)
            if result in (RuleResult.ALLOW, RuleResult.REJECT):
                return result
        return RuleResult.ALLOW  # nothing objected


app = FastAPI()
chain = RuleChain([
    WhitelistRule(trusted_ips={"10.0.0.1"}),
    PermBlacklistRule(),
    FrequencyRule(key="rl:demo:search:1min", window_seconds=60, threshold=3),
])


def get_redis():
    import redis
    return redis.Redis(host="localhost", port=6379, decode_responses=True)


@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    conn = get_redis()
    ip = request.client.host
    if chain.evaluate(conn, ip) == RuleResult.REJECT:
        return JSONResponse(status_code=429, content={"detail": "rate limit exceeded"})
    return await call_next(request)


@app.get("/search")
def search():
    return {"results": []}

# Rate Limiting

Techniques for a production API gateway's rate limiter, distilled from a
real Redis-backed anti-abuse system (endpoint paths, service names, and
company-specific numbers generalized away — only the mechanisms remain).
Each file builds on the `WindowCounter` from `01`.

```sh
docker run --rm --name redis-server -p 6379:6379 redis
pip install redis fastapi uvicorn
python3 01_redis_window_counter.py
```

| File | Demonstrates |
|---|---|
| `01_redis_window_counter.py` | Approximate rolling window via fixed time buckets in Redis, each auto-expiring |
| `02_weighted_and_tiered_quotas.py` | Charging a request more than 1 unit by cost, and different thresholds per plan tier |
| `03_user_vs_ip_scoping.py` | Scoping the same limiter by user_id when authenticated, by IP when anonymous, with a whitelist bypass |
| `04_blacklist_escalation.py` | Promoting a repeat offender from a short temp-block to a permanent one |
| `05_rule_chain_middleware.py` | Composing whitelist/blacklist/frequency checks into one ALLOW/REJECT/CONTINUE chain, wired into FastAPI |

A fixed-bucket counter is an *approximation* of a true sliding window (it
can under- or over-count near a bucket boundary) — good enough for abuse
prevention, where "roughly right, cheap, and fast" beats "exact but a sorted
set scan per request."

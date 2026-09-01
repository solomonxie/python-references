# Authentication

Techniques from a real API gateway's multi-strategy authentication layer
(endpoint paths, service names, and company-specific details generalized
away — only the mechanisms remain), plus standard reference
implementations for JWT and magic-link login to round out the common
methods.

```sh
docker run --rm --name redis-server -p 6379:6379 redis
pip install cachetools redis pyjwt fastapi uvicorn
python3 01_bearer_token_remote_verify.py
```

| File | Demonstrates |
|---|---|
| `01_bearer_token_remote_verify.py` | Opaque bearer token verified by a remote auth service, with a short-TTL cache so every request isn't a round trip |
| `02_session_cookie_auth.py` | Server-side session: opaque cookie id looked up in a Redis-backed store, revoked with a single DEL |
| `03_jwt_auth.py` | Stateless signed token carrying its own claims and expiry |
| `04_magic_link_email_auth.py` | Passwordless login link, single-use via atomic GETDEL |
| `05_ip_whitelist_auth.py` | Trusted-network auth for internal service-to-service calls |
| `06_auth_chain_middleware.py` | Composing several of the above into one gateway: first authenticator to return a user wins |

`01`, `02`, and `05` mirror the real gateway's approach directly (delegate
to a remote identity service, or trust the network); `03` and `04` are
standard reference implementations for methods the source gateway didn't
happen to use, included since they're common in practice.

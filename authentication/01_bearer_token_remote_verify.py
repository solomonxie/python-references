# $ pip install cachetools
# $ python3 01_bearer_token_remote_verify.py
#
# A gateway often doesn't know how to validate a token itself (OAuth
# access tokens, API keys) — it forwards the token to an internal auth
# service and trusts whatever comes back. That remote call is too slow to
# make on every single request, so the result is cached for a short TTL
# keyed by the token itself: repeat calls within the window are free, and
# a revoked token still take effect within one TTL window.

from cachetools import cachedmethod, TTLCache
from cachetools.keys import hashkey

remote_calls_made = 0


def call_remote_auth_service(token):
    """Stands in for an HTTP call to an internal auth/user service."""
    global remote_calls_made
    remote_calls_made += 1
    fake_token_db = {"tok-alice": {"user_id": 1, "email": "alice@example.com"}}
    return fake_token_db.get(token)


class BearerTokenAuthenticator:
    def __init__(self, ttl_seconds=60, cache_size=1024):
        self._cache = TTLCache(maxsize=cache_size, ttl=ttl_seconds)

    def should_handle(self, headers):
        auth = headers.get("authorization", "")
        parts = auth.split()
        return len(parts) == 2 and parts[0].lower() == "bearer"

    def authenticate(self, headers):
        if not self.should_handle(headers):
            return None
        token = headers["authorization"].split()[1]
        return self._verify_cached(token)

    @cachedmethod(lambda self: self._cache, key=lambda self, token: hashkey(token))
    def _verify_cached(self, token):
        return call_remote_auth_service(token)


if __name__ == "__main__":
    auth = BearerTokenAuthenticator(ttl_seconds=60)
    headers = {"authorization": "Bearer tok-alice"}

    for i in range(5):
        user = auth.authenticate(headers)
        print(f"request {i + 1}: user={user}, remote calls so far={remote_calls_made}")

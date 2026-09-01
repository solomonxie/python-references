# $ docker run --rm --name redis-server -p 6379:6379 redis
# $ pip install redis
# $ python3 04_magic_link_email_auth.py
#
# Passwordless login: generate a single-use, short-lived token, "email" a
# link containing it, and consume it exactly once when clicked. The
# single-use part matters — a plain TTL key would let the same link log
# someone in twice; GETDEL (atomic get-then-delete) makes redeeming a
# link and invalidating it one operation, so two racing clicks can't both
# succeed.

import secrets


class MagicLinkAuthenticator:
    def __init__(self, redis_conn, ttl_seconds=15 * 60):
        self.conn = redis_conn
        self.ttl_seconds = ttl_seconds

    def send_login_link(self, email: str) -> str:
        token = secrets.token_urlsafe(24)
        self.conn.set(f"magic:{token}", email, ex=self.ttl_seconds)
        link = f"https://example.com/login/magic?token={token}"
        print(f"[email to {email}] click to log in: {link}")
        return token

    def consume(self, token: str):
        """Redeems the token; returns the email once, then never again."""
        return self.conn.getdel(f"magic:{token}")


if __name__ == "__main__":
    import redis
    conn = redis.Redis(host="localhost", port=6379, decode_responses=True)

    auth = MagicLinkAuthenticator(conn, ttl_seconds=900)
    token = auth.send_login_link("alice@example.com")

    print("first click:", auth.consume(token))
    print("second click (already used):", auth.consume(token))

# $ docker run --rm --name redis-server -p 6379:6379 redis
# $ pip install redis
# $ python3 02_session_cookie_auth.py
#
# Classic server-side session: login creates a random opaque session id,
# stores the user data behind it in Redis with a TTL, and hands the id
# back as a cookie. Every later request just looks the id up — no
# encoding/decoding, no secret key, revocation is a single DEL.

import secrets


class SessionStore:
    def __init__(self, redis_conn, ttl_seconds=60 * 60 * 24 * 7):
        self.conn = redis_conn
        self.ttl_seconds = ttl_seconds

    def create(self, user_data: dict) -> str:
        session_id = secrets.token_urlsafe(32)
        self.conn.hset(f"session:{session_id}", mapping=user_data)
        self.conn.expire(f"session:{session_id}", self.ttl_seconds)
        return session_id

    def get_user(self, session_id: str):
        data = self.conn.hgetall(f"session:{session_id}")
        return data or None

    def revoke(self, session_id: str):
        self.conn.delete(f"session:{session_id}")


class SessionCookieAuthenticator:
    COOKIE_NAME = "session_id"

    def __init__(self, session_store: SessionStore):
        self.store = session_store

    def authenticate(self, cookies: dict):
        session_id = cookies.get(self.COOKIE_NAME)
        if not session_id:
            return None
        return self.store.get_user(session_id)


if __name__ == "__main__":
    import redis
    conn = redis.Redis(host="localhost", port=6379, decode_responses=True)

    store = SessionStore(conn, ttl_seconds=3600)
    session_id = store.create({"user_id": "1", "email": "alice@example.com"})
    print("login sets cookie:", session_id)

    auth = SessionCookieAuthenticator(store)
    print("authenticated:", auth.authenticate({"session_id": session_id}))

    store.revoke(session_id)
    print("after logout:", auth.authenticate({"session_id": session_id}))

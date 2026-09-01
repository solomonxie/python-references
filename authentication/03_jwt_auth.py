# $ pip install pyjwt
# $ python3 03_jwt_auth.py
#
# Stateless alternative to a session/cookie lookup: the token itself
# carries the claims, signed so the server can trust it without a
# database round-trip. Cheap to verify, but revocation before expiry
# needs its own mechanism (e.g. a blacklist of token ids) since there's
# no server-side record to delete.

import time

import jwt

SECRET = "dev-secret-change-me-32-bytes-min"  # load from env/secret-manager in real use
ALGORITHM = "HS256"


def issue_token(user_id: int, email: str, ttl_seconds=3600) -> str:
    now = int(time.time())
    claims = {
        "sub": str(user_id),
        "email": email,
        "iat": now,
        "exp": now + ttl_seconds,
    }
    return jwt.encode(claims, SECRET, algorithm=ALGORITHM)


def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


class JWTAuthenticator:
    def authenticate(self, headers: dict):
        auth = headers.get("authorization", "")
        parts = auth.split()
        if len(parts) != 2 or parts[0].lower() != "bearer":
            return None
        return verify_token(parts[1])


if __name__ == "__main__":
    token = issue_token(user_id=1, email="alice@example.com", ttl_seconds=2)
    print("issued:", token)

    auth = JWTAuthenticator()
    print("valid token:", auth.authenticate({"authorization": f"Bearer {token}"}))

    print("tampered token:", auth.authenticate({"authorization": f"Bearer {token}x"}))

    time.sleep(3)
    print("after expiry:", auth.authenticate({"authorization": f"Bearer {token}"}))

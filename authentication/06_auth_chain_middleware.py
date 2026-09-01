# $ pip install fastapi uvicorn pyjwt
# $ uvicorn 06_auth_chain_middleware:app --reload
# $ curl http://127.0.0.1:8000/whoami                                     # 401
# $ curl -H "X-Session-Token: sess-alice" http://127.0.0.1:8000/whoami    # session cookie/header
# $ curl -H "Authorization: Bearer <jwt>" http://127.0.0.1:8000/whoami    # JWT
#
# Real gateways accept several auth methods on the same endpoint (browser
# session cookie, mobile app JWT, service-to-service IP allowlist) and
# try them in priority order — first one that returns a user wins, same
# shape as 01-05 but composed instead of picked upfront.

import time

import jwt
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

JWT_SECRET = "dev-secret-change-me-32-bytes-min"
FAKE_SESSION_STORE = {"sess-alice": {"user_id": 1, "email": "alice@example.com"}}


class Authenticator:
    def authenticate(self, request: Request):
        raise NotImplementedError


class JWTBearerAuthenticator(Authenticator):
    def authenticate(self, request):
        auth = request.headers.get("authorization", "")
        parts = auth.split()
        if len(parts) != 2 or parts[0].lower() != "bearer":
            return None
        try:
            return jwt.decode(parts[1], JWT_SECRET, algorithms=["HS256"])
        except jwt.InvalidTokenError:
            return None


class SessionHeaderAuthenticator(Authenticator):
    """Stand-in for a cookie-based session lookup (see 02_session_cookie_auth.py)."""

    def authenticate(self, request):
        token = request.headers.get("x-session-token")
        if not token:
            return None
        return FAKE_SESSION_STORE.get(token)


class AuthenticationChain:
    def __init__(self, authenticators):
        self.authenticators = authenticators

    def authenticate(self, request: Request):
        for authenticator in self.authenticators:
            user = authenticator.authenticate(request)
            if user:
                return user
        return None


chain = AuthenticationChain([
    JWTBearerAuthenticator(),
    SessionHeaderAuthenticator(),
])

app = FastAPI()


@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    request.state.user = chain.authenticate(request)
    return await call_next(request)


@app.get("/whoami")
def whoami(request: Request):
    if not request.state.user:
        return JSONResponse(status_code=401, content={"detail": "unauthenticated"})
    return {"user": request.state.user}


if __name__ == "__main__":
    demo_jwt = jwt.encode(
        {"sub": "2", "email": "bob@example.com", "exp": int(time.time()) + 3600},
        JWT_SECRET, algorithm="HS256",
    )
    print("demo JWT for curl:", demo_jwt)

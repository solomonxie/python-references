"""
API Exception: Has a `status_code`
"""

INTERNAL_ERROR_MESSAGE = 'Internal error, contact support@example.com if this problem persists.'

OK = ('OK', 200)
NOT_MODIFIED = ('Not modified', 304)
BAD_REQUEST = ('Bad request', 400)
UNAUTHORIZED = ('Unauthorized access', 401)
FORBIDDEN = ('User account does not have access.', 403)
IP_ADDRESS_ILLEGAL = ('You are requesting from an IP address that is not associated with your account', 403)
METHOD_NOT_SUPPORT = ('HTTP method is not supported', 405)
TEMP_BLACKLISTED = ('User/IP is temporarily blacklisted', 428)
USER_IP_NOT_IN_REQUEST = ('User_ip is not in Request', 440)
USER_ID_NOT_IN_REQUEST = ('User_id is not in Request', 441)
INTERNAL_ERROR = (INTERNAL_ERROR_MESSAGE, 500)
REQUEST_REMOTE_ERROR = (INTERNAL_ERROR_MESSAGE, 521)
DATA_ERROR = ('Data is corrupted or incomplete', 501)
# 53X: reverse-proxy could not get a response from the upstream service
NGINX_500 = (INTERNAL_ERROR_MESSAGE, 530)
NGINX_502 = (INTERNAL_ERROR_MESSAGE, 532)
NGINX_504 = (INTERNAL_ERROR_MESSAGE, 534)
TOO_MANY_REQUEST = ('Too many requests, please try again later.', 429)
UPSTREAM_REQUEST_FAILED = (INTERNAL_ERROR_MESSAGE, 539)
# 54X: a downstream/internal service returned an error
DOWNSTREAM_SERVICE_ERROR = (INTERNAL_ERROR_MESSAGE, 540)


class CustomExceptionBase(Exception):
    def __init__(self, message=None, ex=None, code=500):
        self.ex = ex
        self.code = code
        self.message = message


class RequestRemoteError(CustomExceptionBase):
    def __init__(self, message=REQUEST_REMOTE_ERROR[0], ex=None, code=REQUEST_REMOTE_ERROR[1]):
        message = f'Remote error: {message}'
        super().__init__(ex=ex, message=message, code=code)


class DataError(CustomExceptionBase):
    def __init__(self, message=DATA_ERROR[0], ex=None, code=DATA_ERROR[1]):
        message = f'Data error: {message}'
        super().__init__(ex=ex, message=message, code=code)


class ServerError(CustomExceptionBase):
    def __init__(self, message=INTERNAL_ERROR[0], ex=None, code=INTERNAL_ERROR[1]):
        message = f'Server error: {message}'
        super().__init__(ex=ex, message=message, code=code)


class RateLimitationError(CustomExceptionBase):
    def __init__(self, message=TOO_MANY_REQUEST[0], ex=None, code=TOO_MANY_REQUEST[1]):
        message = f'Too many requests: {message}'
        super().__init__(ex=ex, message=message, code=code)


class UserInputError(CustomExceptionBase):
    def __init__(self, message=None, ex=None, code=400):
        message = f'Input error: {message}'
        super().__init__(ex=ex, message=message, code=code)


class UserPermissionError(CustomExceptionBase):
    def __init__(self, message=None, ex=None, code=403):
        message = f'Permission error: {message}'
        super().__init__(ex=ex, message=message, code=code)


class GracefulExit(CustomExceptionBase):
    """ Used to gracefully exit the process without an error """
    def __init__(self, message=None, ex=None, code=200):
        message = f'Graceful exit: {message}'
        super().__init__(ex=ex, message=message, code=code)


Name2ErrorType = {
    'RequestRemoteError': RequestRemoteError,
    'DataError': RequestRemoteError,
    'ServerError': ServerError,
    'RateLimitationError': RequestRemoteError,
    'UserInputError': RequestRemoteError,
    'UserPermissionError': RequestRemoteError,
    'GracefulExit': GracefulExit,
}


def get_error_by_name(name: str) -> type:
    if not name:
        return None
    if Name2ErrorType.get(name):
        cls = Name2ErrorType[name]
    elif 'runtime' in name.lower():
        cls = RuntimeError
    elif 'memory' in name.lower():
        cls = MemoryError
    else:
        cls = ServerError
    return cls
